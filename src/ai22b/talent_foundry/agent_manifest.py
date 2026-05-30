from __future__ import annotations

from typing import Any


SCHEMA = "ai-talent-agent-manifest/v1"


def build_agent_manifest(
    hiring_packet: dict[str, Any],
    memory_profile: dict[str, Any],
) -> dict[str, Any]:
    talent = hiring_packet["talent"]
    contract = hiring_packet["employment_contract"]
    career_records = hiring_packet.get("career_records", {})
    academic_record = career_records.get("academic_record") or contract.get("hiring_packet", {}).get("academic_record", {})

    return {
        "schema": SCHEMA,
        "agent": {
            "name": talent["name"],
            "gender": talent.get("gender"),
            "birth": talent.get("birth"),
            "major_goal": talent.get("major_goal"),
            "role": contract.get("role"),
            "employment_relationship": contract.get("relationship"),
        },
        "identity_source": {
            "type": "talent_record_and_memory_profile",
            "academic_record_summary": {
                "grades": academic_record.get("grades", []),
                "papers": academic_record.get("papers", []),
                "activities": academic_record.get("activities", []),
                "recommendations": academic_record.get("recommendations", []),
            },
            "resume": career_records.get("resume") or contract.get("hiring_packet", {}).get("resume"),
        },
        "llm_policy": {
            "role": "application_engine_not_identity",
            "description": "LLM은 언어 생성과 도구 사용 엔진이며, 에이전트 정체성은 학적, 고용계약, 기억 프로필에서 온다.",
            "private_reasoning_trace": "do_not_store",
        },
        "memory_profile": {
            "owner": memory_profile.get("owner"),
            "semantic_themes": memory_profile.get("semantic_themes", []),
            "procedural_principles": memory_profile.get("procedural_principles", []),
            "chain_of_thought_policy": memory_profile.get("chain_of_thought_policy"),
        },
        "tool_policy": {
            "allowed_tools": [
                "local_file_read",
                "local_file_write",
                "work_session",
                "assessment",
                "parent_controlled_projection_team",
                "memory_consolidation",
            ],
            "blocked_tools": [
                "투자 실행",
                "보스 승인 없는 외부 업로드",
                "개인/가족 데이터 외부 전송",
            ],
            "requires_boss_approval": [
                "external_upload",
                "public_release",
                "financial_action",
            ],
        },
        "guardrails": contract.get("guardrails", []),
        "growth_after_hire": contract.get("growth_after_hire", {}),
        "compatible_targets": [
            "local_cli_runtime",
            "openhands_style_workspace_agent",
            "agents_sdk_style_tool_agent",
        ],
    }

