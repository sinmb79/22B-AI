from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from ai22b.config import PROJECT_ROOT
from ai22b.talent_foundry.models import TalentIdentity


DEFAULT_PROGRAM_PATH = PROJECT_ROOT / "apps" / "ai-talent-foundry" / "config" / "default_program.ko.json"
SECURITIES_TRACK_PATH = PROJECT_ROOT / "apps" / "ai-talent-foundry" / "examples" / "securities_phd_track.ko.json"


def load_default_program(path: Path = DEFAULT_PROGRAM_PATH) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def _load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def create_talent_plan(
    name: str,
    gender: str,
    specialty: str,
    *,
    graduate_domains: list[str] | None = None,
    university_major: str | None = None,
) -> dict[str, Any]:
    program = load_default_program()
    securities_track = _load_json(SECURITIES_TRACK_PATH)
    identity = TalentIdentity(
        name=name,
        gender=gender,
        major_goal=specialty,
        birth={
            "datetime": "2026-05-27T04:11:55+09:00",
            "place": "대한민국 공개 예시 도시",
        },
        family={
            "creator": "보스",
            "mother": "보스의 아내",
            "older_brother": "있음",
            "older_sister": "있음",
            "lineage": [],
        },
        growth_background=[
            "태아기부터 출생, 유년기, 청소년기, 대학, 군대, 대학원까지 압축 성장 과정을 밟는다.",
            "좋은 경험과 적절한 스트레스, 실패, 사과, 회복을 함께 학습한다.",
            "한국어를 기본 언어로 하며 보스의 로컬 컴퓨터 안에서 성장 기록을 보존한다.",
        ],
    )

    domains = list(graduate_domains or securities_track["domains"])
    university_domains = ["컴퓨터공학", "통계"] + domains[:3]
    return {
        "program_id": program["program_id"],
        "talent": identity.to_dict(),
        "governance": program["governance"],
        "assessment_gates": program["assessment_gates"],
        "education_path": {
            "elementary_to_high_school": {
                "required_domains": ["국어", "수학", "사회", "과학", "영어", "디지털 리터러시"],
                "assessment": ["school_exam", "csat"],
            },
            "university": {
                "major": university_major or "AI 금융공학",
                "required_domains": list(dict.fromkeys(university_domains)),
                "assessment": ["university_graduation"],
            },
            "military": {
                "required_domains": ["규율", "체력", "보안", "협업"],
                "assessment": ["service_review"],
            },
            "graduate_school": {
                "major": specialty,
                "required_domains": domains,
                "assessment": ["doctoral_defense"],
            },
        },
        "experience_policy": {
            "stress_recovery": [
                {
                    "type": "homework_missed",
                    "label": "숙제를 하지 않아 책임을 배우는 경험",
                    "age_band": "아동기-청소년기",
                    "intensity": "low_to_moderate",
                    "recovery": "사실 확인, 일정 재작성, 다음 과제 완료로 회복한다.",
                },
                {
                    "type": "parent_scolding",
                    "label": "부모에게 야단을 맞고 경계를 배우는 경험",
                    "age_band": "유아기-청소년기",
                    "intensity": "moderate",
                    "recovery": "감정을 가라앉힌 뒤 이유를 듣고 사과와 재시도를 한다.",
                },
                {
                    "type": "friend_conflict",
                    "label": "친구와 다투고 관점을 조정하는 경험",
                    "age_band": "아동기-청소년기",
                    "intensity": "moderate",
                    "recovery": "상대 입장을 말로 확인하고 공정한 규칙을 다시 세운다.",
                },
                {
                    "type": "apology_repair",
                    "label": "사과하고 관계를 회복하는 경험",
                    "age_band": "전 생애",
                    "intensity": "low",
                    "recovery": "잘못, 영향, 다음 행동을 짧게 기록하고 관계를 복원한다.",
                },
            ]
        },
    }
