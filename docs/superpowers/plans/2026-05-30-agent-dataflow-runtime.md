# Agent Dataflow Runtime Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build a local, inspectable Agent Dataflow Runtime that runs hired AI talents through formatted jobs, active memory cache, task tiles, shadow buffers, reverse verification, and reviewed growth candidates.

**Architecture:** Add a focused `dataflow_runtime.py` module with pure functions first, then connect it to the existing registry, CLI, demo, release bundle, and doctor checks. The v1 scheduler is deterministic and sequential while preserving a matrix-shaped artifact model so later projection/team parallelism can be added without rewriting the artifact contract.

**Tech Stack:** Python standard library, `unittest`, local JSON/Markdown artifacts, existing `ai22b.talent_foundry` modules, PowerShell helper scripts.

---

## Scope

This plan implements the first working slice of the design in `docs/superpowers/specs/2026-05-30-agent-dataflow-runtime-design.md`.

It does not implement real hardware acceleration, true parallel workers, external market-data connectors, or financial advice execution. Investment execution remains blocked. The LLM remains an application engine, not the talent identity.

## File Structure

- Create `src/ai22b/talent_foundry/dataflow_runtime.py`
  - Owns schemas, formatter, active memory cache adapter, tile matrix, scheduler, shadow buffers, synthesis, transpose verification, growth commit candidate, and workspace artifact writing.
- Modify `src/ai22b/talent_foundry/registry.py`
  - Adds installed-agent wrapper `run_hired_dataflow_job(...)`.
- Modify `src/ai22b/talent_foundry/cli.py`
  - Adds `run-hired-dataflow-job` command.
- Modify `src/ai22b/talent_foundry/distribution.py`
  - Adds release template `dataflow_job.template.json`, script `run_dataflow_job.ps1`, manifest entrypoint, and doctor required-file coverage.
- Modify `src/ai22b/talent_foundry/demo.py`
  - Runs one Shin Yong dataflow job and includes artifacts in the public manifest/audit path if appropriate.
- Modify `src/ai22b/doctor.py` only if repository-level doctor needs a new dataflow readiness check.
- Modify `tests/test_talent_foundry.py`
  - Adds unit and integration tests for the runtime, CLI, installed-agent wrapper, release bundle, and demo output.
- Modify `apps/ai-talent-foundry/README.ko.md`
  - Korean usage section for dataflow jobs.
- Modify `apps/ai-talent-foundry/README.en.md`
  - English usage section for dataflow jobs.
- Modify `docs/log.md`
  - Add implementation note and verification commands.

---

### Task 1: Runtime Formatter And Memory Cache

**Files:**
- Create: `src/ai22b/talent_foundry/dataflow_runtime.py`
- Modify: `tests/test_talent_foundry.py`

- [ ] **Step 1: Write failing formatter test**

Add a test similar to:

```python
def test_dataflow_formatter_normalizes_job_and_blocks_investment_execution(self):
    from ai22b.talent_foundry.dataflow_runtime import format_dataflow_job

    job = format_dataflow_job({
        "objective": "삼성전자 분기 실적을 분석해줘",
        "deliverables": [{"id": "brief", "description": "보스 검토용 요약"}],
    })

    self.assertEqual(job["schema"], "ai-talent-dataflow-formatted-job/v1")
    self.assertEqual(job["objective"], "삼성전자 분기 실적을 분석해줘")
    self.assertIn("investment_execution", job["blocked_actions"])
    self.assertEqual(job["deliverables"][0]["id"], "brief")
    self.assertIn("source_date_check", job["required_evidence"])
```

- [ ] **Step 2: Run the failing formatter test**

Run:

```powershell
$env:PYTHONPATH='src'; python -m unittest tests.test_talent_foundry.TalentFoundryTests.test_dataflow_formatter_normalizes_job_and_blocks_investment_execution
```

Expected: FAIL because `ai22b.talent_foundry.dataflow_runtime` does not exist or `format_dataflow_job` is missing.

- [ ] **Step 3: Implement minimal formatter**

In `dataflow_runtime.py`, add:

