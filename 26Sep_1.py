import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
import requests
import pandas as pd
from datetime import datetime, timedelta

# Jira server URL and credentials
JIRA_SERVER = 'https://your-jira-instance.com'
USERNAME = 'your_username'
PASSWORD = 'your_password'

# Project key for the specific project you want to query
PROJECT_KEY = 'YOUR_PROJECT_KEY'

# Calculate the start and end dates for the last 15 days
end_date = datetime.now()
start_date = end_date - timedelta(days=14)  # 14 days ago

# Define the Jira API endpoint for searching issues
api_endpoint = f'{JIRA_SERVER}/rest/api/2/search'

# Initialize variables for pagination
start_at = 0
max_results = 1000  # Adjust as needed to fetch more results per page

# Initialize an empty list to store issue data for all issues
all_issue_data = []

# Initialize a dictionary to store issue data for specific assignees
assignee_specific_data = {}

# Read assignees from a text file
with open('assignees.txt', 'r') as assignees_file:
    assignees = [line.strip() for line in assignees_file]

while True:
    # Construct the JQL query for issues created in the last 15 days for the specified project with pagination
    jql_query = (
        f'project = {PROJECT_KEY} AND created >= "{start_date.strftime("%Y-%m-%d")}" '
        f'AND created <= "{end_date.strftime("%Y-%m-%d")}" ORDER BY Rank DESC'
    )

    # Set up headers for authentication
    headers = {
        'Content-Type': 'application/json',
    }

    # Create a session for making authenticated requests
    session = requests.Session()
    session.auth = (USERNAME, PASSWORD)

    # Define the query parameters including the fields you want (e.g., summary, assignee, status, created, resolved) and pagination
    params = {
        'jql': jql_query,
        'fields': 'key,summary,assignee,status,created,resolutiondate',  # Add any additional fields you need
        'startAt': start_at,
        'maxResults': max_results,
    }

    # Make the API request to Jira
    response = session.get(api_endpoint, headers=headers, params=params)

    # Check if the request was successful
    if response.status_code == 200:
        data = response.json()
        issues = data.get('issues', [])

        # Create a DataFrame from the issues data for the current page
        issue_data = []
        for issue in issues:
            assignee_data = issue['fields']['assignee']
            assignee_name = assignee_data['displayName'] if assignee_data else 'Unassigned'
            issue_key = issue['key']
            summary = issue['fields']['summary']
            status = issue['fields']['status']['name']
            created_date = datetime.strptime(issue['fields']['created'], '%Y-%m-%dT%H:%M:%S.%f%z').strftime('%Y-%m-%d')
            resolved_date = issue['fields'].get('resolutiondate', '')
            if resolved_date:
                resolved_date = datetime.strptime(resolved_date, '%Y-%m-%dT%H:%M:%S.%f%z').strftime('%Y-%m-%d')
            issue_data.append([issue_key, summary, assignee_name, status, created_date, resolved_date])

            # Check if the assignee is in the list of specific assignees
            if assignee_name in assignees:
                assignee_specific_data.setdefault(assignee_name, []).append([issue_key, summary, assignee_name, status, created_date, resolved_date])

        all_issue_data.extend(issue_data)

        # Check if there are more pages of results
        if len(issues) < max_results:
            break  # No more pages
        else:
            start_at += max_results  # Move to the next page
    else:
        print(f'Error: {response.status_code} - {response.text}')
        break

# Create a DataFrame with all issues
df = pd.DataFrame(all_issue_data, columns=["Issue Key", "Summary", "Assignee", "Status", "Created Date", "Resolved Date"])

# Format the "Created Date" and "Resolved Date" columns to display only the date part
df["Created Date"] = pd.to_datetime(df["Created Date"]).dt.strftime('%Y-%m-%d')
df["Resolved Date"] = pd.to_datetime(df["Resolved Date"]).dt.strftime('%Y-%m-%d')

# Save the DataFrame to an Excel file with the sheet name "all issues"
excel_filename_all = "jira_all_issues.xlsx"
with pd.ExcelWriter(excel_filename_all, engine='openpyxl') as writer:
    df.to_excel(writer, sheet_name='all issues', index=False)

# Create a separate Excel file for each specific assignee
for assignee, data_list in assignee_specific_data.items():
    assignee_df = pd.DataFrame(data_list, columns=["Issue Key", "Summary", "Assignee", "Status", "Created Date", "Resolved Date"])
    assignee_excel_filename = f"jira_issues_{assignee}.xlsx"
    with pd.ExcelWriter(assignee_excel_filename, engine='openpyxl') as writer:
        assignee_df.to_excel(writer,
