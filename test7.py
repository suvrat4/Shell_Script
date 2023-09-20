import requests
from datetime import datetime, timedelta
import calendar

# Jira server URL and credentials
JIRA_SERVER = 'https://your-jira-instance.com'
USERNAME = 'your_username'
PASSWORD = 'your_password'

# Project key for the specific project you want to query
PROJECT_KEY = 'YOUR_PROJECT_KEY'

# Calculate the start and end dates for the current month
today = datetime.today()
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

# Define the query parameters
params = {
    'jql': jql_query,
}

# Make the API request to Jira
response = session.get(api_endpoint, headers=headers, params=params)

# Check if the request was successful
if response.status_code == 200:
    issues = response.json().get('issues', [])
    for issue in issues:
        print(f'Issue Key: {issue["key"]} - Summary: {issue["fields"]["summary"]}')
else:
    print(f'Error: {response.status_code} - {response.text}')
