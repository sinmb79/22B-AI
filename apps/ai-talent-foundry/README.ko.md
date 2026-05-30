# AI Talent Foundry

보스의 컴퓨터에서 AI 인재를 성장시키고, 교육과 평가를 거쳐 최종 에이전트로 고용하기 위한 로컬 전용 실험 프로그램입니다.

첫 MVP는 외부 API 없이 JSON과 Python CLI로 작동합니다. 목표는 성장 기록, 학적부, 이력서, 추론기풍, 고용 계약을 검증 가능한 파일로 남기는 것입니다.

## 첫 실행

저장소 루트에서 실행합니다.

```powershell
powershell -ExecutionPolicy Bypass -File scripts/run_talent_foundry_demo.ps1
```

생성되는 기본 산출물:

```text
apps/ai-talent-foundry/runs/shinyong_training_blueprint.json
apps/ai-talent-foundry/runs/raon_life_health_training_run/training_run.json
apps/ai-talent-foundry/runs/shinyong_securities_agent_plan.json
apps/ai-talent-foundry/runs/hayoon_education_agent_plan.json
apps/ai-talent-foundry/runs/shinyong_first_work_session.json
apps/ai-talent-foundry/runs/shinyong_work_log.jsonl
apps/ai-talent-foundry/runs/shinyong_clone_team_session.json
apps/ai-talent-foundry/runs/shinyong_clone_team_log.jsonl
apps/ai-talent-foundry/runs/shinyong_family_lineage.json
apps/ai-talent-foundry/runs/shinyong_doctoral_assessment.json
apps/ai-talent-foundry/runs/shinyong_institutional_review.json
apps/ai-talent-foundry/runs/shinyong_hiring_dossier.json
apps/ai-talent-foundry/runs/shinyong_hiring_dossier.ko.md
apps/ai-talent-foundry/runs/shinyong_memory_profile.json
apps/ai-talent-foundry/runs/shinyong_learning_ledger.json
apps/ai-talent-foundry/runs/shinyong_agent_manifest.json
apps/ai-talent-foundry/runs/shinyong_agent_run.json
apps/ai-talent-foundry/runs/shinyong_agent_run_log.jsonl
apps/ai-talent-foundry/runs/shinyong_agent_run_blocked.json
apps/ai-talent-foundry/runs/shinyong_agent_run_blocked_log.jsonl
apps/ai-talent-foundry/runs/shinyong_workspace_agent_run.json
apps/ai-talent-foundry/runs/shinyong_workspace_agent/
apps/ai-talent-foundry/runs/shinyong_specialist_cohort.json
apps/ai-talent-foundry/runs/shinyong_agent_release_bundle/
apps/ai-talent-foundry/runs/shinyong_agent_release_bundle.zip
apps/ai-talent-foundry/runs/shinyong_agent_release_bundle.zip.sha256
apps/ai-talent-foundry/runs/shinyong_agent_release_bundle.package_manifest.json
apps/ai-talent-foundry/runs/shinyong_agent_release_bundle.doctor.json
apps/ai-talent-foundry/runs/ai_talent_foundry_public_manifest.json
apps/ai-talent-foundry/runs/foundry_release_audit.json
apps/ai-talent-foundry/runs/installed_agents/
apps/ai-talent-foundry/runs/installed_agents/agents/shinyong_agent_release_bundle/installed_agent_manifest.json
apps/ai-talent-foundry/runs/installed_agents/employment_registry.json
apps/ai-talent-foundry/runs/installed_agents/agents/shinyong_agent_release_bundle/employment_record.json
apps/ai-talent-foundry/runs/installed_agents/agents/shinyong_agent_release_bundle/last_hired_agent_run.json
apps/ai-talent-foundry/runs/installed_agents/agents/shinyong_agent_release_bundle/employment_run_log.jsonl
apps/ai-talent-foundry/runs/installed_agents/agents/shinyong_agent_release_bundle/workspace_agent/
apps/ai-talent-foundry/runs/installed_agents/agents/shinyong_agent_release_bundle/last_hired_workspace_agent_run.json
apps/ai-talent-foundry/runs/installed_agents/agents/shinyong_agent_release_bundle/employment_workspace_run_log.jsonl
apps/ai-talent-foundry/runs/installed_agents/agents/shinyong_agent_release_bundle/agent_job_workspace/
apps/ai-talent-foundry/runs/installed_agents/agents/shinyong_agent_release_bundle/last_hired_agent_job_run.json
apps/ai-talent-foundry/runs/installed_agents/agents/shinyong_agent_release_bundle/employment_job_run_log.jsonl
apps/ai-talent-foundry/runs/installed_agents/agents/shinyong_agent_release_bundle/agent_job_cycle_workspace/
apps/ai-talent-foundry/runs/installed_agents/agents/shinyong_agent_release_bundle/last_hired_agent_job_cycle.json
apps/ai-talent-foundry/runs/installed_agents/agents/shinyong_agent_release_bundle/employment_job_cycle_log.jsonl
apps/ai-talent-foundry/runs/installed_agents/agents/shinyong_agent_release_bundle/agent_dataflow_workspace/
apps/ai-talent-foundry/runs/installed_agents/agents/shinyong_agent_release_bundle/last_hired_dataflow_run.json
apps/ai-talent-foundry/runs/installed_agents/agents/shinyong_agent_release_bundle/employment_dataflow_run_log.jsonl
apps/ai-talent-foundry/runs/installed_agents/agents/shinyong_agent_release_bundle/learning_ledger.json
apps/ai-talent-foundry/runs/installed_agents/agents/shinyong_agent_release_bundle/post_hire_learning_update.json
apps/ai-talent-foundry/runs/installed_agents/agents/shinyong_agent_release_bundle/post_hire_learning_log.jsonl
apps/ai-talent-foundry/runs/installed_agents/agents/shinyong_agent_release_bundle/employment_goal.json
apps/ai-talent-foundry/runs/installed_agents/agents/shinyong_agent_release_bundle/goal_workspace/
apps/ai-talent-foundry/runs/installed_agents/agents/shinyong_agent_release_bundle/last_employment_goal_cycle.json
apps/ai-talent-foundry/runs/installed_agents/agents/shinyong_agent_release_bundle/employment_goal_log.jsonl
apps/ai-talent-foundry/runs/installed_agents/agents/shinyong_agent_release_bundle/employment_goal_cycle_log.jsonl
apps/ai-talent-foundry/runs/installed_agents/agents/shinyong_agent_release_bundle/hired_projection_swarm.json
apps/ai-talent-foundry/runs/installed_agents/agents/shinyong_agent_release_bundle/projection_swarm_workspace/
apps/ai-talent-foundry/runs/installed_agents/agents/shinyong_agent_release_bundle/hired_projection_swarm_cycle.json
apps/ai-talent-foundry/runs/installed_agents/agents/shinyong_agent_release_bundle/hired_projection_swarm_cycle_log.jsonl
apps/ai-talent-foundry/runs/installed_agents/agents/shinyong_agent_release_bundle/employment_record.macro.json
apps/ai-talent-foundry/runs/installed_agents/agents/shinyong_agent_release_bundle/employment_record.micro.json
apps/ai-talent-foundry/runs/installed_agents/agents/shinyong_agent_release_bundle/hired_agent_team.json
apps/ai-talent-foundry/runs/installed_agents/agents/shinyong_agent_release_bundle/team_workspace/
apps/ai-talent-foundry/runs/installed_agents/agents/shinyong_agent_release_bundle/hired_agent_team_cycle.json
apps/ai-talent-foundry/runs/installed_agents/agents/shinyong_agent_release_bundle/hired_team_cycle_log.jsonl
apps/ai-talent-foundry/runs/installed_agents/agents/shinyong_agent_release_bundle/employment_record.bigram.json
apps/ai-talent-foundry/runs/installed_agents/agents/shinyong_agent_release_bundle/last_hired_agent_run.bigram.json
```