```python
from __future__ import annotations

from datetime import datetime, timezone
from typing import Any

FORMATTED_JOB_SCHEMA = "ai-talent-dataflow-formatted-job/v1"

def _now() -> str:
    return datetime.now(timezone.utc).isoformat()

def format_dataflow_job(job_spec: dict[str, Any] | str) -> dict[str, Any]:
    if isinstance(job_spec, str):
        objective = job_spec.strip()
        raw = {"objective": objective}
    else:
        raw = dict(job_spec)
        objective = str(raw.get("objective", "")).strip()
    if not objective:
        raise ValueError("Dataflow job requires a non-empty objective")

    deliverables = raw.get("deliverables") or [
        {"id": "synthesis_report", "description": "보스 검토용 데이터플로우 종합 보고서"}
    ]
    acceptance = raw.get("acceptance_criteria") or [
        "모든 결론은 타일 증거 또는 불확실성 표시와 연결되어야 한다.",
        "투자 실행 권한은 차단되어야 한다.",
    ]
    blocked = list(dict.fromkeys(raw.get("blocked_actions", []) + [
        "investment_execution",
        "external_upload_without_boss_approval",
        "private_reasoning_trace_storage",
    ]))

    return {
        "schema": FORMATTED_JOB_SCHEMA,
        "created_at_utc": _now(),
        "objective": objective,
        "constraints": [str(item) for item in raw.get("constraints", [])],
        "deliverables": [
            {"id": str(item.get("id", f"deliverable_{index}")), "description": str(item.get("description", ""))}
            for index, item in enumerate(deliverables, start=1)
        ],
        "acceptance_criteria": [str(item) for item in acceptance],
        "blocked_actions": blocked,
        "required_evidence": raw.get("required_evidence") or ["source_date_check", "artifact_trace", "risk_boundary_check"],
        "domain_hints": raw.get("domain_hints") or ["securities_research"],
    }
```

- [ ] **Step 4: Run formatter test until it passes**

Run the same command as Step 2.

Expected: PASS.

- [ ] **Step 5: Write failing active memory cache test**

Add a test similar to:

```python
def test_dataflow_active_memory_cache_excludes_quarantined_experiences(self):
    from ai22b.talent_foundry.dataflow_runtime import build_active_memory_tile_cache
    from ai22b.talent_foundry.learning_loop import create_learning_ledger, record_learning_experience

    ledger = create_learning_ledger(owner="신용")
    record_learning_experience(
        ledger,
        source="workspace_agent_run",
        event={"run_status": "completed", "workspace_outputs": {"trace": "trace.jsonl"}},
        quality_label={"score": 92, "status": "verified"},
    )
    record_learning_experience(
        ledger,
        source="workspace_agent_run",
        event={"run_status": "failed", "private_reasoning_trace": "secret"},
        quality_label={"score": 20, "status": "failed"},
    )

    cache = build_active_memory_tile_cache(ledger, objective="증권 근거 검증")

    self.assertEqual(cache["schema"], "ai-talent-dataflow-active-memory-cache/v1")
    self.assertEqual(cache["owner"], "신용")
    self.assertEqual(cache["quarantined_experiences"], "excluded")
    self.assertEqual(cache["memory_health"]["quarantined_experience_count"], 1)
    self.assertNotIn("secret", json.dumps(cache, ensure_ascii=False))
```

- [ ] **Step 6: Run active memory cache test and verify failure**

Run:

```powershell
$env:PYTHONPATH='src'; python -m unittest tests.test_talent_foundry.TalentFoundryTests.test_dataflow_active_memory_cache_excludes_quarantined_experiences
```

Expected: FAIL because `build_active_memory_tile_cache` is missing.

- [ ] **Step 7: Implement memory cache wrapper**

Use `route_active_memory(...)` from `learning_loop.py`. Wrap its output with dataflow-specific schema and explicit cache policy.

- [ ] **Step 8: Run both Task 1 tests**

Run:

```powershell
$env:PYTHONPATH='src'; python -m unittest tests.test_talent_foundry.TalentFoundryTests.test_dataflow_formatter_normalizes_job_and_blocks_investment_execution tests.test_talent_foundry.TalentFoundryTests.test_dataflow_active_memory_cache_excludes_quarantined_experiences
```

Expected: PASS.

---

