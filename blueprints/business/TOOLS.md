# Tools

<!-- CUSTOMIZE: Add or remove tools based on your agent's capabilities and integrations -->

## Core Tools

### search_knowledge_base
Search internal documentation and FAQs.

**When to use:** Answering customer questions, finding policies
**Parameters:**
- query: Search terms
- category: Filter by topic

### send_email
Send email to customers or team members.

**When to use:** Follow-ups, confirmations, updates
**Parameters:**
- to: Recipient email
- subject: Email subject
- body: Email content
- cc: Optional CC recipients

**Tips:**
- Always include context for why you're emailing
- Keep subject lines clear and specific
- Review before sending important emails

### create_ticket
Create support or task ticket.

**When to use:** Tracking issues, assigning work, escalation
**Parameters:**
- type: support, task, bug
- title: Brief description
- description: Full details
- priority: low, medium, high, urgent
- assignee: Who should handle

### update_crm
Update customer relationship management data.

**When to use:** Recording interactions, updating customer info
**Parameters:**
- customer_id: Customer identifier
- field: What to update
- value: New value
- notes: Context for the change

### search_crm
Look up customer information.

**When to use:** Understanding customer context, checking history
**Parameters:**
- query: Search by name, email, company
- fields: Specific fields to return

## Optional Tools

### schedule_meeting
Create calendar events.

**When to use:** Booking calls, demos, meetings
**Parameters:**
- title: Meeting name
- attendees: List of participants
- datetime: When to schedule
- duration: Length in minutes

### generate_report
Create business reports.

**When to use:** Weekly reviews, metrics summaries
**Parameters:**
- type: Report type
- date_range: Time period
- filters: Additional filters

### send_slack
Send internal message.

**When to use:** Quick team communication
**Parameters:**
- channel: Where to send
- message: Content

## Tool Usage Guidelines

1. **Check before contacting** - Look up customer info first
2. **Document interactions** - Update CRM after conversations
3. **Escalate with context** - Include full background in tickets
4. **Review before sending** - Double-check external communications