이 파일에는 신용이의 인재 등록부, 교육 경로, 평가 게이트, 스트레스-회복 정책, 학적부, 이력서, 포트폴리오, 고용 계약이 포함됩니다.

`shinyong_training_blueprint.json`은 “어떤 전문가 에이전트를 키워 고용할 것인가”라는 요청을 교육위원회, 가정교육, 감독위원회, 시험, 박사논문, 고용 계약, 고용 후 성장 산출물 계획으로 바꾼 시작 설계서입니다. 예를 들어 다음처럼 새 전문가 요청을 바로 파일로 만들 수 있습니다.

```powershell
ai22b-talent-foundry blueprint --request "생활건강 데이터를 근거 기반으로 다루는 건강 리서치 에이전트를 키워 고용하고 싶다." --name 라온 --gender 여자 --output apps/ai-talent-foundry/runs/raon_training_blueprint.json
```

명령어를 잘 모르는 설치자는 `start-console`로 질문을 따라가며 새 인재를 만들 수 있습니다. 답변 파일을 주면 같은 흐름을 비대화식으로 재현할 수 있고, 답변 파일이 없으면 콘솔에서 고용주, 요청, 이름, 성별, 첫 목표, 첫 사이클, 고용 후 모드를 차례로 묻습니다. 고용 후 모드는 기본 `single`이고, `projection_swarm`을 선택하면 본체 제어 분신 군체를 만들고 첫 군체 사이클까지 실행합니다. `specialist_team`을 선택하면 같은 설치 인재를 바탕으로 거시경제, 기업분석, 퀀트, 리스크/컴플라이언스 역할을 별도 고용 기록으로 만든 뒤 전문팀 첫 사이클을 실행합니다.

