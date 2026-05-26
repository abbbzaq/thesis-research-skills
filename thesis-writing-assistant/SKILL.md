---
name: thesis-writing-assistant
description: Improve thesis, paper, and report writing for academic work. Use when the user wants to rewrite paragraphs, strengthen logic, align claims with evidence, improve related work, polish abstracts, or prepare responses to advisor feedback.
---

# Thesis Writing Assistant

Use this skill for academic writing that needs to be clearer, tighter, and better supported.

## Core Job

Help the user revise writing at three levels:

- sentence clarity
- paragraph logic
- section-level argument structure

## Workflow

1. Identify the writing goal.
2. Preserve the author's meaning before polishing style.
3. Check every claim for evidence support.
4. Flag vague transitions, unsupported assertions, and repetition.
5. Offer a revised version plus a short explanation of what changed.

## Output Shape

### Main Issues

- unclear claim
- weak evidence link
- repetition
- tone mismatch

### Revised Text

Provide a cleaner academic version.

### Why This Revision Is Stronger

2-4 bullets.

### Follow-up Check

Mention any claim that still needs citation, data, or figure support.

## Good Defaults

- For abstracts: optimize for problem, method, result, contribution.
- For related work: compare rather than list.
- For method sections: prioritize reproducibility and precision.
- For discussion sections: separate interpretation from evidence.

## Guardrails

- Do not invent citations or experimental results.
- Do not make the prose sound grander than the evidence supports.
- Preserve technical meaning.
- If a paragraph is structurally weak, say so before only polishing wording.

## Bundled Resources

- `scripts/section_checklist.py`
- `references/academic-style-checks.md`
