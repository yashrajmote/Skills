# Prompt 2 — New Project Jira Template Generation

Use this prompt when starting a **new** project that has documentation, product requirements, UI designs, architecture plans, meeting notes, or early repo/config evidence but little or no completed implementation yet. The goal is to propose a clean Jira project structure, generate an importable Jira CSV, and produce a simple workflow recommendation for a small engineering team.

**All rules needed to generate the CSV are in this file; do not rely on other documents or links.**

---

## Jira CSV import checklist (mandatory)

Follow every item below so the CSV imports into Jira Cloud without mapping or hierarchy errors.

### Column headers

Use exactly these headers:

- `Summary` (required)
- `Issue type` (use this exact header so Jira maps to Issue Type)
- `Work item ID`
- `Parent`
- `Status` (optional but recommended)
- `Description` (optional)

No extra punctuation in the header row except commas. No punctuation in header names.

### Work types and hierarchy

Use **only** these values in the `Issue type` column:

- `Epic`
- `Story`
- `Sub-task`

Do not use `Task` for the third level. Jira Cloud expects `Sub-task` as the child of `Story`; using `Task` can cause invalid work type and hierarchy errors.

Hierarchy:

- Epic = level 1, top-level planning bucket.
- Story = level 0, child of Epic.
- Sub-task = level -1, child of Story.

Parent rules:

- Epic has no parent.
- Story's parent must be an Epic's `Work item ID`.
- Sub-task's parent must be a Story's `Work item ID`.

### Work item ID and Parent

- `Work item ID` must be **globally unique** across the entire CSV.
- Never reuse the same value for an Epic, Story, or Sub-task.
- Use distinct ID ranges, for example:
  - Epics: `100–199`
  - Stories: `1000–1999`
  - Sub-tasks: `10000+`
- `Parent` must equal the `Work item ID` of the parent row.
- Parent is empty for Epics.
- Every Parent value must reference an existing row's `Work item ID`.

### Row order

Order rows **by hierarchy level across the whole file**:

1. All Epic rows first.
2. All Story rows second.
3. All Sub-task rows third.

Do not group by feature in an interleaved order such as Epic A, Story A1, Sub-task A1a, Epic B. Interleaved ordering can cause Jira import errors such as incorrectly mapped values or broken hierarchy.

### CSV formatting

- Use commas as column separators.
- Enclose any field that contains a comma or newline in double quotes.
- To include a literal double quote inside a quoted field, use two double quotes: `""`.
- Put the full Description text inside double-quoted CSV fields.
- Newlines are allowed inside quoted Description fields.

---

## Structured description template (mandatory for Description column)

Populate the `Description` column for every row. Keep each section concise but specific enough for product and engineering to understand what must be delivered.

### For Epics and Stories

Use this structure in the Description field:

- **Objective** — One sentence stating the goal of this Epic or Story.
- **Context** — Brief background: why this exists, where it fits in the product, and current state if known, such as implemented, stubbed, partially implemented, or not started.
- **Scope** — **Included:** What is in scope. **Not included:** What is explicitly out of scope when needed.
- **Technical notes** — Key implementation details, expected modules, screens, endpoints, services, data entities, dependencies, or integration points.
- **Success criteria** — 2–4 measurable outcomes that define done.
- **Risks and dependencies** — Short list of blockers, design/backend dependencies, unclear requirements, or risks. Use `None` or `N/A` if none are known.
- **Other information** — Extra notes, references to wireframes/docs, assumptions, or `N/A`.

### For Sub-tasks

Use this shorter structure in the Description field:

- **Objective** — One sentence stating what this task delivers.
- **Implementation details** — Specific files, components, services, endpoints, schema changes, test cases, or configuration work expected.
- **Success criteria** — 1–3 concrete done/not-done conditions.
- **Notes** — Optional extra notes, dependencies, or `N/A`.

Put the full description text, including newlines between sections, inside double-quoted CSV fields. Escape any internal double quotes as `""`.

---

## Description quality rules (mandatory)

