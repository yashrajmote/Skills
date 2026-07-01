#!/usr/bin/env python3
"""Validate Jira backlog CSV hierarchy and flag duplicate summaries."""

from __future__ import annotations

import argparse
import csv
import sys
from collections import Counter, defaultdict
from difflib import SequenceMatcher
from pathlib import Path


REQUIRED_HEADERS = [
    "Summary",
    "Issue type",
    "Work item ID",
    "Parent",
    "Status",
    "Description",
]
VALID_ISSUE_TYPES = {"Epic", "Story", "Sub-task"}


def normalize(value: str) -> str:
    return " ".join(value.casefold().split())


def similarity(left: str, right: str) -> float:
    return SequenceMatcher(None, normalize(left), normalize(right)).ratio()


def read_rows(path: Path) -> tuple[list[dict[str, str]], list[str]]:
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        headers = reader.fieldnames or []
        rows = list(reader)
    return rows, headers


def validate(rows: list[dict[str, str]], headers: list[str], threshold: float) -> tuple[list[str], list[str], list[str]]:
    errors: list[str] = []
    warnings: list[str] = []
    near_duplicates: list[str] = []

    missing_headers = [header for header in REQUIRED_HEADERS if header not in headers]
    if missing_headers:
        errors.append(f"Missing required headers: {', '.join(missing_headers)}")
        return errors, warnings, near_duplicates

    ids = [row["Work item ID"].strip() for row in rows]
    id_counts = Counter(item_id for item_id in ids if item_id)
    for item_id, count in sorted(id_counts.items()):
        if count > 1:
            errors.append(f"Duplicate Work item ID: {item_id} appears {count} times")

    by_id: dict[str, dict[str, str]] = {}
    for row in rows:
        item_id = row["Work item ID"].strip()
        if item_id and item_id not in by_id:
            by_id[item_id] = row

    for index, row in enumerate(rows, start=2):
        summary = row["Summary"].strip() or f"row {index}"
        issue_type = row["Issue type"].strip()
        item_id = row["Work item ID"].strip()
        parent_id = row["Parent"].strip()

        if issue_type not in VALID_ISSUE_TYPES:
            errors.append(f"{summary}: invalid issue type {issue_type!r}")

        if not item_id:
            errors.append(f"{summary}: missing Work item ID")

        parent = by_id.get(parent_id) if parent_id else None

        if issue_type == "Epic" and parent_id:
            errors.append(f"{summary}: Epic should not have a Parent")
        elif issue_type == "Story":
            if not parent_id:
                errors.append(f"{summary}: Story must have an Epic parent")
            elif parent is None:
                errors.append(f"{summary}: Parent {parent_id} does not exist")
            elif parent["Issue type"].strip() != "Epic":
                errors.append(f"{summary}: Story parent {parent_id} is not an Epic")
        elif issue_type == "Sub-task":
            if not parent_id:
                errors.append(f"{summary}: Sub-task must have a Story parent")
            elif parent is None:
                errors.append(f"{summary}: Parent {parent_id} does not exist")
            elif parent["Issue type"].strip() != "Story":
                errors.append(f"{summary}: Sub-task parent {parent_id} is not a Story")

    summaries_by_type: dict[str, list[tuple[int, str]]] = defaultdict(list)
    for index, row in enumerate(rows, start=2):
        issue_type = row["Issue type"].strip()
        if issue_type in {"Story", "Sub-task"}:
            summaries_by_type[issue_type].append((index, row["Summary"].strip()))

    for issue_type, summaries in summaries_by_type.items():
        normalized_counts = Counter(normalize(summary) for _, summary in summaries if summary)
        for normalized_summary, count in sorted(normalized_counts.items()):
            if count > 1:
                warnings.append(f"Duplicate {issue_type} summary: {normalized_summary!r} appears {count} times")

        for left_index, (left_row, left_summary) in enumerate(summaries):
            if not left_summary:
                continue
            for right_row, right_summary in summaries[left_index + 1 :]:
                if not right_summary:
                    continue
                if normalize(left_summary) == normalize(right_summary):
                    continue
                score = similarity(left_summary, right_summary)
                if score >= threshold:
                    near_duplicates.append(
                        f"{issue_type} rows {left_row} and {right_row}: {score:.2f} similarity "
                        f"({left_summary!r} vs {right_summary!r})"
                    )

    return errors, warnings, near_duplicates


def print_section(title: str, items: list[str]) -> None:
    print(f"\n{title}")
    if items:
        for item in items:
            print(f"- {item}")
    else:
        print("- None")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Check a Jira backlog CSV for hierarchy and duplicate issues.")
    parser.add_argument("csv_path", type=Path, help="Path to the Jira CSV file")
    parser.add_argument("--threshold", type=float, default=0.86, help="Near-duplicate similarity threshold")
    args = parser.parse_args(argv)

    if not 0 < args.threshold <= 1:
        print("ERROR: --threshold must be greater than 0 and less than or equal to 1", file=sys.stderr)
        return 1

    try:
        rows, headers = read_rows(args.csv_path)
    except FileNotFoundError:
        print(f"ERROR: file not found: {args.csv_path}", file=sys.stderr)
        return 1
    except csv.Error as exc:
        print(f"ERROR: CSV parse error: {exc}", file=sys.stderr)
        return 1

    errors, warnings, near_duplicates = validate(rows, headers, args.threshold)

    print(f"Checked {len(rows)} rows in {args.csv_path}")
    print_section("Errors", errors)
    print_section("Warnings", warnings)
    print_section("Possible near duplicates", near_duplicates)

    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
