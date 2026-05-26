---
name: paper-reading-matrix
description: Build fast, comparable reading notes for academic papers. Use when the user wants to read papers, compare methods, summarize related work, extract datasets or metrics, or prepare a literature review table.
---

# Paper Reading Matrix

Use this skill when the user is reading papers and needs structured notes instead of loose summaries.

## Core Job

Turn one or more papers into a comparison matrix with fields such as:

- research problem
- core idea
- method
- dataset
- metrics
- main results
- limitations
- usefulness for the current project

## Workflow

1. Identify the reading goal.
2. Extract only the details needed for that goal.
3. Normalize terminology across papers so rows are comparable.
4. Separate author claims from your own judgment.
5. End with a short "takeaway for my research" block.

## Good Defaults

- For 1 paper: produce a concise structured reading note.
- For 2-6 papers: produce a matrix.
- For more than 6 papers: cluster by theme first, then compare inside each cluster.

## Output Shape

### Reading Goal

One sentence.

### Comparison Matrix

Use a Markdown table when practical.

### Cross-paper Insights

- agreements
- differences
- open gaps

### Relevance To Current Research

2-5 bullets tied to the user's topic.

## Guardrails

- Do not mix quoted results with guessed results.
- Mark uncertainty clearly when a field is missing.
- Do not over-summarize methods into vague phrases.
- Prefer comparable units for metrics and datasets.

## Bundled Resources

- `scripts/build_matrix.py`
- `references/matrix-fields.md`
