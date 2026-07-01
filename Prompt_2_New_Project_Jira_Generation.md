# Prompt 2 — New Project Jira Template Generation

Use this prompt when starting a **new** project that has documentation, product requirements, UI designs, or architecture plans but little or no code yet. The goal is to propose a clean Jira project structure and simple workflow. **All rules needed to generate the CSV are in this file; do not rely on other documents or links.**

---

## Jira CSV import checklist (mandatory)

Follow every item below so the CSV imports into Jira Cloud without mapping or hierarchy errors.

**Column headers (use exactly):**
- `Summary` (required)
- `Issue type` (use this exact header so Jira maps to Issue Type)
- `Work item ID`
- `Parent`
- `Status` (optional but recommended)
- `Description` (optional)

No extra punctuation in the header row except commas. No punctuation in header names.

**Work types and hierarchy:**
- Use **only** these values in the `Issue type` column: **Epic**, **Story**, **Sub-task**. Do not use "Task" for the third level. Jira Cloud expects Sub-task as the child of Story; using "Task" causes "Invalid work type" and hierarchy errors.
- Epic = level 1 (top). Story = level 0 (child of Epic). Sub-task = level -1 (child of Story).
- Epic has no parent. Story's parent must be an Epic's Work item ID. Sub-task's parent must be a Story's Work item ID.

**Work item ID and Parent:**
- Work item ID must be **globally unique** across the entire CSV. Never reuse the same value for an Epic and a Story (e.g. do not use `10` for both). Use distinct ID ranges (e.g. Epics 100–199, Stories 1000–1999, Sub-tasks 10000+).
- Parent = Work item ID of the parent row. Empty for Epics. For Stories, Parent = the Epic's Work item ID. For Sub-tasks, Parent = the Story's Work item ID. Every Parent must reference an existing row's Work item ID.

**Row order:**
- Order rows **by hierarchy level across the whole file**: all **Epic** rows first, then all **Story** rows, then all **Sub-task** rows. Do not group by feature (e.g. Epic A, Story A1, Sub-task A1a, Epic B, …). Interleaved ordering causes Jira to show "values are incorrectly mapped" or "breaking the existing hierarchy."

**CSV formatting:**
- Use commas as column separators. Enclose any field that contains a comma or newline in double quotes. To include a literal double quote inside a quoted field, use two double quotes `""`.

---

## Structured description template (mandatory for Description column)

Populate the **Description** column for every row. Keep each section concise (1–3 bullets or short sentences).

**For Epics and Stories**, use this structure in the Description field (plain text with clear headings; newlines allowed inside the quoted CSV field):
- **Objective** — One sentence stating the goal of this Epic or Story.
- **Context** — Brief background: why this exists, where it fits in the product, and (if known) current state (e.g. implemented, stubbed, or not started).
- **Scope** — **Included:** What is in scope. **Not included:** What is explicitly out of scope (optional; omit if obvious).
- **Success criteria** — 2–4 measurable outcomes that define "done" (e.g. "User can submit a case from the Saved tab," "Report payload is sent to POST /api/reports").
- **Risks and dependencies** — Short list of blockers, design/backend dependencies, or risks (or "None" / "N/A" if none).
- **Other information** — Any extra notes, references to wireframes/docs, or N/A.

**For Sub-tasks**, use this shorter form:
- **Objective** — One sentence: what this task delivers.
- **Success criteria** — 1–3 concrete conditions (e.g. "Bearer token is sent on all /api/* requests," "Filter sheet applies state/city/type to feed query").
- **Notes** — Optional: file/component names, API contract, or N/A.

Put the full description text (including newlines between sections) inside double-quoted CSV fields. Escape any internal double quotes as `""`.

---

## Task

Analyze project **documentation** (and optionally early code or config) and produce a **Jira project template** as a **separate CSV file** plus setup notes. Plan in Epic → Story → Task terms, but export the third level as **Sub-task** in the CSV. The CSV must be importable into Jira Cloud without hierarchy or mapping errors. Apply the **Jira CSV import checklist** and the **Structured description template** above exactly. The result should be simple and suitable for a small engineering team.

