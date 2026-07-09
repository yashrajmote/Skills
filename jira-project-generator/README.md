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
|   +-- prepare_jira_generation.py
|   +-- duplicate_backlog_checker.py
+-- assets/
    +-- sample_backlog.csv
```

The skill is mostly instruction-based. The helper scripts collect file-based generation inputs and validate generated CSVs; the AI skill performs the actual document analysis and backlog generation.

## Generate From Input Files

Use the helper to turn one or more project files into a ready-to-run skill request:

```bash
python3 scripts/prepare_jira_generation.py /path/to/project-plan.md /path/to/architecture.md
```

For an input-style flow, run:

```bash
python3 scripts/prepare_jira_generation.py --interactive
```

The helper will ask for input files and optional output paths, then print a request that tells `$jira-project-generator` where to save:

- `Jira_Backlog.csv`
- `Jira_Setup_Notes.md`

Paste the printed request into Codex or ChatGPT with this skill enabled. The AI skill performs the actual document analysis and CSV generation.

## Duplicate Checker

Run the checker against a generated Jira CSV:

```bash
python3 scripts/duplicate_backlog_checker.py Jira_Backlog.csv
```

Adjust near-duplicate sensitivity:

```bash
python3 scripts/duplicate_backlog_checker.py Jira_Backlog.csv --threshold 0.90
```