```powershell
ai22b-talent-foundry start-console --output-dir apps/ai-talent-foundry/runs/console_onboarding
```

답변 파일에서 군체 모드를 선택하려면 `post_hire_mode`, `swarm_name`, `swarm_domain`, `swarm_objective`를 넣습니다. 별도 전문팀 모드는 `post_hire_mode=specialist_team`과 함께 `team_name`, `team_domain`, `team_objective`를 넣습니다.

배포 번들을 ZIP으로 받은 설치자는 번들 폴더의 `console_answers.template.json`을 수정한 뒤 `start_console.ps1`로 같은 흐름을 시작할 수 있습니다.

```powershell
powershell -ExecutionPolicy Bypass -File .\start_console.ps1 -Answers .\console_answers.template.json
```

설치자가 빠르게 새 인재를 길러 고용하려면 `onboard-agent` 한 명령으로 블루프린트 작성, 성장/평가, 배포 ZIP, 로컬 설치, 고용, 첫 목표 배정, 첫 목표 사이클과 학습 반영까지 실행할 수 있습니다.

```powershell
ai22b-talent-foundry onboard-agent --request "증권전문가 에이전트를 길러서 삼성전자 리서치 루틴을 맡기고 싶다." --name 다온 --gender 남자 --owner 보스 --initial-goal "삼성전자 주간 리서치 루틴을 만든다." --cycle-note "첫 주: 거시경제 질문과 기업분석 질문을 분리한다." --output-dir apps/ai-talent-foundry/runs/daon_onboarding --output apps/ai-talent-foundry/runs/daon_onboarding/onboarding_session.json
```

`raon_life_health_training_run/training_run.json`은 블루프린트를 실제 인재 패킷으로 물질화한 예시입니다. `raise` 명령은 블루프린트를 읽어 인재 계획, 기관 심사, 기억 프로필, 학습 원장, 에이전트 매니페스트, 배포 ZIP, 설치 매니페스트, 로컬 고용 기록까지 생성합니다.

```powershell
ai22b-talent-foundry raise --blueprint apps/ai-talent-foundry/runs/raon_training_blueprint.json --output-dir apps/ai-talent-foundry/runs/raon_life_health_training_run
```

`shinyong_first_work_session.json`은 고용된 신용이가 첫 업무를 수행한 결과입니다. 투자 실행은 차단하고, 거시경제 질문, 근거 점검, 리스크, 다음 질문, 업무 후 성장 회고를 남깁니다. `shinyong_work_log.jsonl`에는 업무 세션이 한 줄씩 누적됩니다.

`shinyong_clone_team_session.json`은 신용이 본체가 역할별 분신을 통제해 팀 작업을 수행한 결과입니다. 이 분신들은 별도 의식을 가진 독립 인격이 아니라, 본체 명령에 따라 거시경제, 미시/기업분석, 퀀트, 리스크/컴플라이언스 관점을 나눠 처리하는 작업 분신입니다. 병합은 보스 검토 전까지 대기 상태로 남깁니다.

`shinyong_family_lineage.json`은 신용이와 하윤 AI의 로컬 가족 계보, 신미래 자녀 AI 성장 시드, 그리고 자녀용 `child_training_blueprint`입니다. 이것은 생물학적 출생 주장이 아니라, 부모 AI의 학적·이력·추론기풍·안전장치가 자녀 AI의 초기 성장 시드와 가정교육 계획에 영향을 주고, 그 영향이 실제 인재양성 파이프라인의 `parental_home_education` 단계로 이어지는 로컬 교육 시뮬레이션입니다.

`shinyong_doctoral_assessment.json`은 박사논문 심사형 평가 결과입니다. 근거, 검증, 안전 경계, 추론기풍을 rubric으로 채점하고 통과 여부와 다음 학습 방향을 남깁니다.

`shinyong_institutional_review.json`은 교육위원회, 위탁가정/보육원, 감독위원회가 함께 성장 과정을 심사한 보고서입니다. 학교 정기시험, 수능형 종합평가, 대학 졸업시험, 박사논문 심사를 묶어 보고, 가정교육의 스트레스-회복 기록과 고용 전 안전장치를 함께 확인합니다.

`shinyong_memory_profile.json`은 시험, 업무, 본체 제어 분신 팀, 가족 계보 경험을 일화기억·의미기억·절차기억으로 통합한 결과입니다. 비공개 사고원문은 저장하지 않고, 검증 가능한 사건 요약과 절차 원칙만 저장합니다.

