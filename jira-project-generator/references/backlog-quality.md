# Backlog Quality

Apply these checks before exporting the final Jira CSV.

## No-Overlap Rule

- Each Story and Sub-task must appear only once.
- Do not duplicate the same implementation work under multiple Epics.
- If work touches multiple areas, assign it to the Epic that owns the final deliverable.
- Mention related work as dependencies instead of creating duplicate issues.

## Deduplication Pass

Before final CSV export, check for:

- Duplicate Story summaries.
- Duplicate Sub-task summaries.
- Semantically similar work items.
- Vague repeated items.
- Unclear ownership.
- Work that belongs under a different Epic.
- Stories that are too broad.
- Sub-tasks that are not binary done/not-done.

## Dependency Handling

- Do not duplicate dependency work.
- Use the `Description` field to mention dependencies.
- Example: a frontend Story may depend on a backend API Story, but should not duplicate backend implementation tasks.

## Story Sizing

- A Story should represent one testable user or system capability.
- If a Story requires many unrelated Sub-tasks, split it.
- Avoid giant Stories like "Build the whole chat system."

## Sub-task Specificity

Bad examples:

- Build UI
- Add backend
- Write tests
- Connect API
- Update docs

Good examples:

- Create login form validation for email and password fields.
- Implement `POST /api/auth/login` request handling.
- Add integration test for expired token rejection.
- Persist user language preference in the profile table.

## Final Quality Review

Before producing the final CSV, confirm:

- Every parent ID exists.
- Every row has a valid issue type.
- Every row has a meaningful description.
- Every Story belongs to one Epic.
- Every Sub-task belongs to one Story.
- No duplicate or near-duplicate work exists.
- Technical implementation details are specific enough for engineers.
