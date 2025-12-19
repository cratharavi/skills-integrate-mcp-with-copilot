# Search, filter, and pagination for /activities

GitHub issue: https://github.com/cratharavi/skills-integrate-mcp-with-copilot/issues/14

**Description**

Add query parameters to `/activities` to allow searching, filtering (by available spots, schedule, tags), and pagination.

**Tasks**

- Add query params: `q`, `available`, `schedule`, `page`, `page_size`
- Implement filtering and pagination at the API layer
- Update docs and tests

**Acceptance criteria**

- `/activities?q=chess&available=true&page=1` returns filtered, paginated results
- Tests cover basic filtering scenarios

**Labels**: backend, frontend, enhancement
