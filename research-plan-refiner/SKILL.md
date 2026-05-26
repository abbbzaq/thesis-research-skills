---
name: research-plan-refiner
description: Turn a rough research idea into a concrete study plan. Use when the user wants to refine a topic, form research questions, design experiments, define baselines, or prepare for advisor discussion, proposal writing, or project kickoff.
---

# Research Plan Refiner

Use this skill when the user has an idea but not yet a solid research plan.

## Core Job

Convert a vague topic into a plan with:

- problem statement
- research question
- hypothesis
- method outline
- baselines
- evaluation plan
- risks and fallback options

## Workflow

1. Clarify the intended contribution.
2. Narrow the question until it is testable.
3. Define what evidence would support or reject the hypothesis.
4. List the smallest viable experiment first.
5. Add risks, assumptions, and backup plans.

## Output Shape

### Topic

One sentence.

### Research Question

One or two testable questions.

### Hypothesis

Expected result and why it may hold.

### Study Design

- inputs
- method
- baselines
- metrics
- ablations

### Risk Register

- data risk
- method risk
- evaluation risk
- timeline risk

### Next 7 Days

Concrete tasks the student can do now.

## Guardrails

- Avoid turning every idea into an overlarge thesis.
- Prefer falsifiable questions over broad ambition.
- Distinguish novelty from convenience.
- If the idea is weak, say so kindly and suggest a narrower angle.

## Bundled Resources

- `scripts/plan_template.py`
- `references/research-plan-checklist.md`
