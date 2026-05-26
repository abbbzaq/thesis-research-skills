# Thesis Research Skills

Practical Codex skills for graduate research workflows.

This repository collects four high-frequency skills designed for day-to-day academic work, especially for master's and PhD students who repeatedly need help with:

- reading and comparing papers
- turning rough ideas into executable research plans
- revising thesis and paper writing
- organizing experiment logs for reports and ablations

## Included Skills

### 1. `paper-reading-matrix`

Use this skill to turn one or more papers into structured reading notes or a comparison matrix.

Best for:

- literature review
- related work preparation
- method comparison
- deciding whether a paper is worth deep reading

Typical output:

- problem
- method
- dataset
- metrics
- results
- limitations
- relevance to your topic

### 2. `research-plan-refiner`

Use this skill to turn a vague topic into a concrete study plan.

Best for:

- proposal preparation
- advisor discussion
- narrowing a topic
- designing a first experiment

Typical output:

- research question
- hypothesis
- baselines
- metrics
- risks
- next 7 days

### 3. `thesis-writing-assistant`

Use this skill to improve thesis, paper, abstract, and report writing.

Best for:

- rewriting unclear paragraphs
- improving related work structure
- checking whether claims match evidence
- polishing academic tone without exaggeration

Typical output:

- main issues
- revised text
- why the revision is stronger
- claims that still need support

### 4. `experiment-log-organizer`

Use this skill to convert scattered experiment notes into structured logs.

Best for:

- weekly reports
- ablation tracking
- failed-run analysis
- reproducible experiment records

Typical output:

- experiment goal
- setup
- changed variable
- results
- interpretation
- next step

## Who This Repository Is For

This repository is especially useful for:

- graduate students
- research assistants
- students preparing proposals or theses
- anyone using Codex to support academic research workflows

## Repository Structure

Each skill is packaged as its own folder and typically includes:

- `SKILL.md`
- `agents/openai.yaml`
- `assets/`
- `references/`
- `scripts/`

## Quick Start

Pick the skill that matches your current task:

- reading papers -> `paper-reading-matrix`
- refining a topic -> `research-plan-refiner`
- revising writing -> `thesis-writing-assistant`
- organizing experiment logs -> `experiment-log-organizer`

## Design Principles

These skills were written with a few practical principles:

- optimize for high-frequency research tasks
- keep outputs structured and reusable
- separate evidence from interpretation
- avoid inflated academic wording
- support iteration across multiple research sessions

## Notes

This repository focuses on practical academic workflows rather than software engineering workflows.

The goal is not to replace deep research judgment, but to reduce repetitive organizational and writing overhead so more time can go to actual thinking and experimentation.
