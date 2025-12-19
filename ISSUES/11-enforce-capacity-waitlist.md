# Enforce capacity and implement waitlist

GitHub issue: https://github.com/cratharavi/skills-integrate-mcp-with-copilot/issues/11

**Description**

Prevent signups when an activity reaches `max_participants` and implement an optional waitlist.

**Tasks**

- Block signups when capacity is full (return 409)
- Add waitlist model and endpoints to view/join/leave waitlist
- Notify users when a spot opens (email or in-app)
- Add tests for capacity and waitlist behavior

**Acceptance criteria**

- Signups return an error when activity is full
- Users can be placed on a waitlist with ordering preserved
- Tests cover capacity edge cases

**Labels**: backend, feature