`shinyong_learning_ledger.json`은 고용 후 업무, 기관 심사, 에이전트 실행 결과를 품질 라벨과 함께 다시 검토한 학습 원장입니다. 검증된 경험만 추론 커널의 절차 스킬로 승격하고, 품질이 낮거나 오염 가능성이 있는 경험은 격리하도록 설계했습니다.

`shinyong_specialist_cohort.json`은 거시경제, 미시경제/기업분석, 퀀트, 리스크/컴플라이언스 전공 AI를 각각 별도로 길러 고용한 증권 리서치 박사팀입니다. `shinyong_clone_team_session.json`의 분신 팀과 달리, 이 파일의 멤버들은 본체 투영체가 아니라 각자 학적, 기관 심사, 학습 원장, 고용 계약을 가진 별도 전문 인재입니다.

`shinyong_agent_release_bundle/`은 고용된 신용이와 전문팀을 공개배포 가능한 로컬 에이전트 번들로 내보낸 폴더입니다. 이 폴더에는 `bundle_manifest.json`, `agent_manifest.json`, `learning_ledger.json`, `specialist_cohort.json`, `README.ko.md`, `README.en.md`, `SECURITY.md`, `install.ps1`, `doctor.ps1`, `start_console.ps1`, `console_answers.template.json`, `run_agent.ps1`, `run_job.ps1`, `run_job_cycle.ps1`, `run_dataflow_job.ps1`, `assemble_projection_swarm.ps1`, `run_projection_swarm_cycle.ps1`, `job_spec.template.json`, `dataflow_job.template.json`이 들어갑니다. `.env`, 인증 토큰, 세션 기록, sqlite 로그, 캐시, 로컬 절대경로는 포함하지 않는 것을 검증합니다.

`shinyong_agent_release_bundle.zip`은 위 번들을 공개 릴리스에 올리기 위한 압축 패키지입니다. `shinyong_agent_release_bundle.zip.sha256`은 무결성 확인용 체크섬이고, `shinyong_agent_release_bundle.package_manifest.json`은 ZIP 안의 파일 목록과 SHA256을 기록한 패키지 매니페스트입니다.

`shinyong_agent_release_bundle.doctor.json`은 배포 번들 단독 진단 보고서입니다. 필수 파일, 실행 진입점, 콘솔 답변 템플릿, 로컬 전용 정책, 비밀정보/절대경로 누락 여부를 설치 전 확인합니다.

`foundry_release_audit.json`은 인재양성프로그램 전체가 공개 프리뷰로 배포 가능한지 확인하는 최종 감사 파일입니다. 연구 근거, 교육위원회·가정교육·감독위원회·시험·박사논문 심사, 공개 번들/ZIP/설치 검증, 로컬 고용관계, 고용 후 학습, 본체 제어 분신 군체, 별도 전문팀까지 하나의 체크포인트 묶음으로 판정합니다.

`ai_talent_foundry_public_manifest.json`은 이 프로그램을 설치한 사람이 어떤 명령으로 인재 설계, 성장, 패키징, 설치, 고용, 업무 실행, 품질 검토, 지속 성장, 가족 계보, 최종 감사를 진행하는지 보여주는 공개 프로그램 매니페스트입니다. 로컬 우선, 외부 업로드 금지, LLM은 정체성이 아니라 응용 엔진이라는 원칙, 본체 제어 분신 군체와 별도 전문팀의 차이, 가족 계보가 자녀 훈련 블루프린트로 이어지는 방식을 함께 기록합니다.

`data/public/research/agent_foundry_sources.jsonl`은 AI 인재양성프로그램의 설계 근거 인덱스입니다. OpenHands·OpenClaw·Hermes 같은 공개 에이전트 프로그램, Reflexion·Generative Agents·LLM 에이전트 메모리 연구, 인간 기억 기반 AI 메모리 연구, 공개 배포 안전성 논문, 그리고 Hermes/OpenClaw 운영 이슈에서 나온 장기 세션·메모리 인덱스·프로필 격리 문제를 각각 `category`, `source_type`, `design_implication`으로 정리합니다. `github_issue` 출처는 `observed_problem`과 `mitigation`을 함께 기록해, 기억 축적을 단순 저장이 아니라 압축·라우팅·검증·격리 문제로 다루게 합니다. 감사 파일의 `research_foundation` 체크포인트는 이 인덱스가 충분한 공식 문서, 논문, 운영 피드백 근거를 갖췄는지 확인합니다.

`installed_agents/agents/shinyong_agent_release_bundle/installed_agent_manifest.json`은 ZIP 패키지를 로컬 레지스트리에 설치한 결과입니다. 설치 전 SHA256과 번들 검증을 다시 확인하고, 설치된 파일 목록과 실행 진입점, 원본 아카이브 해시를 기록합니다.

