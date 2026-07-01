# Jira Project Generator

This skill generates clean Jira Cloud project backlogs from project documentation, PRDs, meeting notes, UI designs, architecture plans, or early repo structure.

Use it when a project needs Epics, Stories, Sub-tasks, an importable Jira CSV, setup notes, or a cleaner non-overlapping project plan.

## Folder Structure

```text
jira-project-generator/
+-- SKILL.md
+-- agents/
|   +-- openai.yaml
+-- references/
|   +-- jira-csv-rules.md
|   +-- backlog-quality.md
|   +-- epic-boundaries.md
|   +-- story-writing.md
+-- scripts/
|   +-- duplicate_backlog_checker.py
+-- assets/
    +-- sample_backlog.csv
```

The skill is mostly instruction-based. The Python script is optional and only supports CSV validation, duplicate detection, and near-duplicate summary checks.

## Duplicate Checker

Run the checker against a generated Jira CSV:

```bash
python3 scripts/duplicate_backlog_checker.py Jira_Backlog.csv
```

Adjust near-duplicate sensitivity:

```bash
python3 scripts/duplicate_backlog_checker.py Jira_Backlog.csv --threshold 0.90
```
