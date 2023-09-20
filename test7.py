
from jira import JIRA
from datetime import date, datetime, timedelta
import calendar

# Jira server URL and credentials
JIRA_SERVER = 'https://your-jira-instance.com'
USERNAME = 'your_username'
PASSWORD = 'your_password'

# Project key for the specific project you want to query
PROJECT_KEY = 'YOUR_PROJECT_KEY'

# Initialize Jira client
jira = JIRA(server=JIRA_SERVER, basic_auth=(USERNAME, PASSWORD))

# Calculate the start and end dates for the current month
today = date.today()
first_day_of_month = today.replace(day=1)
last_day_of_month = today.replace(day=calendar.monthrange(today.year, today.month)[1])

# Define JQL query to search for issues in the current month for the specified project
jql_query = f'project = {PROJECT_KEY} AND created >= "{first_day_of_month}" AND created <= "{last_day_of_month}"'

# Execute the JQL query
issues = jira.search_issues(jql_query)

# Print the issue keys and summaries
for issue in issues:
    print(f'Issue Key: {issue.key} - Summary: {issue.fields.summary}')
