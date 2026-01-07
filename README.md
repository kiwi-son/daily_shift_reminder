# daily_shift_remainder
📅 Daily Shift Reminder Automation This project is a full-stack automation system that manages employee shift schedules. It allows for bulk uploads via Excel, stores data in MongoDB, and sends automated daily email reminders to staff using GitHub Actions.
🚀 System OverviewThe system consists of three main components:
Frontend: A management dashboard to upload, view, and delete monthly shifts.
Database: MongoDB stores the shift details, employee IDs, and email addresses.
Automation: A Python script triggered by GitHub Actions that fetches today's shifts and sends emails via yagmail.

🛠️ Tech StackFrontend: [HTML]
Database: MongoDB 
Automation: Python 3.10
Email Service: yagmail (SMTP)
Workflow: GitHub Actions / Cloud Scheduler
📋 Features
1. Excel Upload SystemThe frontend includes a dedicated upload section.
2. To ensure the automation works, the Excel file must follow a specific template:Required Columns: Date, Employee Name, Email, Shift Type (e.g., General, Night, Morning).
3. Validation: The system only accepts the pre-defined .xlsx format to prevent database errors.
4.  Shift ManagementMonthly Upload: Upload the entire month's schedule at once.Delete/Reset: Option to clear the current month’s schedule if a re-upload is needed.
5.  Automated NotificationsThe system runs daily at 10:00 PM IST.It identifies employees scheduled for the following day.Sends a personalized email reminder with their shift timings.
   