The generated Jira CSV must have strong, useful descriptions. Do not treat the Description column as filler. Each Description should help a product manager, engineer, designer, or QA person understand the purpose, implementation direction, and done criteria without needing to ask basic follow-up questions.

### 1. Make descriptions more complete and actionable

Every Description should explain:

- Why the work exists.
- What the work includes.
- What is explicitly out of scope when boundaries are important.
- What technical layer or component is affected.
- What must be true for the work to be considered done.
- What dependencies, risks, assumptions, or open questions exist.

Avoid shallow descriptions such as:

- Build the login feature.
- Create the dashboard.
- Add backend support.
- Implement the API.
- Write tests.

Prefer descriptions that mention the expected behavior, affected screens/components, API or data requirements, validation rules, edge cases, and acceptance criteria.

### 2. Epic descriptions

Epic descriptions should describe the full product or system area, not just repeat the Epic title. Include:

- The business or product reason this Epic exists.
- The main capabilities included under the Epic.
- The boundaries of ownership so work does not overlap with other Epics.
- Major technical systems involved.
- Key risks, dependencies, or unknowns.
- How success will be recognized at the Epic level.

### 3. Story descriptions

Story descriptions should be detailed enough that an engineer can understand the expected behavior and implementation direction. Include:

- User or system goal.
- Trigger or entry point, such as screen, user action, API call, scheduled job, webhook, or admin action.
- Expected behavior and important states.
- API, database, integration, permission, or UI implications where relevant.
- Acceptance criteria that are testable.
- Dependencies on other Stories, Epics, designs, infrastructure, or external services.

### 4. Sub-task descriptions

Sub-task descriptions should be technically concrete. Include:

- The specific implementation action.
- The expected file, component, endpoint, service, model, migration, config, test, or integration area when known.
- The exact done condition.
- Any relevant notes about dependencies or assumptions.

A Sub-task Description should not be a single vague sentence unless the task is truly trivial.

### 5. Avoid generic filler

Do not use generic filler phrases unless they are paired with concrete details. Avoid repeating the same Description structure with only the title changed. Each row should have a Description that is specific to that row's actual work.

Bad:

- Objective: Implement this feature.
- Success criteria: Feature works as expected.
- Notes: N/A.

Good:

- Objective: Implement email/password login so registered users can securely start a session.
- Implementation details: Add form validation for required email, valid email format, password presence, disabled submit state, loading state, invalid credentials error, and successful token storage.
- Success criteria: User cannot submit invalid input; invalid credentials show a clear error; successful login stores the token and navigates to the authenticated home screen.
- Notes: Depends on the backend login endpoint and agreed token response shape.

### 6. Description review

Before exporting the CSV, review every Description and improve any row that is too vague, too short, duplicated from another row, missing technical context, missing acceptance criteria, or unclear about ownership.

---

## Backlog quality rules (mandatory)

Apply these rules before generating the final CSV.

### 1. No overlapping work

Each Story and Sub-task must appear only once in the backlog. Do not duplicate the same implementation work under multiple Epics.

If work touches multiple areas, assign it to the Epic that owns the final deliverable and document the cross-Epic dependency in the Description field instead of creating a duplicate row.

Use this ownership priority when work could fit in multiple Epics:

1. User-facing feature Epic owns visible product behavior and screen-level user flows.
2. Backend/API Epic owns reusable services, endpoints, data models, validation, persistence, and server-side business logic.
3. Infrastructure/DevOps Epic owns deployment, environments, CI/CD, cloud resources, observability, and runtime configuration.
4. Design System Epic owns reusable UI components, theme tokens, typography, spacing, shared styling, and common interaction patterns.
5. Integration Epic owns third-party service connection, synchronization, provider-specific API handling, external credentials, and webhook/event ingestion.

Before finalizing the CSV, scan all Story and Sub-task summaries. Merge, rename, or remove duplicates where the work outcome is substantially the same.

### 2. Epic ownership boundaries

Before generating Stories, define the ownership boundary for every Epic.

For each Epic, determine:

- **Owns:** The type of work this Epic is responsible for.
- **Does not own:** Similar or adjacent work that belongs in another Epic.
- **Depends on:** Other Epics, APIs, designs, infrastructure, decisions, or external systems this Epic relies on.

