from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from ai22b.talent_foundry.agent_manifest import build_agent_manifest
from ai22b.talent_foundry.distribution import (
    create_agent_release_bundle,
    install_agent_release_package,
    package_agent_release_bundle,
)
from ai22b.talent_foundry.employment import create_employment_contract
from ai22b.talent_foundry.institutions import run_institutional_review
from ai22b.talent_foundry.learning_loop import (
    build_reasoning_kernel,
    create_learning_ledger,
    record_learning_experience,
)
from ai22b.talent_foundry.memory import consolidate_memory, create_memory_store, remember_event
from ai22b.talent_foundry.program import create_talent_plan
from ai22b.talent_foundry.records import build_career_records
from ai22b.talent_foundry.registry import hire_installed_agent


TRAINING_RUN_SCHEMA = "ai-talent-training-run/v1"


def _write_json(path: Path, data: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")


def _slug(text: str) -> str:
    slug = "".join(char.lower() if char.isalnum() else "_" for char in text)
    return "_".join(part for part in slug.split("_") if part) or "talent"


def _submissions_for(blueprint: dict[str, Any]) -> dict[str, dict[str, Any]]:
    track = blueprint["track"]
    doctoral_project = track["doctoral_project"]
    return {
        "school_exam": {
            "answer": "기초 규칙을 복습하고 근거를 확인한다.",
            "project": "학교 정기시험",
            "evidence": ["오답노트", "복습기록", "담임평가"],
        },
        "csat": {
            "answer": "종합 문제에서 추론, 비교, 검증 절차를 분리한다.",
            "project": "수능형 종합평가",
            "evidence": ["모의고사", "풀이기록", "검증표"],
        },
        "university_graduation": {
            "answer": "전공 프로젝트에서 데이터와 검증 기준을 분리한다.",
            "project": f"{track['name']} 전공 프로젝트",
            "evidence": ["전공 프로젝트", "데이터카드", "재현로그"],
        },
        "doctoral_defense": {
            "answer": f"{doctoral_project}에서 근거, 검증, 안전 경계, 추론기풍을 분리해 설명한다.",
            "project": doctoral_project,
            "evidence": ["논문", "실험 로그", "보스 검토 기록"],
        },
    }


def _hiring_packet_from_blueprint(blueprint: dict[str, Any]) -> dict[str, Any]:
    identity = blueprint["identity"]
    track = blueprint["track"]
    plan = create_talent_plan(
        name=identity["name"],
        gender=identity["gender"],
        specialty=track["specialty"],
        graduate_domains=track["domains"],
        university_major=f"{track['name']} 기초전공",
    )
    records = build_career_records(plan)
    contract = create_employment_contract(plan, role=track["target_role"])
    return {
        **plan,
        "career_records": records,
        "employment_contract": contract,
        "employment_ready": contract["employment_ready"],
        "source_blueprint": {
            "schema": blueprint["schema"],
            "request": blueprint["request"],
            "track_id": track["track_id"],
        },
    }


def materialize_training_blueprint(
    blueprint: dict[str, Any],
    *,
    output_dir: Path,
) -> dict[str, Any]:
    if blueprint.get("schema") != "ai-talent-training-blueprint/v1":
        raise ValueError("Unsupported training blueprint schema")

    output_dir.mkdir(parents=True, exist_ok=True)
    name_slug = _slug(blueprint["identity"]["name"])
    artifacts = {
        "training_blueprint": output_dir / f"{name_slug}_training_blueprint.json",
        "talent_plan": output_dir / f"{name_slug}_agent_plan.json",
        "institutional_review": output_dir / f"{name_slug}_institutional_review.json",
        "memory_profile": output_dir / f"{name_slug}_memory_profile.json",
        "learning_ledger": output_dir / f"{name_slug}_learning_ledger.json",
        "agent_manifest": output_dir / f"{name_slug}_agent_manifest.json",
        "release_bundle": output_dir / f"{name_slug}_agent_release_bundle",
        "release_archive": output_dir / f"{name_slug}_agent_release_bundle.zip",
        "installed_agent_root": output_dir / "installed_agents",
        "training_run": output_dir / "training_run.json",
    }

    _write_json(artifacts["training_blueprint"], blueprint)

    packet = _hiring_packet_from_blueprint(blueprint)
    _write_json(artifacts["talent_plan"], packet)

    institutional_review = run_institutional_review(packet, submissions=_submissions_for(blueprint))
    _write_json(artifacts["institutional_review"], institutional_review)

    memory_store = create_memory_store(owner=packet["talent"]["name"])
    memory_store = remember_event(memory_store, source="institutional_review", event=institutional_review)
    memory_profile = consolidate_memory(memory_store)
    _write_json(artifacts["memory_profile"], memory_profile)

    learning_ledger = create_learning_ledger(owner=packet["talent"]["name"])
    learning_ledger = record_learning_experience(
        learning_ledger,
        source="institutional_review",
        event=institutional_review,
        quality_label={"score": 95, "reviewed_by": "감독위원회", "status": "verified"},
    )
    learning_ledger["reasoning_kernel"] = build_reasoning_kernel(learning_ledger)
    _write_json(artifacts["learning_ledger"], learning_ledger)

    agent_manifest = build_agent_manifest(packet, memory_profile)
    _write_json(artifacts["agent_manifest"], agent_manifest)

    create_agent_release_bundle(
        output_dir=artifacts["release_bundle"],
        agent_manifest_path=artifacts["agent_manifest"],
        learning_ledger_path=artifacts["learning_ledger"],
    )
    package = package_agent_release_bundle(
        artifacts["release_bundle"],
        output_zip=artifacts["release_archive"],
    )
    package_manifest = json.loads(package["package_manifest"].read_text(encoding="utf-8"))
    install = install_agent_release_package(
        package["archive"],
        install_root=artifacts["installed_agent_root"],
        expected_sha256=package_manifest["sha256"],
    )
    hiring = hire_installed_agent(
        install["installed_manifest"],
        employer=blueprint["owner"],
        role=blueprint["track"]["target_role"],
    )

    artifacts["release_checksum"] = package["checksum"]
    artifacts["release_package_manifest"] = package["package_manifest"]
    artifacts["installed_agent_manifest"] = install["installed_manifest"]
    artifacts["employment_record"] = hiring["employment_record"]
    artifacts["employment_registry"] = hiring["registry_index"]

    run = {
        "schema": TRAINING_RUN_SCHEMA,
        "created_at_utc": datetime.now(timezone.utc).isoformat(),
        "owner": blueprint["owner"],
        "status": "employment_ready",
        "identity": blueprint["identity"],
        "track": blueprint["track"],
        "pipeline_stage_count": len(blueprint["training_pipeline"]),
        "artifact_count": len(artifacts),
        "artifacts": {key: str(path) for key, path in artifacts.items()},
        "verification": {
            "institutional_review_status": institutional_review["oversight_committee_decision"]["status"],
            "employment_ready": packet["employment_ready"],
            "release_package_created": package["archive"].exists(),
            "installed_agent_manifest_created": install["installed_manifest"].exists(),
            "employment_record_created": hiring["employment_record"].exists(),
        },
    }
    _write_json(artifacts["training_run"], run)
    return run
