# Add authentication and role-based access (admin / student)

GitHub issue: https://github.com/cratharavi/skills-integrate-mcp-with-copilot/issues/9

**Description**

Implement authentication (JWT or session) and role-based access control so admins can manage activities while students can sign up.

**Tasks**

- Add login/register endpoints
- Implement role checks (admin vs student)
- Protect admin-only endpoints
- Add tests for auth flows

**Acceptance criteria**

- Admin endpoints are protected and accessible only by admin users
- Students can register/login and sign up for activities after authentication
- Tests for auth flows exist and run in CI

**Labels**: backend, security, feature