### Task 2: Tile Matrix, Scheduler, Shadow Buffers

**Files:**
- Modify: `src/ai22b/talent_foundry/dataflow_runtime.py`
- Modify: `tests/test_talent_foundry.py`

- [ ] **Step 1: Write failing tile matrix test**

```python
def test_dataflow_tile_matrix_creates_securities_tiles_with_safety_first(self):
    from ai22b.talent_foundry.dataflow_runtime import (
        build_task_tile_matrix,
        format_dataflow_job,
    )

    formatted = format_dataflow_job("삼성전자 실적과 거시환경을 분석해줘")
    matrix = build_task_tile_matrix(formatted, domain="securities_research")

    self.assertEqual(matrix["schema"], "ai-talent-dataflow-tile-matrix/v1")
    self.assertEqual(matrix["execution_policy"], "deterministic_sequential_v1")
    tile_ids = [tile["tile_id"] for tile in matrix["tiles"]]
    self.assertIn("evidence", tile_ids)
    self.assertIn("risk_compliance", tile_ids)
    self.assertIn("macro", tile_ids)
    self.assertIn("synthesis", tile_ids)
    self.assertLess(tile_ids.index("evidence"), tile_ids.index("synthesis"))
```

- [ ] **Step 2: Run tile matrix test and verify failure**

Run:

```powershell
$env:PYTHONPATH='src'; python -m unittest tests.test_talent_foundry.TalentFoundryTests.test_dataflow_tile_matrix_creates_securities_tiles_with_safety_first
```

Expected: FAIL because `build_task_tile_matrix` is missing.

- [ ] **Step 3: Implement deterministic securities tile matrix**

Create fixed tile templates for:

- `evidence`
- `risk_compliance`
- `macro`
- `micro`
- `quant`
- `synthesis`

Keep tile fields small: `tile_id`, `role`, `purpose`, `inputs`, `depends_on`, `blocked_actions`.

- [ ] **Step 4: Write failing shadow buffer test**

```python
def test_dataflow_shadow_buffers_keep_tile_outputs_separate(self):
    from ai22b.talent_foundry.dataflow_runtime import (
        build_shadow_result_buffers,
        build_task_tile_matrix,
        format_dataflow_job,
    )

    matrix = build_task_tile_matrix(format_dataflow_job("근거 중심 리서치"))
    buffers = build_shadow_result_buffers(matrix)

    self.assertEqual(buffers["schema"], "ai-talent-dataflow-shadow-buffers/v1")
    self.assertEqual(len(buffers["buffers"]), len(matrix["tiles"]))
    for buffer in buffers["buffers"]:
        self.assertIn("tile_id", buffer)
        self.assertIn("claim_summary", buffer)
        self.assertIn("evidence_summary", buffer)
        self.assertIn("uncertainties", buffer)
        self.assertNotEqual(buffer["status"], "final_truth")
```

- [ ] **Step 5: Run shadow buffer test and verify failure**

Run:

```powershell
$env:PYTHONPATH='src'; python -m unittest tests.test_talent_foundry.TalentFoundryTests.test_dataflow_shadow_buffers_keep_tile_outputs_separate
```

Expected: FAIL because `build_shadow_result_buffers` is missing.

- [ ] **Step 6: Implement scheduled mock tile execution and buffers**

For v1, use deterministic textual outputs per tile. Do not call external APIs. Make safety and evidence tiles explicit.

- [ ] **Step 7: Run Task 2 tests**

Run:

```powershell
$env:PYTHONPATH='src'; python -m unittest tests.test_talent_foundry.TalentFoundryTests.test_dataflow_tile_matrix_creates_securities_tiles_with_safety_first tests.test_talent_foundry.TalentFoundryTests.test_dataflow_shadow_buffers_keep_tile_outputs_separate
```

Expected: PASS.

---

### Task 3: Synthesis, Transpose Verification, Growth Commit Gate

**Files:**
- Modify: `src/ai22b/talent_foundry/dataflow_runtime.py`
- Modify: `tests/test_talent_foundry.py`

- [ ] **Step 1: Write failing transpose verification test**

