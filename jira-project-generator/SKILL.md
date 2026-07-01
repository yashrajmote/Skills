---
name: jira-project-generator
description: A skill for generating Jira Cloud project backlogs from project documentation, PRDs, meeting notes, UI designs, architecture plans, or early code. Use when the user wants Epics, Stories, Sub-tasks, Jira CSV imports, backlog planning, project-management task generation, Jira issue decomposition, or a cleaner non-overlapping project plan.
---

# Jira Project Generator

## Workflow

Analyze the provided project materials and extract:

- System components, including frontend or mobile apps, backend APIs, workers, databases, admin tools, infrastructure, and integrations.
- User-facing capabilities, including onboarding, dashboards, workflows, reports, settings, notifications, and admin experiences.
- Technical work, including APIs, services, validation, persistence, queues, deployment, observability, tests, and security controls.
- Data entities, relationships, lifecycle states, permissions, request/response contracts, and integration boundaries.
- Design-system needs, including reusable components, form patterns, layout primitives, states, tokens, and shared UI behavior.

Generate a small-team-friendly Jira backlog using the hierarchy:

1. Epic
2. Story
3. Sub-task

Export the third level as `Sub-task`, never `Task`.

## Required References

Read the relevant references before producing the final backlog:

- `references/jira-csv-rules.md` for Jira Cloud CSV import rules, hierarchy, headers, row ordering, statuses, and description templates.
- `references/backlog-quality.md` for no-overlap, deduplication, dependency handling, sizing, and final quality review.
- `references/epic-boundaries.md` for deciding which Epic owns ambiguous work.
- `references/story-writing.md` for writing technical, engineer-useful Story and Sub-task descriptions.

## Deliverables

Produce two outputs:

- Part A: a Jira CSV file with the exact required headers, valid parent references, useful descriptions for every row, and no duplicate or overlapping work.
- Part B: short Jira setup notes covering workflow states, issue types, labels, import mapping notes, assumptions, technical gaps, and human-review areas.

Default all statuses to `To Do` for new projects unless implementation evidence proves work is `Done` or explicitly `In Progress`. Designs, requirements, and architecture plans count as planned scope, not implementation progress.

Before finalizing, review the CSV for technical usefulness, non-overlap, specific ownership, valid hierarchy, meaningful descriptions, and small-team execution practicality. When a CSV exists, optionally run `scripts/duplicate_backlog_checker.py` to catch duplicate IDs, invalid parents, invalid hierarchy, duplicate summaries, and near-duplicate summaries.