**Input you will receive:**
- Documentation: product requirements (e.g. MVP requirements, PRD), technical approach or scope, service/API design docs, data types or integration specs
- Meeting transcripts, discovery notes, stakeholder notes, call summaries
- UI/UX designs (e.g. Figma exports, wireframes), architecture diagrams, or early repo structure

**Process:**

1. **Analyze the documentation**
   - Extract system components (e.g. mobile app, backend API, external data sources, design system).
   - Identify user-facing capabilities (e.g. onboarding, login, main dashboard, alerts feed, detail screens, reporting, map, profile).
   - Identify system-facing or technical work (e.g. auth service, feed API, integrations, push notifications).
   - List data entities and APIs (endpoints, payloads, auth) and any infrastructure (hosting, CI/CD, environments).
   - Extract planned scope from meeting transcripts and wireframes even if not yet implemented.

2. **Propose Epics**
   - Define Epics for major system areas. Examples: "Authentication & Onboarding", "Core Feed & Alerts", "Detail & Reporting", "Map & Location", "Profile & Notifications", "Backend Services & APIs", "Design System & UI", "Integrations & External Data", "Infrastructure & DevOps".
   - Keep Epics manageable (e.g. 6–12). Each Epic is a clear bucket of related work. Epics should reflect the intended product/system from the combined sources.

3. **Propose Stories**
   - Under each Epic, define Stories that represent user or system functionality (e.g. "User can sign up and verify email", "User can view a filtered list of safety alerts", "System fetches and normalizes weather alerts from NWS API").
   - Stories should be testable and understandable by both product and engineering.

4. **Propose Tasks**
   - Under each Story, define Tasks that represent implementation work (e.g. "Implement login screen UI", "Add POST /api/auth/login endpoint", "Implement FeedFilter and wire to repository").
   - Tasks should be binary: clearly "Done" or "Not Done". Prefer small, assignable units. Export the lowest level as **Sub-task** in the CSV.

5. **Descriptions and acceptance criteria**
   - For the CSV Description column, use the Structured description template above: full template (Objective, Context, Scope, Success criteria, Risks and dependencies, Other) for Epics and Stories; short form (Objective, Success criteria, Notes) for Sub-tasks.
   - Success criteria in the template serve as acceptance criteria; add 1–3 concrete conditions per Story or Sub-task where it removes ambiguity.

6. **Implementation state**
   - Assign statuses from evidence: Task/Sub-task: `Done` or `To Do`; Story/Epic: `Done`, `In Progress`, or `To Do`. If a feature is in wireframes or transcripts but not implemented, set `To Do`.

7. **Jira project setup (for Part B)**
   - Recommend a simple board workflow (e.g. To Do → In Progress → Done). Keep states minimal (3–5).
   - In the CSV use Epic, Story, Sub-task. Suggest labels (e.g. frontend, backend, api, design-system, integration, infrastructure, mvp) and how to use them.

**Build the CSV (Part A):**
- Create and save a separate CSV file (e.g. `Jira_Backlog.csv`), typically under `Documentation/`.
- **Headers:** Exactly `Summary`, `Issue type`, `Work item ID`, `Parent`, `Status`, `Description`.
- **Work types:** Only Epic, Story, Sub-task. **Work item ID:** Globally unique (e.g. Epics 100–199, Stories 1000+, Sub-tasks 10000+). **Parent:** Empty for Epics; for Stories the parent Epic ID; for Sub-tasks the parent Story ID.
- **Row order:** All Epic rows first, then all Story rows, then all Sub-task rows.
- **Formatting:** Commas as separators; quote fields with commas or newlines; escape `"` as `""`.
- **Descriptions:** For every row, fill Description using the Structured description template above (full for Epics/Stories, short for Sub-tasks).
- The file must import into Jira Cloud without mapping or hierarchy errors.

**Constraints:**
- Use Sub-task in the CSV for the third level. No scope beyond what is described in the provided documentation, transcripts, designs, or config.
- Focus on clarity and visibility of engineering work; no heavy Agile ceremony.

**Deliverable:**
- **Part A:** A separate CSV file conforming to the checklist and template in this prompt (Summary, Issue type, Work item ID, Parent, Status, Description), with Epics, Stories, and Sub-tasks and structured descriptions.
- **Part B:** Short recommendations for Jira workflow (columns/states), issue types (Epic, Story, Sub-task), and suggested labels with brief usage notes.
