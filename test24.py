import pandas as pd
from jira import JIRA
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from email.mime.text import MIMEText

# Step 1: Connect to Jira
jira = JIRA(server='Your_Jira_Server_URL', basic_auth=('Your_Username', 'Your_Password'))

# Step 2: Fetch Jira data for the past 15 days
from datetime import datetime, timedelta
end_date = datetime.now()
start_date = end_date - timedelta(days=15)

issues = jira.search_issues(
    f'created >= "{start_date}" AND created <= "{end_date}"',
    maxResults=None  # To fetch all matching issues
)

data = []

for issue in issues:
    issue_data = [
        issue.key,
        issue.fields.summary,
        issue.fields.assignee.displayName if issue.fields.assignee else "",
        issue.fields.status.name,
        issue.fields.created,
        issue.fields.resolutiondate if hasattr(issue.fields, 'resolutiondate') else ""
    ]
    data.append(issue_data)

# Step 3: Calculate open and closed ticket counts
open_count = sum(1 for issue in data if issue[3] != "Closed")
closed_count = len(data) - open_count

# Step 4: Create an Excel spreadsheet
excel_data = pd.DataFrame(data, columns=[
    'Issue Key', 'Summary', 'Assignee', 'Status', 'Created Date', 'Resolved Date'
])

excel_writer = pd.ExcelWriter('jira_data.xlsx', engine='xlsxwriter')
excel_data.to_excel(excel_writer, sheet_name='Jira Data', index=False)

# Create a summary tab
summary_data = pd.DataFrame({'Status': ['Open', 'Closed'], 'Count': [open_count, closed_count]})
summary_data.to_excel(excel_writer, sheet_name='Ticket Count Summary', index=False)

excel_writer.save()

# Step 5: Send the Excel file via email
from_email = 'your_email@gmail.com'
to_email = 'recipient_email@gmail.com'
email_subject = 'Jira Data for the Past 15 Days'

msg = MIMEMultipart()
msg['From'] = from_email
msg['To'] = to_email
msg['Subject'] = email_subject

# Attach the Excel file
with open('jira_data.xlsx', 'rb') as file:
    part = MIMEApplication(file.read())
part.add_header('Content-Disposition', 'attachment', filename='jira_data.xlsx')
msg.attach(part)

# Connect to SMTP server and send email
smtp_server = 'smtp.gmail.com'
smtp_port = 587
smtp_username = 'your_email@gmail.com'
smtp_password = 'your_password'

server = smtplib.SMTP(smtp_server, smtp_port)
server.starttls()
server.login(smtp_username, smtp_password)
server.sendmail(from_email, to_email, msg.as_string())
server.quit()
