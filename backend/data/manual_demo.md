# AI Website Assistant Demo Documentation

This documentation describes a demo business management application used to test the RAG chatbot.

The application allows administrators to manage users, products, orders, support tickets and internal documentation.

## Users

The user management panel allows administrators to create, view, edit and archive users.

Each user has a name, email, role, status and registration date.

Available roles are:

- Administrator
- Manager
- Support Agent
- Customer

Only administrators can create or archive users.

## User Archiving

To archive a user, the administrator must open the user management panel, select the target user and click the archive option.

Archived users are not deleted from the database. They are hidden from the main user lists but their historical records are preserved.

This is important because the system must keep sensitive information and activity history for security, audit and legal reasons.

## Products

The product management panel allows administrators to manage the product catalog.

Each product can have:

- Name
- Description
- Price
- Stock
- Category
- Status

Products can be active, inactive or archived.

## Orders

The orders panel allows the team to review customer orders, update order status and check delivery information.

Available order statuses are:

- Pending
- Processing
- Shipped
- Completed
- Cancelled

Only managers and administrators can change order status.

## Support Tickets

The support module allows customers to create tickets and support agents to answer them.

Each ticket contains:

- Customer name
- Email
- Subject
- Message
- Priority
- Status

Ticket priorities are low, medium and high.

Ticket statuses are open, in progress, resolved and closed.

## Security

Sensitive information must not be shown to users without proper permissions.

Only authenticated users can access the admin panel.

Critical actions such as archiving users, deleting records or changing order status must require administrator or manager permissions.

## Chatbot Behavior

The chatbot must answer only using the available documentation.

If the answer is not found in the documents, the chatbot must say that it does not have enough information.

The chatbot should show the source documents used to generate each answer.

The chatbot should answer in the same language as the user question whenever possible.

## Example Questions

The chatbot should be able to answer questions such as:

- How do I archive a user?
- What happens to archived users?
- Who can change order status?
- What information is stored in a support ticket?
- What should the chatbot do if it does not have enough information?