# Story Writing

Use these rules to make generated Jira work technically useful.

## Better Story Descriptions

Every Story should include enough technical detail that an engineer can understand what to build.

A good Story description should mention relevant details such as:

- User or system capability.
- Screen or route involved.
- API endpoint involved.
- Data entity or table involved.
- Request and response payloads.
- Validation rules.
- Permission rules.
- State transitions.
- Loading, error, and empty states.
- Analytics or logging requirements.
- Testing expectations.
- Dependencies.

Do not write shallow descriptions like:

```text
Build the login feature.
```

Instead write:

```text
Implement the login capability for registered users. The mobile login screen should collect email and password, validate required fields, call POST /api/auth/login, handle invalid credentials, persist the returned access token securely, and route the user to the authenticated home screen.
```

## Better Sub-task Descriptions

Every Sub-task should be binary and implementation-specific.

Each Sub-task should answer:

- What file, component, endpoint, service, table, or configuration is being changed?
- What exact behavior should exist when this Sub-task is done?
- What success criteria prove it works?
- What edge cases should be handled?

## Acceptance Criteria Quality

Acceptance criteria should be concrete and testable.

Good:

- User sees inline validation when email is missing.
- `POST /api/auth/login` returns `401` for invalid credentials.
- Access token is stored securely after successful login.
- Expired token redirects the user to login.

Bad:

- Login works.
- Backend is complete.
- UI is done.

## Technical Depth Checklist

When relevant, include:

Frontend:

- Screen or component name.
- Route or navigation.
- State management.
- API adapter.
- Validation.
- Loading state.
- Error state.
- Empty state.
- Analytics event.

Backend:

- Endpoint.
- Method.
- Request DTO.
- Response DTO.
- Validation.
- Service method.
- Repository query.
- Error handling.
- Permissions.
- Tests.

Database:

- Table.
- Columns.
- Relationships.
- Indexes.
- Migrations.
- Enum or status fields.
- Seed data.

Infrastructure:

- Service or resource name.
- Environment variables.
- IAM permissions.
- Secrets.
- Deployment.
- Monitoring.
- Logs.
- Alarms.

Integrations:

- Provider.
- API endpoint.
- Credentials.
- Webhook.
- Payload mapping.
- Retries.
- Rate limits.
- Failure modes.

Security:

- Auth role.
- Ownership check.
- Protected route.
- Token handling.
- Audit logging.
- Sensitive data handling.

Testing:

- Unit tests.
- Integration tests.
- UI tests.
- Negative cases.
- Permission tests.
- Failure and retry cases.
