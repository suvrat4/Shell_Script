import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import requests
from datetime import datetime, timedelta, date
import calendar

# Jira server URL and credentials
JIRA_SERVER = 'https://your-jira-instance.com'
USERNAME = 'your_username'
PASSWORD = 'your_password'

# Project key for the specific project you want to query
PROJECT_KEY = 'YOUR_PROJECT_KEY'

# Calculate the start and end dates for the current month
today = date.today()
first_day_of_month = today.replace(day=1)
last_day_of_month = today.replace(day=calendar.monthrange(today.year, today.month)[1])

# Define the Jira API endpoint for searching issues
api_endpoint = f'{JIRA_SERVER}/rest/api/2/search'

# Construct the JQL query for issues created in the current month for the specified project
jql_query = f'project = {PROJECT_KEY} AND created >= "{first_day_of_month.strftime("%Y-%m-%d")}" AND created <= "{last_day_of_month.strftime("%Y-%m-%d")}"'

# Set up headers for authentication
headers = {
    'Content-Type': 'application/json',
}

# Create a session for making authenticated requests
session = requests.Session()
session.auth = (USERNAME, PASSWORD)

# Define the query parameters including the fields you want (e.g., summary, assignee)
params = {
    'jql': jql_query,
    'fields': 'summary,assignee',  # Add any additional fields you need
}

# Make the API request to Jira
response = session.get(api_endpoint, headers=headers, params=params)

# Check if the request was successful
if response.status_code == 200:
    data = response.json()
    issues = data.get('issues', [])
    
    # Create an email message
    email_subject = 'Jira Issues for Current Month'
    email_from = 'your_email@example.com'
    email_to = 'recipient@example.com'
    
    message = MIMEMultipart()
    message['From'] = email_from
    message['To'] = email_to
    message['Subject'] = email_subject
    
    # Create the email body with issue details
    email_body = "Jira Issues for the Current Month:\n\n"
    
    for issue in issues:
        assignee_data = issue['fields']['assignee']
        assignee_name = assignee_data['displayName'] if assignee_data else 'Unassigned'
        email_body += f'Issue Key: {issue["key"]} - Summary: {issue["fields"]["summary"]} - Assignee: {assignee_name}\n'
    
    # Attach the email body to the email message
    message.attach(MIMEText(email_body, 'plain'))
    
    # Connect to the SMTP server and send the email
    smtp_server = 'smtp.example.com'  # Replace with your SMTP server details
    smtp_port = 587  # Replace with the appropriate port
    smtp_username = 'your_email@example.com'
    smtp_password = 'your_email_password'
    
    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(smtp_username, smtp_password)
            server.sendmail(email_from, email_to, message.as_string())
        print("Email sent successfully.")
    except Exception as e:
        print(f"Error sending email: {str(e)}")
else:
    print(f'Error: {response.status_code} - {response.text}')