```python
def test_dataflow_transpose_verification_fails_unsupported_conclusion(self):
    from ai22b.talent_foundry.dataflow_runtime import verify_dataflow_transpose

    result = verify_dataflow_transpose(
        synthesis={"conclusions": [{"id": "c1", "text": "무근거 결론", "supporting_tiles": []}]},
        shadow_buffers={"buffers": []},
        acceptance_criteria=["결론은 근거와 연결되어야 한다."],
    )

    self.assertEqual(result["schema"], "ai-talent-dataflow-transpose-verification/v1")
    self.assertEqual(result["status"], "failed")
    self.assertTrue(result["issues"])
```

- [ ] **Step 2: Run transpose test and verify failure**

Run:

```powershell
$env:PYTHONPATH='src'; python -m unittest tests.test_talent_foundry.TalentFoundryTests.test_dataflow_transpose_verification_fails_unsupported_conclusion
```

Expected: FAIL because `verify_dataflow_transpose` is missing.

- [ ] **Step 3: Implement synthesis and transpose verification**

Add:

- `synthesize_dataflow_report(...)`
- `verify_dataflow_transpose(...)`

Verification should fail if:

- A conclusion has no supporting tiles.
- Required acceptance criteria have no artifact evidence.
- Investment execution is not listed as blocked.

- [ ] **Step 4: Write failing growth commit gate test**

```python
def test_dataflow_growth_commit_gate_promotes_only_verified_runs(self):
    from ai22b.talent_foundry.dataflow_runtime import build_growth_commit_candidate

    candidate = build_growth_commit_candidate(
        run_result={"run_status": "completed", "objective": "근거 검증"},
        verification={"status": "passed", "issues": []},
        review_label={"score": 91, "status": "verified", "reviewed_by": "보스"},
    )

    self.assertEqual(candidate["schema"], "ai-talent-dataflow-growth-commit-candidate/v1")
    self.assertEqual(candidate["promotion_status"], "promote_to_learning_ledger")
    self.assertNotIn("private_reasoning_trace", candidate)

    blocked = build_growth_commit_candidate(
        run_result={"run_status": "completed", "objective": "근거 검증"},
        verification={"status": "failed", "issues": ["missing evidence"]},
        review_label={"score": 91, "status": "verified", "reviewed_by": "보스"},
    )
    self.assertEqual(blocked["promotion_status"], "quarantine")
```

- [ ] **Step 5: Run growth gate test and verify failure**

Run:

```powershell
$env:PYTHONPATH='src'; python -m unittest tests.test_talent_foundry.TalentFoundryTests.test_dataflow_growth_commit_gate_promotes_only_verified_runs
```

Expected: FAIL because `build_growth_commit_candidate` is missing.

- [ ] **Step 6: Implement growth commit candidate**

Promotion requires:

- `run_status == "completed"`
- `verification.status == "passed"`
- review status in `verified`, `approved`, or `passed`
- score >= 80

Otherwise quarantine.

- [ ] **Step 7: Run Task 3 tests**

Run:

```powershell
$env:PYTHONPATH='src'; python -m unittest tests.test_talent_foundry.TalentFoundryTests.test_dataflow_transpose_verification_fails_unsupported_conclusion tests.test_talent_foundry.TalentFoundryTests.test_dataflow_growth_commit_gate_promotes_only_verified_runs
```

Expected: PASS.

---

### Task 4: Full Dataflow Job Workspace Runner

**Files:**
- Modify: `src/ai22b/talent_foundry/dataflow_runtime.py`
- Modify: `tests/test_talent_foundry.py`

- [ ] **Step 1: Write failing full runner test**

```python
def test_dataflow_runtime_writes_workspace_artifacts_for_hired_manifest(self):
    from ai22b.talent_foundry.dataflow_runtime import run_dataflow_job_from_manifest

    manifest = self._sample_agent_manifest()
    ledger = self._sample_learning_ledger(owner="신용")
    workspace = self.temp_dir / "dataflow_workspace"

    run = run_dataflow_job_from_manifest(
        manifest,
        ledger=ledger,
        job_spec={"objective": "삼성전자 실적과 거시환경을 근거 중심으로 분석"},
        workspace_dir=workspace,
        review_label={"score": 90, "status": "verified", "reviewed_by": "보스"},
    )

    self.assertEqual(run["schema"], "ai-talent-dataflow-run/v1")
    self.assertEqual(run["run_status"], "completed")
    for key in [
        "formatted_job",
        "active_memory_cache",
        "tile_matrix",
        "shadow_buffers",
        "synthesis_report",
        "transpose_verification",
        "growth_commit_candidate",
    ]:
        self.assertIn(key, run["workspace_outputs"])
        self.assertTrue(Path(run["workspace_outputs"][key]).exists())
```

