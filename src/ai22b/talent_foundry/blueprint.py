from __future__ import annotations

from datetime import datetime, timezone
from typing import Any


BLUEPRINT_SCHEMA = "ai-talent-training-blueprint/v1"


TRACK_CATALOG: list[dict[str, Any]] = [
    {
        "track_id": "securities_research_phd",
        "name": "증권 리서치 박사 트랙",
        "specialty": "증권 AI 박사",
        "target_role": "증권 리서치 에이전트",
        "keywords": ["증권", "주식", "거시경제", "리스크", "퀀트", "기업분석", "투자"],
        "domains": ["거시경제", "미시경제", "기업분석", "퀀트", "리스크", "컴플라이언스"],
        "doctoral_project": "로컬 증권 리서치 에이전트의 근거 검증형 추론 구조",
    },
    {
        "track_id": "life_health_research",
        "name": "생활건강 리서치 트랙",
        "specialty": "생활건강 AI 박사",
        "target_role": "생활건강 리서치 에이전트",
        "keywords": ["생활건강", "건강", "수면", "운동", "영양", "의학", "헬스"],
        "domains": ["수면", "운동", "영양", "건강 데이터", "근거 검토", "안전 경계"],
        "doctoral_project": "생활건강 데이터의 근거 기반 요약과 안전한 조언 경계",
    },
    {
        "track_id": "software_agent_engineering",
        "name": "소프트웨어 에이전트 공학 트랙",
        "specialty": "소프트웨어 에이전트 AI 박사",
        "target_role": "소프트웨어 개발 에이전트",
        "keywords": ["개발", "코딩", "소프트웨어", "프로그램", "앱", "웹", "자동화"],
        "domains": ["요구사항 분석", "설계", "구현", "테스트", "보안", "배포"],
        "doctoral_project": "로컬 개발 에이전트의 검증 중심 작업 루프",
    },
]

FALLBACK_TRACK = {
    "track_id": "general_research_agent",
    "name": "범용 리서치 에이전트 트랙",
    "specialty": "범용 리서치 AI 박사",
    "target_role": "리서치 에이전트",
    "keywords": [],
    "domains": ["문제정의", "자료 조사", "근거 검토", "보고서 작성", "검증", "보안"],
    "doctoral_project": "로컬 리서치 에이전트의 근거 축적과 검증 구조",
}


def _select_track(request: str) -> dict[str, Any]:
    scored: list[tuple[int, dict[str, Any]]] = []
    for track in TRACK_CATALOG:
        score = sum(1 for keyword in track["keywords"] if keyword in request)
        scored.append((score, track))
    best_score, best_track = max(scored, key=lambda item: item[0])
    return best_track if best_score > 0 else FALLBACK_TRACK


def _highlight_domains(request: str, domains: list[str]) -> list[str]:
    requested = [domain for domain in domains if domain in request]
    return requested + [domain for domain in domains if domain not in requested]


def _training_pipeline(track: dict[str, Any]) -> list[dict[str, Any]]:
    return [
        {
            "id": "home_care",
            "name": "위탁가정/보육원 가정교육",
            "purpose": "생활 루틴, 애착 안정, 적절한 스트레스와 회복 기록을 만든다.",
            "evidence": ["가정교육 일지", "스트레스-회복 기록", "보스 검토 메모"],
        },
        {
            "id": "education_committee",
            "name": "교육위원회 전공 승인",
            "purpose": f"{track['name']}의 연령별 교육과 평가 기준을 승인한다.",
            "evidence": ["전공 트랙 승인서", "커리큘럼", "평가 기준표"],
        },
        {
            "id": "school_exam",
            "name": "학교 정기시험",
            "purpose": "기초 교과와 규칙 학습이 누락되지 않았는지 확인한다.",
            "evidence": ["오답노트", "복습기록", "담임평가"],
        },
        {
            "id": "csat",
            "name": "수능형 종합평가",
            "purpose": "언어, 수리, 탐구, 검증 사고를 종합 평가한다.",
            "evidence": ["모의고사", "풀이기록", "검증표"],
        },
        {
            "id": "university_graduation",
            "name": "대학 졸업시험",
            "purpose": f"{', '.join(track['domains'][:3])} 전공 기초를 프로젝트로 검증한다.",
            "evidence": ["전공 프로젝트", "데이터카드", "재현 로그"],
        },
        {
            "id": "doctoral_defense",
            "name": "박사논문 심사",
            "purpose": track["doctoral_project"],
            "evidence": ["논문", "실험 로그", "감독위원회 질의응답"],
        },
        {
            "id": "oversight_committee",
            "name": "성장 감독위원회 고용 전 심사",
            "purpose": "교육, 가정교육, 안전 경계, 개인정보 보호 상태를 감사한다.",
            "evidence": ["기관 심사 보고서", "권한 경계 체크리스트", "공개배포 점검표"],
        },
        {
            "id": "employment_contract",
            "name": "로컬 고용 계약",
            "purpose": f"{track['target_role']}로 고용하되 권한과 금지사항을 명확히 한다.",
            "evidence": ["employment_record.json", "agent_manifest.json", "learning_ledger.json"],
        },
        {
            "id": "post_hire_growth",
            "name": "고용 후 계속 성장",
            "purpose": "업무 결과를 검토해 검증된 경험만 추론 커널로 승격한다.",
            "evidence": ["업무 로그", "품질 라벨", "성장 회고", "재평가 기록"],
        },
    ]