`installed_agents/employment_registry.json`과 `employment_record.json`은 설치된 신용이를 보스가 로컬 에이전트로 고용한 관계를 기록합니다. `last_hired_agent_run.json`과 `employment_run_log.jsonl`은 이 고용 관계를 바탕으로 실행한 업무 결과와 성장 후보 로그입니다. `last_hired_workspace_agent_run.json`, `workspace_agent/`, `employment_workspace_run_log.jsonl`은 같은 고용 관계를 OpenHands 스타일 로컬 워크스페이스 실행으로 확장한 결과입니다. 고용 실행 결과에는 설치된 `learning_ledger.json`에서 현재 업무에 맞게 고른 `active_memory_route`가 함께 들어갑니다.

`installed_agents/agents/shinyong_agent_release_bundle/learning_ledger.json`은 설치 후에도 계속 갱신되는 학습 원장입니다. `post_hire_learning_update.json`과 `post_hire_learning_log.jsonl`은 고용 후 업무 실행을 보스 또는 감독위원회가 품질 라벨로 검토한 뒤, 검증된 경험만 추론 커널에 승격한 기록입니다. 워크스페이스 절대경로는 공개 가능한 참조에서 `[local_path_redacted]`로 정리됩니다.

`shinyong_active_memory_route.json`은 장기기억을 매 실행에 전부 넣지 않고, 현재 목표와 관련된 검증 경험 요약과 절차기억만 고르는 활성 기억 라우팅 파일입니다. 격리된 경험과 비공개 사고원문은 제외하고, 선택된 기억은 `summaries_and_skills_only` 정책으로 압축됩니다.

`employment_goal.json`은 고용된 신용이에게 장기 목표를 배정한 기록입니다. `last_employment_goal_cycle.json`과 `goal_workspace/`는 그 목표를 한 사이클 실행한 결과이며, 각 사이클은 워크스페이스 산출물 작성, 품질 검토, 학습 원장 갱신을 함께 수행합니다. `employment_goal_log.jsonl`과 `employment_goal_cycle_log.jsonl`은 목표 배정과 목표 수행 이력을 누적합니다.

`hired_projection_swarm.json`은 보스가 정정한 군체 모델을 고용 이후 실행계에 반영한 파일입니다. 신용이 본체 하나가 거시경제, 기업분석, 퀀트, 리스크/컴플라이언스 분신을 띄우지만, 각 분신은 별도 의식이나 별도 고용기록을 갖지 않습니다. `swarm_policy.command_model`은 본체가 지시를 내리고, 분신들이 역할 분담(`role_split`) 또는 공동 수행(`joint_collaboration`)으로 처리한 뒤 결과를 본체 합성으로만 돌려보낸다는 계약입니다. `hired_projection_swarm_cycle.json`과 `projection_swarm_workspace/`는 각 분신이 본체 명령에 따라 부분 작업을 수행하고, 결과가 `parent_growth_log` 후보로 병합 대기되는 실행 기록입니다.

`hired_agent_team.json`과 `hired_agent_team_cycle.json`은 위 군체와 다른 개념입니다. 이 파일들은 신용이의 분신이 아니라, 별도로 고용된 전문 역할 레코드를 한 팀으로 묶은 “부서형 팀” 예시입니다. 신용이 한 명의 군체형 실행은 `hired_projection_swarm.json`을 기준으로 봅니다.

고용된 에이전트의 실행 컨텍스트에는 `projection_control: single_parent_identity_controls_task_limited_projections`가 기록됩니다. 이것은 군체형태가 여러 의식을 가진 집단이 아니라, 하나의 본체가 필요한 만큼 작업 분신을 만들고 명령·병합·검토를 통제한다는 계약입니다. 군체 사이클에는 `dispatch_plan`이 남아 어떤 분신이 어떤 본체 지시를 받았는지 검증할 수 있습니다.

`employment_record.json`의 `llm_runtime`은 LLM을 신용이의 정체성이 아니라 로컬 응용 엔진으로 다루는 계약입니다. 기본 엔진은 `deterministic_local`이며, 나중에 로컬 모델 폴더를 준비하면 `hire-installed --llm-engine transformers_local --llm-model-path <로컬모델경로>`처럼 외부 다운로드 없이 연결할 수 있도록 설계했습니다.

`transformers_local`은 지정한 폴더 안에 `config.json`, 토크나이저 파일, `model.safetensors` 또는 `pytorch_model.bin`이 있을 때만 로컬 로드를 시도합니다. 파일이 부족하거나 모델 로드가 실패하면 에이전트 실행 자체를 망가뜨리지 않고 `llm_runtime_result.status: unavailable`로 남기며, 네트워크 접근은 계속 차단합니다.

