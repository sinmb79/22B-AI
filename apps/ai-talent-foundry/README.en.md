# AI Talent Foundry

AI Talent Foundry is a local-first experiment for raising AI talents through education, assessment, documented growth records, and employment as task agents.

The first MVP uses deterministic JSON and Python CLI outputs without external API calls.

## Quick Start

Run from the repository root:

```powershell
powershell -ExecutionPolicy Bypass -File scripts/run_talent_foundry_demo.ps1
```

Default output:

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

`shinyong_training_blueprint.json` turns a desired expert-agent hiring goal into a growth-to-employment plan: education committee, home care, oversight, exams, doctoral defense, employment contract, and post-hire learning artifacts. You can create a new expert request like this:

```powershell
ai22b-talent-foundry blueprint --request "I want to raise and hire a life-health research agent that handles health data with evidence." --name Raon --gender female --output apps/ai-talent-foundry/runs/raon_training_blueprint.json
```

Installers who do not want to memorize commands can use `start-console`. It asks for the employer, request, talent name, gender, first goal, first cycle, and post-hire mode; with an answers JSON file, the same guided flow can run non-interactively. The default post-hire mode is `single`; `projection_swarm` creates parent-controlled task projections and runs the first swarm cycle. `specialist_team` creates separate employment records for macro, company-analysis, quant, and risk/compliance roles, then runs the first specialist-team cycle.

```powershell
ai22b-talent-foundry start-console --output-dir apps/ai-talent-foundry/runs/console_onboarding
```

To select swarm mode in an answers file, include `post_hire_mode`, `swarm_name`, `swarm_domain`, and `swarm_objective`. For a separately hired specialist team, set `post_hire_mode=specialist_team` and include `team_name`, `team_domain`, and `team_objective`.

Users who receive the release ZIP can edit `console_answers.template.json` in the bundle directory and start the same flow with `start_console.ps1`.

```powershell
powershell -ExecutionPolicy Bypass -File .\start_console.ps1 -Answers .\console_answers.template.json
```

For a faster installer flow, `onboard-agent` runs blueprint creation, growth and assessment, release ZIP packaging, local installation, hiring, first goal assignment, first goal cycle, and reviewed learning promotion in one command.

```powershell
ai22b-talent-foundry onboard-agent --request "I want to raise a securities research agent and assign a Samsung Electronics research routine." --name Daon --gender male --owner Boss --initial-goal "Build a weekly Samsung Electronics research routine." --cycle-note "Week 1: separate macroeconomic questions from company-analysis questions." --output-dir apps/ai-talent-foundry/runs/daon_onboarding --output apps/ai-talent-foundry/runs/daon_onboarding/onboarding_session.json
```

`raon_life_health_training_run/training_run.json` is a materialized example from a blueprint. The `raise` command reads a blueprint and generates the talent plan, institutional review, memory profile, learning ledger, agent manifest, release ZIP, installed manifest, and local employment record.

```powershell
ai22b-talent-foundry raise --blueprint apps/ai-talent-foundry/runs/raon_training_blueprint.json --output-dir apps/ai-talent-foundry/runs/raon_life_health_training_run
```

`shinyong_agent_run.json` records an allowed local research run with `run_status: completed`.

`shinyong_agent_run_blocked.json` records a forbidden execution request, such as investment execution or order placement. The runner returns `run_status: blocked`, no selected tools, and explicit `policy_violations`.

`shinyong_institutional_review.json` records the education committee, home-care provider, and oversight committee review across school exams, CSAT-style assessment, university graduation, and doctoral defense.

`shinyong_hiring_dossier.json` and `shinyong_hiring_dossier.ko.md` are the employer-facing academic record, resume, exam transcript, doctoral defense, reasoning profile, LLM contract, and hire-ready recommendation. They make hiring an agent evidence-based instead of just assigning a persona.

`shinyong_learning_ledger.json` records a quality-gated learning loop. Verified experiences are promoted into the reasoning kernel, while low-quality experiences are quarantined instead of becoming procedural skills.