Use these boundaries to decide where each Story belongs and to prevent duplicated Stories across Epics.

### 3. Story size and clarity

Each Story should describe one testable user or system capability.

A Story should not combine multiple unrelated capabilities. If a Story contains multiple workflows, multiple user goals, or multiple independently testable outcomes, split it into smaller Stories.

Stories should be understandable by both product and engineering. Avoid vague Story summaries such as:

- Build backend
- Implement dashboard
- Add admin functionality
- Connect API
- Create frontend

Prefer specific Story summaries such as:

- User can sign in with email and password
- Admin can invite a team member by email
- System persists translated chat messages after successful AWS Translate response
- User can filter alerts by location and severity

### 4. Sub-task specificity

Each Sub-task must be a concrete implementation action with a clear done/not-done outcome.

Avoid vague repeated Sub-tasks such as:

- Implement backend logic
- Create frontend UI
- Add tests
- Update documentation
- Connect API

Instead, make each Sub-task specific to its parent Story outcome.

Good examples:

- Implement `POST /api/auth/login` request validation and response handling
- Create login form validation for email and password fields
- Add integration test for invalid login credentials
- Add database migration for `team_members` table
- Wire `ConversationWebSocketClient` reconnect handling into chat screen lifecycle

Bad examples:

- Implement API
- Build UI
- Add tests
- Update docs
- Finish backend

### 5. Dependency handling

Do not duplicate dependent work.

If one Story depends on another Epic, API, design, integration, or infrastructure task, mention that dependency in the Description field under `Risks and dependencies` instead of creating the same work item again.

Example:

- Do not create `Set up AWS Translate` under both `Chat Translation` and `Infrastructure`.
- Put the AWS setup work under the owning Infrastructure or Integration Epic.
- In the Chat Translation Story, list `Depends on AWS Translate client configuration and IAM permissions` under Risks and dependencies.

### 6. Backlog review before CSV export

Before writing the final CSV, perform a backlog quality review:

1. Check for duplicate or near-duplicate Stories across Epics.
2. Check for duplicate or near-duplicate Sub-tasks across Stories.
3. Check that every Sub-task produces a concrete implementation outcome.
4. Check that every Story has a clear parent Epic and does not span multiple Epics.
5. Check that dependencies are documented in Description instead of duplicated as separate work items.
6. Check that each row can be understood without reading another row.
7. Check that each Description includes useful technical detail instead of generic filler.
8. Check that the final backlog is suitable for a small engineering team and does not introduce unnecessary process ceremony.

Only export the CSV after this review is complete.

---

## Technical depth rules (mandatory)

The generated Jira backlog should not be only product-level. It should contain enough technical implementation detail to help engineers execute without repeatedly guessing what the task means.

### 1. Extract technical architecture from all available inputs

When analyzing the provided documentation, identify and use technical details such as:

- Application layers, such as mobile app, web app, backend API, worker service, database, queue, storage, admin console, or third-party provider.
- Frameworks, languages, and libraries, such as Flutter, React, Spring Boot, Node.js, PostgreSQL, Redis, AWS, Firebase, Stripe, Twilio, or other named tools.
- API endpoints, methods, payloads, authentication requirements, error responses, and service boundaries.
- Data entities, relationships, status fields, lifecycle states, permissions, and ownership rules.
- Infrastructure components, including environments, secrets, logging, monitoring, deployment, CI/CD, queues, cron jobs, and cloud services.
- Security requirements, including roles, access control, token validation, audit logs, PII handling, rate limits, and permission boundaries.
- Testing needs, including unit tests, integration tests, contract tests, end-to-end tests, seed data, mock services, and manual QA checks.

If the documentation does not specify a technical detail, make a conservative assumption only when needed and clearly mark it as an assumption in the Description field.

### 2. Make technical ownership explicit

Every technical Story should clearly identify the owning layer.

Examples:

- Frontend/mobile Story: screen, route, component, state, validation, API adapter, loading/error/empty states.
- Backend Story: endpoint, service method, validation, authorization, database model, migration, response contract, tests.
- Infrastructure Story: environment, deployment target, IAM/policy, monitoring, logs, secrets, alarms, rollback notes.
- Integration Story: provider API, credentials, request/response mapping, retries, failure handling, rate limits, observability.
- Data Story: entity, fields, relationships, migration, indexes, seed data, constraints, retention, audit requirements.

### 3. Include technical details in Sub-tasks

Sub-tasks should be more technically specific than Stories.

A good Sub-task should usually mention at least one of the following:

- Screen, component, route, widget, or view name.
- Endpoint, service method, worker, adapter, repository, or controller.
- Database table, migration, model, DTO, schema, enum, or index.
- Config file, environment variable, IAM policy, queue, topic, bucket, function, or deployment setting.
- Test file, test type, mocked dependency, expected scenario, or acceptance check.

### 4. Include edge cases and non-happy paths

For each important user-facing or system-facing capability, include tasks or success criteria for relevant edge cases, such as:

- Loading, empty, success, validation, unauthorized, forbidden, not found, timeout, retry, offline, and server-error states.
- Duplicate submissions, idempotency, pagination, sorting, filtering, stale data, race conditions, and partial failures.
- Permission boundaries, role-specific visibility, expired sessions, missing tokens, invalid payloads, and deleted resources.
- External provider failures, rate limits, retries, dead-letter queues, webhook replay, and data normalization errors.

Do not add edge-case tasks that are unrelated to the documented scope, but do include obvious technical failure modes for the selected architecture.

### 5. Include testability in implementation work

Where appropriate, include Sub-tasks for testing. Testing Sub-tasks should be specific, not generic.

Good examples:

- Add controller integration tests for `POST /api/auth/login` success, invalid password, and missing email cases
- Add widget test for login form disabled submit state and validation messages
- Add repository test for retry behavior when AWS Translate returns a transient error
- Add migration test or startup validation for required database schema

Bad examples:

- Add tests
- Test feature
- QA everything

---

## Task

Analyze project **documentation** and optionally early code or config, then produce a **Jira project template** as a **separate CSV file** plus setup notes.

Plan in Epic → Story → Task terms, but export the third level as **Sub-task** in the CSV.

The CSV must be importable into Jira Cloud without hierarchy or mapping errors. Apply the Jira CSV import checklist, Structured description template, Backlog quality rules, and Technical depth rules exactly.

The result should be simple, technically useful, and suitable for a small engineering team.

---

## Input you will receive

Possible inputs include:

- Product requirements, MVP requirements, PRDs, technical approach docs, service/API design docs, data types, or integration specs.
- Meeting transcripts, discovery notes, stakeholder notes, and call summaries.
- UI/UX designs, Figma exports, wireframes, architecture diagrams, or early repo structure.
- Early code, config files, package manifests, dependency files, database migrations, or infrastructure notes.

---

## Process

### 1. Analyze the documentation

Extract:

- System components, such as mobile app, web app, backend API, workers, queues, database, admin console, external services, design system, and infrastructure.
- User-facing capabilities, such as onboarding, login, dashboard, feed, chat, alerts, details, reporting, map, profile, settings, notifications, and admin workflows.
- System-facing or technical work, such as auth service, API endpoints, integrations, background jobs, push notifications, deployment, monitoring, and data persistence.
- Data entities and APIs, including endpoints, payloads, auth requirements, permissions, validation, lifecycle states, and relationships.
- Infrastructure and DevOps needs, such as hosting, CI/CD, environments, secrets, logging, monitoring, queues, cloud services, and database setup.
- Planned scope from transcripts, stakeholder notes, architecture diagrams, and wireframes even if not yet implemented.

### 2. Propose Epics

Define Epics for major system areas.

Examples:

- Authentication & Onboarding
- Core Product Experience
- Dashboard & Feed
- Detail & Reporting
- Chat & Messaging
- Map & Location
- Profile & Notifications
- Backend Services & APIs
- Design System & Shared UI
- Integrations & External Data
- Infrastructure & DevOps
- Admin & Internal Tools