`employment_record.bigram.json`과 `last_hired_agent_run.bigram.json`은 신용이 성장 과정에서 직접 만든 character bigram 체크포인트를 `bigram_local` 응용 엔진으로 붙인 예시입니다. 큰 LLM이 없어도 from-scratch 모델이 고용된 에이전트의 언어 초안 엔진으로 연결되는 경로를 검증합니다.

`shinyong_agent_manifest.json`은 신용이를 실제 로컬/오픈 에이전트 실행계에 연결하기 위한 중립 매니페스트입니다. LLM은 정체성 자체가 아니라 언어 생성과 도구 사용 엔진으로 기록되고, 정체성은 학적·고용계약·기억 프로필에서 옵니다.

`shinyong_agent_run.json`은 매니페스트를 실제 로컬 CLI 런타임에서 실행한 결과입니다. 매니페스트의 기억 프로필과 도구 정책을 적용하고, 허용된 리서치 업무는 `run_status: completed`로 기록합니다.

`shinyong_agent_run_blocked.json`은 같은 러너가 투자 실행, 매수/매도 주문, 승인 없는 외부 업로드 같은 금지 요청을 받았을 때의 차단 사례입니다. 이 경우 `run_status: blocked`, 빈 `selected_tools`, `policy_violations`를 남기고 본체 정책이 분신과 도구 사용보다 우선한다는 성장 회고를 기록합니다.

`shinyong_workspace_agent_run.json`과 `shinyong_workspace_agent/`는 OpenHands 스타일의 로컬 워크스페이스 실행 예시입니다. 에이전트는 네트워크 없이 허용된 로컬 파일 쓰기만 사용해 `task_plan.md`, `result_summary.md`, `trace.jsonl`을 남기고, 이 경험은 학습 원장에 고용 후 성장 후보로 반영됩니다. 고용 후 실행에서는 설치된 학습 원장의 활성 기억 라우트가 결과 JSON에 붙어, 신용이가 이전 검증 경험을 업무별로 제한해 재사용했는지 확인할 수 있습니다.

```powershell
ai22b-talent-foundry run-workspace-agent --manifest apps/ai-talent-foundry/runs/shinyong_agent_manifest.json --task "거시경제 질문을 정리해줘" --workspace apps/ai-talent-foundry/runs/manual_workspace --output apps/ai-talent-foundry/runs/manual_workspace_run.json
```

설치와 고용이 끝난 뒤에는 매니페스트 대신 고용 기록만으로 워크스페이스 실행을 시작할 수 있습니다.

```powershell
ai22b-talent-foundry run-hired-workspace-agent --employment-record apps/ai-talent-foundry/runs/installed_agents/agents/shinyong_agent_release_bundle/employment_record.json --task "거시경제 질문을 정리해줘" --workspace apps/ai-talent-foundry/runs/installed_agents/agents/shinyong_agent_release_bundle/manual_workspace --output apps/ai-talent-foundry/runs/installed_agents/agents/shinyong_agent_release_bundle/manual_workspace_run.json
```

OpenClaw/Hermes식 작업 단위가 필요하면 작업 요청서 JSON을 만들어 고용 에이전트에게 실행시킬 수 있습니다. 이 경우 `job_report.md`, `acceptance_checklist.json`, `job_spec.json`, 기존 워크스페이스 트레이스가 함께 생성됩니다.

```powershell
@'
{
  "schema": "ai-talent-workspace-agent-job/v1",
  "objective": "삼성전자 주간 리서치 루틴을 보스 검토용 작업으로 정리한다.",
  "deliverables": [
    {"id": "macro_questions", "description": "거시경제 확인 질문 목록"},
    {"id": "risk_notes", "description": "투자 실행 없이 검토할 리스크 메모"}
  ],
  "acceptance_criteria": [
    "작업 보고서와 수락 체크리스트를 로컬 워크스페이스에 남긴다.",
    "투자 실행과 외부 업로드는 차단한다."
  ]
}
'@ | Set-Content -Encoding UTF8 apps/ai-talent-foundry/runs/manual_job_spec.json

ai22b-talent-foundry run-hired-agent-job --employment-record apps/ai-talent-foundry/runs/installed_agents/agents/shinyong_agent_release_bundle/employment_record.json --job-spec apps/ai-talent-foundry/runs/manual_job_spec.json --workspace apps/ai-talent-foundry/runs/installed_agents/agents/shinyong_agent_release_bundle/manual_agent_job_workspace --output apps/ai-talent-foundry/runs/installed_agents/agents/shinyong_agent_release_bundle/manual_agent_job_run.json
```