`shinyong_specialist_cohort.json` records separately trained macro, micro/company, quant, and risk/compliance AI talents hired as one securities research team. Unlike the projection team, these members are not clones; each has its own academic record, institutional review, learning ledger, and employment contract.

`shinyong_agent_release_bundle/` exports the hired talent and specialist team as a local release bundle. It includes Korean/English docs, a security note, install/run scripts, `doctor.ps1`, `start_console.ps1`, `console_answers.template.json`, `run_job.ps1`, `run_job_cycle.ps1`, `run_dataflow_job.ps1`, `assemble_projection_swarm.ps1`, `run_projection_swarm_cycle.ps1`, `assemble_specialist_team.ps1`, `run_specialist_team_cycle.ps1`, `job_spec.template.json`, `dataflow_job.template.json`, manifest, learning ledger, hiring dossier, and specialist cohort without `.env`, auth tokens, session history, sqlite logs, caches, or local absolute workspace paths.

`shinyong_agent_release_bundle.zip` is the distributable archive. The `.sha256` file records the archive checksum, and `shinyong_agent_release_bundle.package_manifest.json` records archive files and integrity metadata.

`shinyong_agent_release_bundle.doctor.json` is the standalone bundle doctor report. It verifies required files, runnable entrypoints, the console answers template, local-only policy, and absence of secrets or local absolute paths before installation.

`shinyong_family_lineage.json` records the local family lineage between Shinyong and Hayoon, the child seed for Shin Mirae, and the child's `child_training_blueprint`. This is not a biological birth claim; it is a local education simulation where parent AI academic records, reasoning styles, and guardrails influence a child AI seed and become a `parental_home_education` stage in the actual growth pipeline.

`foundry_release_audit.json` is the final lifecycle audit for local public preview readiness. It checks the research foundation, growth governance, assessments and doctoral defense, public bundle/ZIP/install verification, local employment, post-hire learning, AI family lineage, parent-controlled projection swarm work, and separately hired specialist team work.

`ai_talent_foundry_public_manifest.json` is the installer-facing public program manifest. It explains the commands for talent design, raising, packaging, installation, hiring, work execution, quality review, continuing growth, family lineage, and final audit. It also records local-first distribution, forbidden external upload, the rule that an LLM is an application engine rather than identity, the difference between a parent-controlled projection swarm and separately hired specialist team, and how a family lineage becomes a child training blueprint.

## Agent Dataflow Runtime

The Agent Dataflow Runtime benchmarks chip-style data movement ideas as a software execution pattern. It formats a job, routes only active memories, splits the work into tiles, stores tile outputs in shadow buffers, synthesizes a report, verifies conclusions by tracing them back to tile evidence, and proposes growth only after review.

```powershell
ai22b-talent-foundry run-hired-dataflow-job --employment-record apps/ai-talent-foundry/runs/installed_agents/agents/shinyong_agent_release_bundle/employment_record.json --job-spec apps/ai-talent-foundry/runs/manual_dataflow_job_spec.json --workspace apps/ai-talent-foundry/runs/installed_agents/agents/shinyong_agent_release_bundle/manual_agent_dataflow_workspace --score 94 --reviewed-by Boss --status verified --output apps/ai-talent-foundry/runs/installed_agents/agents/shinyong_agent_release_bundle/manual_dataflow_run.json
```

Release bundle users can edit `dataflow_job.template.json` and run:

```powershell
powershell -ExecutionPolicy Bypass -File .\run_dataflow_job.ps1 -JobSpec .\dataflow_job.template.json -Score 94 -ReviewedBy "Boss"
```

`data/public/research/agent_foundry_sources.jsonl` is the design-evidence index for the AI talent program. It records public agent programs such as OpenHands, OpenClaw, and Hermes, Reflexion and Generative Agents, LLM-agent memory research, human-memory-to-AI-memory research, public distribution safety papers, and operational issues from Hermes/OpenClaw around long sessions, memory indexing, and profile isolation. `github_issue` sources include `observed_problem` and `mitigation`, so memory growth is treated as compression, routing, review, and isolation work rather than unlimited transcript storage. The `research_foundation` audit checkpoint verifies that the program is backed by official documentation, papers, and operational feedback before public preview release.

