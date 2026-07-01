# Jira CSV Rules

Use these rules when creating Jira Cloud CSV imports.

## Required Headers

Use this exact header row:

```csv
Summary,Issue type,Work item ID,Parent,Status,Description
```

Do not add, rename, or punctuate header names.

## Issue Types

Use only these issue types:

- `Epic`
- `Story`
- `Sub-task`

Do not use `Task` as the third level.

## Hierarchy

- Epic has no parent.
- Story parent must be the Epic `Work item ID`.
- Sub-task parent must be the Story `Work item ID`.
- Parent values must reference an existing `Work item ID`.

## Work Item IDs

- `Work item ID` must be globally unique across the entire CSV.
- Use separate ID ranges:
  - Epics: `100-199`
  - Stories: `1000-9999`
  - Sub-tasks: `10000+`

## Row Order

Order rows by hierarchy level across the whole file:

1. All Epics first.
2. All Stories second.
3. All Sub-tasks third.

Do not interleave Epic, Story, and Sub-task rows.

## CSV Formatting

- Use comma separators.
- Quote fields containing commas or newlines.
- Escape double quotes as two double quotes.
- Populate `Description` for every row.

## Status Rules

- Default `Status` to `To Do` unless there is clear implementation evidence.
- Use `Done` only when code, configuration, or documentation proves the work is already completed.
- Use `In Progress` only when there is explicit evidence of partial implementation.

## Description Templates

Descriptions must be useful to engineers, not just product summaries. Include concrete behavior, technical ownership, acceptance criteria, dependencies, and assumptions where relevant.

For Epics and Stories:

```text
Objective -
Context -
Scope -
Success criteria -
Risks and dependencies -
Other information -
```

For Sub-tasks:

```text
Objective -
Success criteria -
Notes -
```
