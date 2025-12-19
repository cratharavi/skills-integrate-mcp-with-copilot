# Student profiles & My Activities endpoint

GitHub issue: https://github.com/cratharavi/skills-integrate-mcp-with-copilot/issues/12

**Description**

Add a Student model (name, grade, email) and endpoints for students to view/edit their profile and list their registered activities.

**Tasks**

- Add Student DB model and migrations
- Add endpoints: GET/PUT `/students/{email}`, GET `/students/{email}/activities`
- Integrate with auth so students can only access their data
- Add tests for student profile endpoints

**Acceptance criteria**

- Students can view and edit their profile
- Students can fetch a list of activities they're signed up for
- Authorization prevents students from accessing other students' data

**Labels**: backend, feature