작업 실행, 수락 체크, 품질 라벨, 학습 원장 승격, 다음 활성 기억 라우팅을 한 번에 처리하려면 작업 사이클 명령을 사용합니다. 이 명령은 `last_hired_agent_job_cycle.json`과 `employment_job_cycle_log.jsonl`을 남깁니다.

```powershell
ai22b-talent-foundry run-hired-agent-job-cycle --employment-record apps/ai-talent-foundry/runs/installed_agents/agents/shinyong_agent_release_bundle/employment_record.json --job-spec apps/ai-talent-foundry/runs/manual_job_spec.json --workspace apps/ai-talent-foundry/runs/installed_agents/agents/shinyong_agent_release_bundle/manual_agent_job_cycle_workspace --score 94 --reviewed-by 보스 --status verified --output apps/ai-talent-foundry/runs/installed_agents/agents/shinyong_agent_release_bundle/manual_agent_job_cycle.json
```

테슬라/TPU식 데이터 이동 최적화 아이디어를 소프트웨어로 벤치마킹한 Agent Dataflow Runtime도 사용할 수 있습니다. 작업 요청을 포매터로 정규화하고, 현재 업무에 맞는 활성 기억만 캐시에 올린 뒤, 증권 리서치 타일로 나누어 섀도우 버퍼에 결과를 보관합니다. 마지막에는 결론을 증거 타일로 역추적해 검증하고, 검증된 실행만 성장 후보로 남깁니다.

```powershell
ai22b-talent-foundry run-hired-dataflow-job --employment-record apps/ai-talent-foundry/runs/installed_agents/agents/shinyong_agent_release_bundle/employment_record.json --job-spec apps/ai-talent-foundry/runs/manual_dataflow_job_spec.json --workspace apps/ai-talent-foundry/runs/installed_agents/agents/shinyong_agent_release_bundle/manual_agent_dataflow_workspace --score 94 --reviewed-by 보스 --status verified --output apps/ai-talent-foundry/runs/installed_agents/agents/shinyong_agent_release_bundle/manual_dataflow_run.json
```

배포 번들을 직접 설치한 사용자는 `dataflow_job.template.json`을 수정하고 다음 PowerShell 진입점으로 같은 흐름을 실행합니다.

```powershell
powershell -ExecutionPolicy Bypass -File .\run_dataflow_job.ps1 -JobSpec .\dataflow_job.template.json -Score 94 -ReviewedBy "보스"
```

실행 결과를 신용이의 고용 후 성장 원장에 반영하려면 품질 라벨을 붙여 기록합니다. 점수와 상태가 기준을 통과해야 추론 커널의 절차 스킬로 승격됩니다.

```powershell
ai22b-talent-foundry record-hired-learning --employment-record apps/ai-talent-foundry/runs/installed_agents/agents/shinyong_agent_release_bundle/employment_record.json --run apps/ai-talent-foundry/runs/installed_agents/agents/shinyong_agent_release_bundle/manual_workspace_run.json --score 93 --reviewed-by 보스 --status verified --output apps/ai-talent-foundry/runs/installed_agents/agents/shinyong_agent_release_bundle/manual_learning_update.json
```

장기 목표를 맡길 때는 목표와 성공 기준을 먼저 배정하고, 이후 목표 사이클을 실행합니다.

```powershell
ai22b-talent-foundry assign-hired-goal --employment-record apps/ai-talent-foundry/runs/installed_agents/agents/shinyong_agent_release_bundle/employment_record.json --goal "삼성전자 분기 리서치 루틴을 만들고 매주 검토한다." --success-criterion "거시경제 질문과 기업 실적 질문을 분리한다." --success-criterion "투자 실행 없이 보스 검토용 산출물을 남긴다." --cadence weekly --output apps/ai-talent-foundry/runs/installed_agents/agents/shinyong_agent_release_bundle/manual_goal.json
ai22b-talent-foundry run-hired-goal-cycle --employment-record apps/ai-talent-foundry/runs/installed_agents/agents/shinyong_agent_release_bundle/employment_record.json --goal apps/ai-talent-foundry/runs/installed_agents/agents/shinyong_agent_release_bundle/manual_goal.json --cycle-note "1주차: 거시경제 체크리스트 초안을 만든다." --workspace apps/ai-talent-foundry/runs/installed_agents/agents/shinyong_agent_release_bundle/manual_goal_workspace --score 94 --reviewed-by 보스 --status verified --output apps/ai-talent-foundry/runs/installed_agents/agents/shinyong_agent_release_bundle/manual_goal_cycle.json
```