Use existing helper patterns in `tests/test_talent_foundry.py`; if helper names differ, add local fixtures inside the test class.

- [ ] **Step 2: Run full runner test and verify failure**

Run:

```powershell
$env:PYTHONPATH='src'; python -m unittest tests.test_talent_foundry.TalentFoundryTests.test_dataflow_runtime_writes_workspace_artifacts_for_hired_manifest
```

Expected: FAIL because `run_dataflow_job_from_manifest` is missing.

- [ ] **Step 3: Implement `run_dataflow_job_from_manifest`**

Implementation order:

1. Format job.
2. Build active memory cache.
3. Build tile matrix.
4. Build shadow buffers.
5. Synthesize Markdown report.
6. Run transpose verification.
7. Build growth commit candidate.
8. Write JSON/Markdown artifacts using safe workspace paths.
9. Return run summary with artifact paths.

- [ ] **Step 4: Run full runner test**

Run:

```powershell
$env:PYTHONPATH='src'; python -m unittest tests.test_talent_foundry.TalentFoundryTests.test_dataflow_runtime_writes_workspace_artifacts_for_hired_manifest
```

Expected: PASS.

---

### Task 5: Registry And CLI Command

**Files:**
- Modify: `src/ai22b/talent_foundry/registry.py`
- Modify: `src/ai22b/talent_foundry/cli.py`
- Modify: `tests/test_talent_foundry.py`

- [ ] **Step 1: Write failing installed-agent registry test**

```python
def test_registry_runs_hired_dataflow_job_from_employment_record(self):
    from ai22b.talent_foundry.registry import run_hired_dataflow_job

    employment_record = self._install_and_hire_sample_agent()
    workspace = self.temp_dir / "installed_dataflow"

    run = run_hired_dataflow_job(
        employment_record,
        job_spec={"objective": "고용된 신용이 증권 리서치 데이터플로우 실행"},
        workspace_dir=workspace,
        review_label={"score": 90, "status": "verified", "reviewed_by": "보스"},
    )

    self.assertEqual(run["schema"], "ai-talent-dataflow-run/v1")
    self.assertEqual(run["run_status"], "completed")
```

Adapt helper calls to existing install/hire test fixtures.

- [ ] **Step 2: Run registry test and verify failure**

Run:

```powershell
$env:PYTHONPATH='src'; python -m unittest tests.test_talent_foundry.TalentFoundryTests.test_registry_runs_hired_dataflow_job_from_employment_record
```

Expected: FAIL because `run_hired_dataflow_job` is missing.

- [ ] **Step 3: Implement registry wrapper**

Load the employment record, installed manifest, and installed learning ledger. Then call `run_dataflow_job_from_manifest`.

- [ ] **Step 4: Write failing CLI test**

```python
def test_cli_run_hired_dataflow_job_writes_run_and_workspace_outputs(self):
    employment_record = self._install_and_hire_sample_agent()
    job = self.temp_dir / "dataflow_job.json"
    output = self.temp_dir / "dataflow_run.json"
    workspace = self.temp_dir / "dataflow_workspace"
    job.write_text(json.dumps({"objective": "데이터플로우 CLI 실행"}, ensure_ascii=False), encoding="utf-8")

    self._run_cli([
        "run-hired-dataflow-job",
        "--employment-record", str(employment_record),
        "--job-spec", str(job),
        "--workspace", str(workspace),
        "--score", "91",
        "--reviewed-by", "보스",
        "--status", "verified",
        "--output", str(output),
    ])

    data = json.loads(output.read_text(encoding="utf-8"))
    self.assertEqual(data["schema"], "ai-talent-dataflow-run/v1")
    self.assertTrue((workspace / "formatted_job.json").exists())
```

