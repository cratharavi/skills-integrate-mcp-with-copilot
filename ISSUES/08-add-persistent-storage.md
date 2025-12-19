# Add persistent storage for activities and students

GitHub issue: https://github.com/cratharavi/skills-integrate-mcp-with-copilot/issues/8

**Description**

Replace the current in-memory storage with a persistent database (SQLite or Postgres).

**Tasks**

- Create database models for Activities and Students
- Add CRUD operations backed by the DB
- Add migration(s) or setup script
- Add unit tests for persistence behavior

**Acceptance criteria**

- Data persists across server restarts
- API returns DB-backed data for `/activities` and signup/unregister endpoints
- Tests covering persistence pass in CI

**Labels**: backend, feature
