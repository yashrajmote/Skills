# Epic Boundaries

When a work item could fit multiple Epics, choose the Epic that owns the final deliverable and document dependencies elsewhere.

## Authentication & Onboarding

Owns:

- Signup.
- Login.
- Verification.
- Password reset.
- Session handling.
- Protected route access.
- Onboarding screens.

Does not own:

- Generic backend infrastructure.
- Unrelated profile settings.
- Deployment or IAM setup.

## Frontend / Mobile App

Owns:

- Screens.
- Navigation.
- UI state.
- Form validation.
- Client-side adapters.
- Loading, error, and empty states.
- Local storage.
- Analytics events from UI.

Does not own:

- Backend persistence.
- Database schema.
- Cloud infrastructure.

## Backend Services & APIs

Owns:

- REST endpoints.
- Service-layer logic.
- DTOs.
- Validation.
- Auth enforcement.
- Database access.
- API error responses.
- Backend tests.

Does not own:

- Cloud deployment.
- UI layout.
- External provider setup unless it is direct integration logic.

## Infrastructure & DevOps

Owns:

- Environments.
- CI/CD.
- Hosting.
- Secrets.
- IAM.
- Networking.
- Logs.
- Monitoring.
- Deployment scripts.

Does not own:

- Product feature logic.
- UI behavior.
- Domain-specific API implementation.

## Integrations & External Services

Owns:

- Third-party API clients.
- Provider-specific authentication.
- Webhooks.
- Synchronization jobs.
- External payload mapping.
- Retry and failure handling for external services.

Does not own:

- Generic app infrastructure.
- Unrelated business features.

## Design System & UI Foundation

Owns:

- Reusable components.
- Theme tokens.
- Spacing.
- Typography.
- Colors.
- Shared form controls.
- Layout patterns.

Does not own:

- Feature-specific business logic.
- API implementation.

## Data & Persistence

Owns:

- Schemas.
- Migrations.
- Indexes.
- Relationships.
- Seed data.
- Data lifecycle and status fields.

Does not own:

- User-facing screens unless directly tied to admin data management.
