#!/usr/bin/env python3
"""Prepare a file-based jira-project-generator request."""

from __future__ import annotations

import argparse
from pathlib import Path


def existing_file(raw_path: str) -> Path:
    path = Path(raw_path).expanduser().resolve()
    if not path.exists():
        raise argparse.ArgumentTypeError(f"file does not exist: {path}")
    if not path.is_file():
        raise argparse.ArgumentTypeError(f"path is not a file: {path}")
    return path


def output_path(raw_path: str) -> Path:
    return Path(raw_path).expanduser().resolve()


def prompt_for_files() -> list[Path]:
    print("Enter input file paths, one per line. Submit a blank line when done.")
    paths: list[Path] = []
    while True:
        raw_path = input("Input file: ").strip()
        if not raw_path:
            break
        paths.append(existing_file(raw_path))
    return paths


def prompt_optional_path(label: str) -> Path | None:
    raw_path = input(f"{label} (blank for default): ").strip()
    return output_path(raw_path) if raw_path else None


def default_outputs(primary_input: Path) -> tuple[Path, Path]:
    return primary_input.parent / "Jira_Backlog.csv", primary_input.parent / "Jira_Setup_Notes.md"


def format_file_list(paths: list[Path]) -> str:
    return "\n".join(f"- {path}" for path in paths)


def build_request(input_files: list[Path], output_csv: Path, output_notes: Path, project_name: str | None) -> str:
    project_part = f" for {project_name}" if project_name else ""
    return (
        f"Use $jira-project-generator{project_part} with these input files:\n"
        f"{format_file_list(input_files)}\n\n"
        f"Read every input file, generate one clean non-overlapping Jira backlog, "
        f"save Part A as a Jira CSV at {output_csv}, and save Part B setup notes at {output_notes}. "
        f"After writing the CSV, run the duplicate backlog checker and fix hard validation errors."
    )


def main() -> int:
    parser = argparse.ArgumentParser(
        description=(
            "Collect project source files and print a ready-to-run request for the "
            "jira-project-generator skill."
        )
    )
    parser.add_argument("input_files", nargs="*", type=existing_file, help="Project source files to analyze")
    parser.add_argument("--interactive", action="store_true", help="Prompt for input files and output paths")
    parser.add_argument("--output-csv", type=output_path, help="Where the generated Jira CSV should be saved")
    parser.add_argument("--output-notes", type=output_path, help="Where the setup notes should be saved")
    parser.add_argument("--project-name", help="Optional project name to include in the request")
    parser.add_argument("--prompt-out", type=output_path, help="Optional file path to write the generated request")
    args = parser.parse_args()

    input_files = list(args.input_files)
    output_csv = args.output_csv
    output_notes = args.output_notes
    project_name = args.project_name

    if args.interactive or not input_files:
        if not project_name:
            entered_project_name = input("Project name (blank to skip): ").strip()
            project_name = entered_project_name or None
        if not input_files:
            input_files = prompt_for_files()
        if not input_files:
            parser.error("at least one input file is required")
        if output_csv is None:
            output_csv = prompt_optional_path("Output Jira CSV path")
        if output_notes is None:
            output_notes = prompt_optional_path("Output setup notes path")

    if not input_files:
        parser.error("at least one input file is required")

    default_csv, default_notes = default_outputs(input_files[0])
    output_csv = output_csv or default_csv
    output_notes = output_notes or default_notes

    request = build_request(input_files, output_csv, output_notes, project_name)

    if args.prompt_out:
        args.prompt_out.parent.mkdir(parents=True, exist_ok=True)
        args.prompt_out.write_text(request + "\n", encoding="utf-8")

    print(request)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