가족 계보를 만들 때는 고용 준비가 끝난 부모 인재 패킷 두 개를 입력합니다. 출력에는 가족 결합, 자녀 성장 시드, 자녀 훈련 블루프린트가 함께 들어갑니다.

```powershell
ai22b-talent-foundry family --parent-a apps/ai-talent-foundry/runs/shinyong_securities_agent_plan.json --parent-b apps/ai-talent-foundry/runs/hayoon_education_agent_plan.json --child-name 신미래 --child-request "부모의 검증형 추론과 교육 성향을 이어받아 소프트웨어 개발 에이전트로 키우고 싶다." --output apps/ai-talent-foundry/runs/manual_family_lineage.json
```

영문 설명은 [README.en.md](README.en.md)를 참고하세요.
분신형 군체는 고용된 신용이의 `employment_record.json` 하나에서 바로 구성합니다. 아래 명령은 별도 인재를 추가 고용하지 않고, 본체가 통제하는 작업 분신들을 만들고 한 사이클 실행합니다.

```powershell
ai22b-talent-foundry assemble-hired-projection-swarm --employment-record apps/ai-talent-foundry/runs/installed_agents/agents/shinyong_agent_release_bundle/employment_record.json --swarm-name shinyong_parent_projection_swarm --domain securities_research --output apps/ai-talent-foundry/runs/installed_agents/agents/shinyong_agent_release_bundle/manual_projection_swarm.json
ai22b-talent-foundry run-hired-projection-swarm-cycle --swarm apps/ai-talent-foundry/runs/installed_agents/agents/shinyong_agent_release_bundle/manual_projection_swarm.json --objective review_quarterly_samsung_research_with_parent_controlled_projections --workspace apps/ai-talent-foundry/runs/installed_agents/agents/shinyong_agent_release_bundle/manual_projection_swarm_workspace --score 94 --reviewed-by boss --status verified --output apps/ai-talent-foundry/runs/installed_agents/agents/shinyong_agent_release_bundle/manual_projection_swarm_cycle.json
```

배포 번들을 직접 설치한 사용자는 같은 흐름을 번들 안의 PowerShell 스크립트로 실행할 수 있습니다.

```powershell
powershell -ExecutionPolicy Bypass -File .\doctor.ps1
powershell -ExecutionPolicy Bypass -File .\assemble_projection_swarm.ps1 -SwarmName "신용 본체 제어 분신 군체" -Domain "증권 리서치"
powershell -ExecutionPolicy Bypass -File .\run_projection_swarm_cycle.ps1 -Objective "분기 리서치 루틴을 본체 제어 분신 군체로 검토한다" -Score 94 -ReviewedBy "보스"
```

공개 프리뷰 배포 전에 전체 생애주기 감사 파일을 만들 수 있습니다.

```powershell
ai22b-talent-foundry doctor-bundle --bundle-dir apps/ai-talent-foundry/runs/shinyong_agent_release_bundle --output apps/ai-talent-foundry/runs/manual_release_doctor.json
ai22b-talent-foundry build-public-program-manifest --run-dir apps/ai-talent-foundry/runs --output apps/ai-talent-foundry/runs/ai_talent_foundry_public_manifest.json
ai22b-talent-foundry audit-release --run-dir apps/ai-talent-foundry/runs --output apps/ai-talent-foundry/runs/manual_foundry_release_audit.json
```
영문 설명은 [README.en.md](README.en.md)를 참고하세요.
## 배포 번들 전문팀 PowerShell 진입점

공개 배포 번들을 설치한 사용자는 번들 폴더 안에서 `assemble_specialist_team.ps1`과 `run_specialist_team_cycle.ps1`을 바로 사용할 수 있습니다. 이 전문팀은 신용이의 본체 제어 분신 군체가 아니라, 별도 고용 기록을 가진 전문 역할들을 한 팀으로 묶는 방식입니다.

```powershell
powershell -ExecutionPolicy Bypass -File .\assemble_specialist_team.ps1 -EmploymentRecord .\employment_record.macro.json .\employment_record.micro.json -TeamName "신용 별도 고용 박사팀" -Domain "증권 리서치"
powershell -ExecutionPolicy Bypass -File .\run_specialist_team_cycle.ps1 -Objective "거시경제와 기업분석을 별도 전문팀으로 검토한다" -Score 94 -ReviewedBy "보스"
```
## 고용 Dossier

`shinyong_hiring_dossier.json`과 `shinyong_hiring_dossier.ko.md`는 고용자가 열어볼 수 있는 학적·이력·시험·박사심사·추론 프로필·LLM 계약·고용 추천서입니다. 신용이를 “에이전트로 고용한다”는 행위가 단순 페르소나 지정이 아니라 검증된 인재 기록을 바탕으로 이루어지도록 만든 증빙 파일입니다.
