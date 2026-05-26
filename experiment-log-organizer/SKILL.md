---
name: experiment-log-organizer
description: Organize research experiments into reusable structured logs. Use when the user wants to整理实验记录, compare experiment variants, summarize failure causes, prepare weekly reports, review ablations, or turn scattered results into a consistent experiment log.
---

# Experiment Log Organizer

Use this skill when the user has scattered experiment notes and needs a clean record they can reuse for reports, papers, or future runs.

## Core Job

Turn raw experiment information into a structured log with:

- experiment goal
- setup and configuration
- dataset or split
- model or method version
- metrics
- key results
- failure cases
- interpretation
- next action

## Workflow

1. Identify what changed in this experiment.
2. Separate setup from outcome.
3. Record both successful and failed runs.
4. Highlight what was learned, not only what was measured.
5. End with one recommended next step.

## Good Defaults

- For a single run: create one structured log.
- For multiple runs: create a comparison summary first, then individual logs if needed.
- For ablations: explicitly state the changed variable and what stayed fixed.

## Output Shape

### Experiment ID

A short label such as `exp-2026-05-26-rag-topk10`.

### Goal

One sentence.

### Setup

- data
- model
- parameters
- hardware or environment when relevant

### Results

- main metrics
- observed behavior
- unexpected outcomes

### Interpretation

What this run suggests.

### Next Step

One concrete follow-up.

## Guardrails

- Do not hide failed experiments.
- Distinguish observed results from interpretation.
- Record the changed variable clearly.
- If the evidence is incomplete, say what is missing.

## Bundled Resources

- `scripts/make_log_template.py`
- `references/log-checklist.md`