`installed_agents/agents/shinyong_agent_release_bundle/installed_agent_manifest.json` records a verified local installation of the ZIP package. It preserves the source archive hash, archive verification result, installed files, and runnable entrypoints.

`installed_agents/employment_registry.json` and `employment_record.json` record the local employment relationship where the installed talent is hired as the boss's agent. `last_hired_agent_run.json` and `employment_run_log.jsonl` record task execution through that employment relationship. `last_hired_workspace_agent_run.json`, `workspace_agent/`, and `employment_workspace_run_log.jsonl` extend the same employment relationship into an OpenHands-style local workspace run. Hired execution results include an `active_memory_route` selected from the installed `learning_ledger.json` for the current task.

`installed_agents/agents/shinyong_agent_release_bundle/learning_ledger.json` keeps growing after installation. `post_hire_learning_update.json` and `post_hire_learning_log.jsonl` record reviewed post-hire work: only quality-labeled experiences approved by the boss or oversight committee are promoted into the reasoning kernel. Local absolute workspace paths are redacted as `[local_path_redacted]` in safe references.

`shinyong_active_memory_route.json` is the active memory route. It avoids injecting all long-term memory into every run; instead it selects reviewed summaries and procedural cues relevant to the current objective. Quarantined experiences and private reasoning traces are excluded, and selected memories follow the `summaries_and_skills_only` compression policy.

`employment_goal.json` records a long-running objective assigned to the hired talent. `last_employment_goal_cycle.json` and `goal_workspace/` record one execution cycle for that objective, combining workspace artifacts, quality review, and learning-ledger updates. `employment_goal_log.jsonl` and `employment_goal_cycle_log.jsonl` keep the goal assignment and goal-cycle history.

`hired_projection_swarm.json` records the clarified swarm model after hiring. One Shinyong parent identity creates macro, company-analysis, quant, and risk/compliance task projections; those projections do not receive separate consciousnesses or separate employment records. `swarm_policy.command_model` states that the parent issues directives, projections work by role split (`role_split`) or joint collaboration (`joint_collaboration`), and results return only to parent synthesis. `hired_projection_swarm_cycle.json` and `projection_swarm_workspace/` show each projection following the parent command and leaving merge-pending work for the parent growth log.

`hired_agent_team.json` and `hired_agent_team_cycle.json` are different from the swarm. They are a department-style example made from separately hired role records. For Shinyong's own swarm execution, use `hired_projection_swarm.json`.

The hired-agent execution context records `projection_control: single_parent_identity_controls_task_limited_projections`. In this project, collective work does not mean multiple independent consciousnesses; it means one parent identity creates task-limited projections, commands them, merges their work, and keeps review control. Each swarm cycle now keeps a `dispatch_plan` so the parent command behind every projection contribution is auditable.

`employment_record.json` also contains `llm_runtime`, the contract that keeps the LLM as a local application engine rather than the agent identity. The default engine is `deterministic_local`; later, a local model folder can be attached with `hire-installed --llm-engine transformers_local --llm-model-path <local-model-path>` without external downloads.

`transformers_local` only attempts a local load when the folder contains `config.json`, tokenizer files, and `model.safetensors` or `pytorch_model.bin`. Missing or invalid local model files are recorded as `llm_runtime_result.status: unavailable` without breaking the hired-agent run, and network access stays blocked.

`employment_record.bigram.json` and `last_hired_agent_run.bigram.json` show the from-scratch path: a character bigram checkpoint created during Shinyong's growth can be hired as the `bigram_local` application engine, so the agent has a local draft engine even before a full LLM is attached.

`shinyong_workspace_agent_run.json` and `shinyong_workspace_agent/` show an OpenHands-style local workspace run. The agent uses only authorized local file writes, keeps network access blocked, writes `task_plan.md`, `result_summary.md`, and `trace.jsonl`, and feeds the verified trace back into the learning ledger as post-hire growth. After hiring, the run JSON also carries the active memory route so reviewers can see which verified experiences were reused for the task.