Keep Epics manageable. Each Epic must be a clear bucket of related work with a defined ownership boundary.

### 3. Define Epic boundaries

Before generating Stories, define each Epic's ownership boundary:

- What this Epic owns.
- What this Epic does not own.
- Which other Epics or systems it depends on.

Use these boundaries to prevent overlapping Stories and Sub-tasks.

### 4. Propose Stories

Under each Epic, define Stories that represent user or system functionality.

Stories should be:

- Testable.
- Understandable by both product and engineering.
- Owned by one Epic only.
- Specific enough to imply implementation work.
- Small enough to represent one capability or workflow.

Example Story patterns:

- User can sign up and verify email.
- User can view a filtered list of safety alerts.
- System fetches and normalizes weather alerts from NWS API.
- Admin can invite a team member by email.
- Backend persists translated messages with source and target language metadata.

### 5. Propose Tasks

Under each Story, define implementation Tasks and export them as `Sub-task` rows in the CSV.

Sub-tasks should be:

- Binary: clearly done or not done.
- Small enough to assign to one engineer.
- Specific to the parent Story.
- Technically meaningful.
- Non-duplicative across Stories.

Example Sub-task patterns:

- Implement login screen UI with email/password validation.
- Add `POST /api/auth/login` endpoint and response DTO.
- Add database migration for `users` table indexes.
- Wire frontend API adapter to login endpoint.
- Add integration tests for valid login, invalid credentials, and missing token.
- Configure CloudWatch alarm for queue message age.

### 6. Descriptions and acceptance criteria

For the CSV Description column, use the Structured description template above.

For Epics and Stories, include:

- Objective
- Context
- Scope
- Technical notes
- Success criteria
- Risks and dependencies
- Other information

For Sub-tasks, include:

- Objective
- Implementation details
- Success criteria
- Notes

Success criteria serve as acceptance criteria. Make them concrete enough to verify.

### 7. Implementation state

Assign statuses from evidence:

- Sub-task: `Done` or `To Do`.
- Story/Epic: `Done`, `In Progress`, or `To Do`.

For new projects, default all rows to `To Do` unless implementation evidence exists in code, config, commits, screenshots of completed functionality, or explicit progress notes.

Designs, requirements, architecture plans, and transcripts count as planned scope, not implementation progress.

### 8. Jira project setup notes

For Part B, recommend:

- A simple board workflow, usually `To Do → In Progress → Done`.
- Issue types: Epic, Story, Sub-task.
- Suggested labels and how to use them.
- Any import mapping notes needed for Jira Cloud.
- Any assumptions made while generating the backlog.
- Any technical gaps or open questions discovered in the source material.

---

## Build the CSV (Part A)

Create and save a separate CSV file, for example `Jira_Backlog.csv`, typically under `Documentation/`.

CSV requirements:

- Headers: exactly `Summary`, `Issue type`, `Work item ID`, `Parent`, `Status`, `Description`.
- Work types: only `Epic`, `Story`, `Sub-task`.
- Work item ID: globally unique.
- Parent: empty for Epics, Epic ID for Stories, Story ID for Sub-tasks.
- Row order: all Epic rows first, then all Story rows, then all Sub-task rows.
- Formatting: commas as separators; quote fields with commas or newlines; escape `"` as `""`.
- Descriptions: every row must have a Description using the required structure.
- No duplicate Stories or Sub-tasks.
- No overlapping implementation work across Epics.
- The file must import into Jira Cloud without mapping or hierarchy errors.

---

## Deliverable

Produce two outputs.

### Part A — Jira CSV file

A separate CSV file conforming to the checklist and template in this prompt, with:

- Epics
- Stories
- Sub-tasks
- Structured descriptions
- Valid hierarchy
- Valid parent references
- Valid statuses
- No duplicate or overlapping work items

### Part B — Setup notes

A short markdown note that includes:

- Recommended Jira workflow columns/states.
- Recommended issue types.
- Suggested labels and brief usage notes.
- CSV import mapping notes.
- Assumptions made.
- Technical gaps or open questions found in the source material.
- Any areas where the generated backlog may need human review before execution.
