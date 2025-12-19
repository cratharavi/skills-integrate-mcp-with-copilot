# Export participants & bulk mailer

GitHub issue: https://github.com/cratharavi/skills-integrate-mcp-with-copilot/issues/16

**Description**

Add an endpoint to export participant lists (CSV) and an admin feature to send bulk mail to participants.

**Tasks**

- Add CSV export endpoint for activity participants (admin-only)
- Add bulk-mail endpoint to send emails to selected participant lists
- Add tests and rate limiting for bulk mail

**Acceptance criteria**

- Admin can download CSV of participants
- Admin can send bulk mail and see delivery summary (or at least success/failure per send)
- Tests/mock coverage present

**Labels**: backend, feature