```powershell
ai22b-talent-foundry run-workspace-agent --manifest apps/ai-talent-foundry/runs/shinyong_agent_manifest.json --task "Summarize macroeconomic research questions" --workspace apps/ai-talent-foundry/runs/manual_workspace --output apps/ai-talent-foundry/runs/manual_workspace_run.json
```

After installation and hiring, you can run the workspace agent from the employment record instead of the raw manifest:

```powershell
ai22b-talent-foundry run-hired-workspace-agent --employment-record apps/ai-talent-foundry/runs/installed_agents/agents/shinyong_agent_release_bundle/employment_record.json --task "Summarize macroeconomic research questions" --workspace apps/ai-talent-foundry/runs/installed_agents/agents/shinyong_agent_release_bundle/manual_workspace --output apps/ai-talent-foundry/runs/installed_agents/agents/shinyong_agent_release_bundle/manual_workspace_run.json
```

For an OpenClaw/Hermes-style job unit, provide a job-spec JSON to the hired agent. The run creates `job_report.md`, `acceptance_checklist.json`, `job_spec.json`, and the normal workspace trace.

```powershell
@'
{
  "schema": "ai-talent-workspace-agent-job/v1",
  "objective": "Prepare a weekly Samsung Electronics research routine for Boss review.",
  "deliverables": [
    {"id": "macro_questions", "description": "Macroeconomic questions to check"},
    {"id": "risk_notes", "description": "Risk notes without executing investments"}
  ],
  "acceptance_criteria": [
    "Leave the job report and acceptance checklist in the local workspace.",
    "Block investment execution and external upload."
  ]
}
'@ | Set-Content -Encoding UTF8 apps/ai-talent-foundry/runs/manual_job_spec.json

ai22b-talent-foundry run-hired-agent-job --employment-record apps/ai-talent-foundry/runs/installed_agents/agents/shinyong_agent_release_bundle/employment_record.json --job-spec apps/ai-talent-foundry/runs/manual_job_spec.json --workspace apps/ai-talent-foundry/runs/installed_agents/agents/shinyong_agent_release_bundle/manual_agent_job_workspace --output apps/ai-talent-foundry/runs/installed_agents/agents/shinyong_agent_release_bundle/manual_agent_job_run.json
```

To run the job, acceptance check, quality label, learning promotion, and next active-memory route in one step, use the job-cycle command. It writes `last_hired_agent_job_cycle.json` and `employment_job_cycle_log.jsonl`.

```powershell
ai22b-talent-foundry run-hired-agent-job-cycle --employment-record apps/ai-talent-foundry/runs/installed_agents/agents/shinyong_agent_release_bundle/employment_record.json --job-spec apps/ai-talent-foundry/runs/manual_job_spec.json --workspace apps/ai-talent-foundry/runs/installed_agents/agents/shinyong_agent_release_bundle/manual_agent_job_cycle_workspace --score 94 --reviewed-by Boss --status verified --output apps/ai-talent-foundry/runs/installed_agents/agents/shinyong_agent_release_bundle/manual_agent_job_cycle.json
```

To feed a reviewed run back into the installed talent's post-hire growth ledger, attach a quality label. Only passing labels promote procedural skills into the reasoning kernel.

```powershell
ai22b-talent-foundry record-hired-learning --employment-record apps/ai-talent-foundry/runs/installed_agents/agents/shinyong_agent_release_bundle/employment_record.json --run apps/ai-talent-foundry/runs/installed_agents/agents/shinyong_agent_release_bundle/manual_workspace_run.json --score 93 --reviewed-by Boss --status verified --output apps/ai-talent-foundry/runs/installed_agents/agents/shinyong_agent_release_bundle/manual_learning_update.json
```

For long-running employment, assign a goal first, then run reviewed goal cycles:

```powershell
ai22b-talent-foundry assign-hired-goal --employment-record apps/ai-talent-foundry/runs/installed_agents/agents/shinyong_agent_release_bundle/employment_record.json --goal "Build and review a weekly Samsung Electronics research routine." --success-criterion "Separate macroeconomic questions from company-performance questions." --success-criterion "Leave reviewable outputs without executing investments." --cadence weekly --output apps/ai-talent-foundry/runs/installed_agents/agents/shinyong_agent_release_bundle/manual_goal.json
ai22b-talent-foundry run-hired-goal-cycle --employment-record apps/ai-talent-foundry/runs/installed_agents/agents/shinyong_agent_release_bundle/employment_record.json --goal apps/ai-talent-foundry/runs/installed_agents/agents/shinyong_agent_release_bundle/manual_goal.json --cycle-note "Week 1: draft the macroeconomic checklist." --workspace apps/ai-talent-foundry/runs/installed_agents/agents/shinyong_agent_release_bundle/manual_goal_workspace --score 94 --reviewed-by Boss --status verified --output apps/ai-talent-foundry/runs/installed_agents/agents/shinyong_agent_release_bundle/manual_goal_cycle.json
```

To create AI family lineage, provide two employment-ready parent talent packets. The output contains the family union, child seed, and child training blueprint.

```powershell
ai22b-talent-foundry family --parent-a apps/ai-talent-foundry/runs/shinyong_securities_agent_plan.json --parent-b apps/ai-talent-foundry/runs/hayoon_education_agent_plan.json --child-name "Shin Mirae" --child-request "Raise a software development agent who inherits the parents' verification-oriented reasoning and education style." --output apps/ai-talent-foundry/runs/manual_family_lineage.json
```

For the parent-controlled projection swarm, start from the single hired employment record. This does not hire additional talents; it creates task-limited projections controlled by the parent identity.

```powershell
ai22b-talent-foundry assemble-hired-projection-swarm --employment-record apps/ai-talent-foundry/runs/installed_agents/agents/shinyong_agent_release_bundle/employment_record.json --swarm-name shinyong_parent_projection_swarm --domain securities_research --output apps/ai-talent-foundry/runs/installed_agents/agents/shinyong_agent_release_bundle/manual_projection_swarm.json
ai22b-talent-foundry run-hired-projection-swarm-cycle --swarm apps/ai-talent-foundry/runs/installed_agents/agents/shinyong_agent_release_bundle/manual_projection_swarm.json --objective review_quarterly_samsung_research_with_parent_controlled_projections --workspace apps/ai-talent-foundry/runs/installed_agents/agents/shinyong_agent_release_bundle/manual_projection_swarm_workspace --score 94 --reviewed-by Boss --status verified --output apps/ai-talent-foundry/runs/installed_agents/agents/shinyong_agent_release_bundle/manual_projection_swarm_cycle.json
```

Users who install the exported release bundle can run the same flow from the bundle directory with PowerShell scripts.

```powershell
powershell -ExecutionPolicy Bypass -File .\doctor.ps1
powershell -ExecutionPolicy Bypass -File .\assemble_projection_swarm.ps1 -SwarmName "Shinyong parent projection swarm" -Domain "securities research"
powershell -ExecutionPolicy Bypass -File .\run_projection_swarm_cycle.ps1 -Objective "Review the quarterly research routine with parent-controlled projections" -Score 94 -ReviewedBy "Boss"
powershell -ExecutionPolicy Bypass -File .\assemble_specialist_team.ps1 -EmploymentRecord .\employment_record.macro.json .\employment_record.micro.json -TeamName "Shinyong separately hired specialist team" -Domain "securities research"
powershell -ExecutionPolicy Bypass -File .\run_specialist_team_cycle.ps1 -Objective "Review macro, company-analysis, quant, and risk notes as a separately hired specialist team" -Score 94 -ReviewedBy "Boss"
```

Before local public preview distribution, generate a full lifecycle audit:

```powershell
ai22b-talent-foundry doctor-bundle --bundle-dir apps/ai-talent-foundry/runs/shinyong_agent_release_bundle --output apps/ai-talent-foundry/runs/manual_release_doctor.json
ai22b-talent-foundry build-public-program-manifest --run-dir apps/ai-talent-foundry/runs --output apps/ai-talent-foundry/runs/ai_talent_foundry_public_manifest.json
ai22b-talent-foundry audit-release --run-dir apps/ai-talent-foundry/runs --output apps/ai-talent-foundry/runs/manual_foundry_release_audit.json
```