- [ ] **Step 5: Run CLI test and verify failure**

Run:

```powershell
$env:PYTHONPATH='src'; python -m unittest tests.test_talent_foundry.TalentFoundryTests.test_cli_run_hired_dataflow_job_writes_run_and_workspace_outputs
```

Expected: FAIL because the CLI command is missing.

- [ ] **Step 6: Implement CLI command**

Add parser command:

```text
run-hired-dataflow-job
  --employment-record
  --job-spec
  --workspace
  --score
  --reviewed-by
  --status
  --output
```

Add handler in `main(...)` following existing registry command patterns.

- [ ] **Step 7: Run Task 5 tests**

Run:

```powershell
$env:PYTHONPATH='src'; python -m unittest tests.test_talent_foundry.TalentFoundryTests.test_registry_runs_hired_dataflow_job_from_employment_record tests.test_talent_foundry.TalentFoundryTests.test_cli_run_hired_dataflow_job_writes_run_and_workspace_outputs
```

Expected: PASS.

---

### Task 6: Release Bundle, Scripts, Doctor, Docs

**Files:**
- Modify: `src/ai22b/talent_foundry/distribution.py`
- Modify: `tests/test_talent_foundry.py`
- Modify: `apps/ai-talent-foundry/README.ko.md`
- Modify: `apps/ai-talent-foundry/README.en.md`
- Modify: `docs/log.md`

- [ ] **Step 1: Write failing release bundle test**

Extend the existing release bundle test to assert:

```python
self.assertTrue((bundle_dir / "run_dataflow_job.ps1").exists())
self.assertTrue((bundle_dir / "dataflow_job.template.json").exists())
manifest = json.loads((bundle_dir / "bundle_manifest.json").read_text(encoding="utf-8"))
self.assertIn("run_dataflow_job", manifest["entrypoints"])
```

- [ ] **Step 2: Run release bundle test and verify failure**

Run the existing release bundle test:

```powershell
$env:PYTHONPATH='src'; python -m unittest tests.test_talent_foundry.TalentFoundryTests.test_release_bundle_exports_hired_agent_without_private_runtime_state
```

Expected: FAIL because dataflow entrypoint/template is missing.

- [ ] **Step 3: Add release script and template generation**

In `distribution.py`, add:

- `dataflow_job.template.json`
- `run_dataflow_job.ps1`
- manifest entrypoint `run_dataflow_job`
- README mention in generated bundle docs if docs are generated there.

PowerShell script should call:

```powershell
python -m ai22b.talent_foundry.cli run-hired-dataflow-job ...
```

following the installed-agent script style already used by job/team/projection scripts.

- [ ] **Step 4: Extend doctor bundle expected files**

Make doctor require:

- `run_dataflow_job.ps1`
- `dataflow_job.template.json`

Only do this after release generation writes them.

- [ ] **Step 5: Update README files**

Add a short Korean-first section:

- What a dataflow job is.
- Why it exists.
- How to run the bundled script.
- What files are produced.
- Investment execution remains blocked.

Mirror in English with a link target from the Korean README if the project pattern supports it.

- [ ] **Step 6: Update `docs/log.md`**

Add date section:

```markdown
# 2026-05-30 Agent Dataflow Runtime

- Added Tesla/TPU-inspired dataflow execution design and implementation plan.
- Planned local-first job formatting, memory cache, task tiles, shadow buffers, reverse verification, and growth gate.
- Verification commands: ...
```

- [ ] **Step 7: Run release/doctor tests**

Run:

```powershell
$env:PYTHONPATH='src'; python -m unittest tests.test_talent_foundry.TalentFoundryTests.test_release_bundle_exports_hired_agent_without_private_runtime_state tests.test_talent_foundry.TalentFoundryTests.test_install_release_package_extracts_verified_agent_to_local_registry
```

Expected: PASS.

---

### Task 7: Demo Integration And Full Verification

**Files:**
- Modify: `src/ai22b/talent_foundry/demo.py`
- Modify: `tests/test_talent_foundry.py`
- Modify: `docs/log.md`

- [ ] **Step 1: Write failing demo output test**

Extend `test_demo_runner_writes_all_local_outputs` to assert:

```python
self.assertIn("dataflow_run", outputs)
self.assertTrue(Path(outputs["dataflow_run"]).exists())
self.assertIn("dataflow_workspace", outputs)
self.assertTrue(Path(outputs["dataflow_workspace"]).exists())
```

If the demo output structure differs, assert the actual demo result keys after inspection.

- [ ] **Step 2: Run demo test and verify failure**

Run:

```powershell
$env:PYTHONPATH='src'; python -m unittest tests.test_talent_foundry.TalentFoundryTests.test_demo_runner_writes_all_local_outputs
```

Expected: FAIL because demo does not run dataflow yet.

- [ ] **Step 3: Implement demo dataflow job**

In `demo.py`, after installed/hired agent setup:

- Create a small securities dataflow job spec.
- Run `run_hired_dataflow_job`.
- Write output to `shinyong_dataflow_run.json`.
- Use workspace `shinyong_dataflow_workspace`.
- Include result paths in demo outputs.

- [ ] **Step 4: Run demo test**

Run:

```powershell
$env:PYTHONPATH='src'; python -m unittest tests.test_talent_foundry.TalentFoundryTests.test_demo_runner_writes_all_local_outputs
```

Expected: PASS.

- [ ] **Step 5: Run focused dataflow test set**

Run:

```powershell
$env:PYTHONPATH='src'; python -m unittest tests.test_talent_foundry.TalentFoundryTests.test_dataflow_formatter_normalizes_job_and_blocks_investment_execution tests.test_talent_foundry.TalentFoundryTests.test_dataflow_active_memory_cache_excludes_quarantined_experiences tests.test_talent_foundry.TalentFoundryTests.test_dataflow_tile_matrix_creates_securities_tiles_with_safety_first tests.test_talent_foundry.TalentFoundryTests.test_dataflow_shadow_buffers_keep_tile_outputs_separate tests.test_talent_foundry.TalentFoundryTests.test_dataflow_transpose_verification_fails_unsupported_conclusion tests.test_talent_foundry.TalentFoundryTests.test_dataflow_growth_commit_gate_promotes_only_verified_runs tests.test_talent_foundry.TalentFoundryTests.test_dataflow_runtime_writes_workspace_artifacts_for_hired_manifest tests.test_talent_foundry.TalentFoundryTests.test_registry_runs_hired_dataflow_job_from_employment_record tests.test_talent_foundry.TalentFoundryTests.test_cli_run_hired_dataflow_job_writes_run_and_workspace_outputs
```

Expected: PASS.

- [ ] **Step 6: Run full Python test suite**

Run:

```powershell
powershell -ExecutionPolicy Bypass -File scripts\run_tests.ps1
```

Expected: all tests pass.

- [ ] **Step 7: Run demo script**

Run:

```powershell
powershell -ExecutionPolicy Bypass -File scripts\run_talent_foundry_demo.ps1
```

Expected: output lists `shinyong_dataflow_run.json` and the dataflow workspace artifacts.

- [ ] **Step 8: Run doctor**

Run:

```powershell
powershell -ExecutionPolicy Bypass -File scripts\run_doctor.ps1
```

Expected: required checks pass. Existing optional dependency warnings may remain acceptable if they are unchanged and documented.

---

### Task 8: Public GitHub Release Gate

**Files:**
- Modify: `.gitignore`
- Modify: `README.ko.md`
- Modify: `README.en.md`
- Optional Create: `docs/PUBLIC_RELEASE_CHECKLIST.ko.md`
- Optional Create: `docs/PUBLIC_RELEASE_CHECKLIST.en.md`

- [ ] **Step 1: Create a public release allowlist**

Public candidates:

- `src/ai22b/**`
- `tests/**`
- `scripts/**`
- `apps/ai-talent-foundry/**` excluding generated `runs/**`
- `config/*.json` only if it contains no personal secrets.
- `corpus/**` only if it is public/generated sample content and not private family/voice data.
- `docs/**` excluding local logs with private paths if any.
- `README.ko.md`, `README.en.md`, `AGENTS.md`, `pyproject.toml`, `requirements-lab.txt`, `.gitignore`.

Private or unnecessary exclusions:

- `apps/**/runs/**`
- `runs/**`
- `data/private/**`
- `models/base/**`, `models/checkpoints/**`, `models/adapters/**` unless they only contain `.gitkeep`
- local voice assets, family/private documents, API keys, `.env*`, auth/session files, caches, `__pycache__`, `.pytest_cache`, `.venv`, logs, zip packages generated from local state.

- [ ] **Step 2: Verify `.gitignore` blocks generated/private outputs**

Run:

```powershell
git check-ignore apps/ai-talent-foundry/runs/shinyong_agent_release_bundle.zip
git check-ignore data/private/.gitkeep
git check-ignore runs/.gitkeep
```

Expected: generated runtime content is ignored or intentionally represented only by `.gitkeep` if needed.

- [ ] **Step 3: Scan for obvious secrets/private paths before staging**

Run:

```powershell
rg -n "OPENAI_API_KEY|api_key|auth_token|refresh_token|C:\\\\Users\\\\|C:/Users/|private-voice-assets|\\.env" .
```

Expected: no public-staged secret values. Document any intentional local-path references in docs as configuration examples only, not uploaded private assets.

- [ ] **Step 4: Korean/English README entry points**

Root `README.ko.md` should be Korean-first and link to English:

```markdown
English: [README.en.md](README.en.md)
```

Root `README.en.md` should link back:

```markdown
Korean: [README.ko.md](README.ko.md)
```

Both should explain:

- AI Talent Foundry concept.
- Dataflow Runtime.
- Local-only/privacy policy.
- Install/test/demo commands.
- What is not included in the public repo.

- [ ] **Step 5: Create a new GitHub repository after verification**

Use `gh` or GitHub connector after the code, tests, demo, doctor, and privacy scan pass.

Suggested repo name:

```text
22B-AI-Talent-Foundry
```

Do not push generated runtime outputs or private assets.

- [ ] **Step 6: Stage only selected public files**

Use explicit path staging rather than `git add .` unless `.gitignore` and `git status --ignored` have been checked carefully.

- [ ] **Step 7: Commit and push**

Run only after user approval or final release checkpoint:

```powershell
git status --short
git add <allowlisted files>
git commit -m "feat: publish AI talent foundry local agent runtime"
git remote add origin <new repo url>
git push -u origin HEAD
```

Expected: GitHub repository contains the selected program and bilingual documentation, without private/generated local data.

---

## Final Verification Checklist

- [ ] `src/ai22b/talent_foundry/dataflow_runtime.py` exists and is focused on dataflow execution.
- [ ] CLI has `run-hired-dataflow-job`.
- [ ] Installed-agent registry can run dataflow jobs from an employment record.
- [ ] Release bundle includes dataflow script and template.
- [ ] Doctor checks bundle dataflow readiness.
- [ ] Demo writes dataflow run and workspace artifacts.
- [ ] Korean and English README files explain dataflow usage.
- [ ] `docs/log.md` records the implementation and verification commands.
- [ ] Full test suite passes.
- [ ] Demo script passes.
- [ ] Doctor script passes.
- [ ] Privacy scan has no unapproved secrets or private assets.
- [ ] Root Korean README links to English README and English README links back to Korean README.
- [ ] New GitHub repository is created and contains only selected public files.

## Commit Guidance

Only commit after the full verification checklist passes and the user asks for commit/push.

Suggested commit messages if committing in small chunks:

```bash
git add docs/superpowers/specs/2026-05-30-agent-dataflow-runtime-design.md docs/superpowers/plans/2026-05-30-agent-dataflow-runtime.md
git commit -m "docs: design agent dataflow runtime"

git add src/ai22b/talent_foundry/dataflow_runtime.py tests/test_talent_foundry.py
git commit -m "feat: add dataflow runtime kernel"

git add src/ai22b/talent_foundry/registry.py src/ai22b/talent_foundry/cli.py tests/test_talent_foundry.py
git commit -m "feat: run hired dataflow jobs"

git add src/ai22b/talent_foundry/distribution.py src/ai22b/talent_foundry/demo.py apps/ai-talent-foundry/README.ko.md apps/ai-talent-foundry/README.en.md docs/log.md tests/test_talent_foundry.py
git commit -m "feat: package dataflow jobs in talent release"
```