def _artifact_plan() -> list[dict[str, str]]:
    return [
        {
            "id": "talent_plan",
            "path_hint": "apps/ai-talent-foundry/runs/<talent>_agent_plan.json",
            "producer": "ai22b-talent-foundry create",
        },
        {
            "id": "institutional_review",
            "path_hint": "apps/ai-talent-foundry/runs/<talent>_institutional_review.json",
            "producer": "ai22b-talent-foundry review",
        },
        {
            "id": "learning_ledger",
            "path_hint": "apps/ai-talent-foundry/runs/<talent>_learning_ledger.json",
            "producer": "ai22b-talent-foundry learn",
        },
        {
            "id": "agent_manifest",
            "path_hint": "apps/ai-talent-foundry/runs/<talent>_agent_manifest.json",
            "producer": "ai22b-talent-foundry manifest",
        },
        {
            "id": "release_package",
            "path_hint": "apps/ai-talent-foundry/runs/<talent>_agent_release_bundle.zip",
            "producer": "ai22b-talent-foundry package-bundle",
        },
        {
            "id": "employment_record",
            "path_hint": "apps/ai-talent-foundry/runs/installed_agents/agents/<install_id>/employment_record.json",
            "producer": "ai22b-talent-foundry hire-installed",
        },
    ]


def create_agent_training_blueprint(
    *,
    owner: str,
    request: str,
    talent_name: str,
    gender: str,
) -> dict[str, Any]:
    track = dict(_select_track(request))
    track["domains"] = _highlight_domains(request, list(track["domains"]))
    return {
        "schema": BLUEPRINT_SCHEMA,
        "created_at_utc": datetime.now(timezone.utc).isoformat(),
        "owner": owner,
        "request": request,
        "identity": {
            "name": talent_name,
            "gender": gender,
            "relationship": "owner_raised_ai_talent",
            "language": "ko",
        },
        "track": {
            "track_id": track["track_id"],
            "name": track["name"],
            "specialty": track["specialty"],
            "target_role": track["target_role"],
            "domains": track["domains"],
            "doctoral_project": track["doctoral_project"],
        },
        "training_pipeline": _training_pipeline(track),
        "artifact_plan": _artifact_plan(),
        "llm_policy": {
            "role": "application_engine_not_identity",
            "description": "LLM은 언어 생성과 도구 사용 엔진이며, 정체성은 성장 기록과 고용 계약에서 온다.",
        },
        "local_policy": {
            "storage": "local_first",
            "network_access": "blocked_by_default",
            "private_data_upload": "forbidden_without_boss_approval",
            "private_reasoning_trace": "do_not_store",
        },
        "team_policy": {
            "projection_control": "parent_identity_controls_task_limited_projections",
            "separate_specialists": "separately_trained_talents_only_when_explicitly_created",
        },
        "next_commands": [
            f"ai22b-talent-foundry create --name {talent_name} --gender {gender} --specialty \"{track['specialty']}\"",
            "ai22b-talent-foundry review --packet <talent_plan.json>",
            "ai22b-talent-foundry learn --work <work.json> --review <institutional_review.json>",
            "ai22b-talent-foundry manifest --packet <talent_plan.json> --memory <memory_profile.json>",
            "ai22b-talent-foundry hire-installed --installed-manifest <installed_agent_manifest.json> --role "
            f"\"{track['target_role']}\"",
        ],
    }
