import requests
from datetime import datetime, date

# Jira API endpoint and credentials
base_url = "https://your-jira-instance-url/rest/api/2/"
username = "your-username"
password = "your-password"

# Calculate the start and end date for the current month
today = date.today()
first_day_of_month = date(today.year, today.month, 1)
last_day_of_month = date(today.year, today.month + 1, 1) - timedelta(days=1)

# Define JQL query to retrieve issues created in the current month
jql_query = f"created >= '{first_day_of_month}' AND created <= '{last_day_of_month}'"

# Create headers with basic authentication
headers = {
    "Authorization": "Basic <base64-encoded-credentials>"
}

# Make a GET request to Jira API to retrieve issues
response = requests.get(f"{base_url}search?jql={jql_query}", headers=headers)

if response.status_code == 200:
    data = response.json()
    
    # Extract and process the retrieved data
    issues = data['issues']
    for issue in issues:
        print(f"Key: {issue['key']}")
        print(f"Summary: {issue['fields']['summary']}")
        print(f"Created: {issue['fields']['created']}")
        print("-" * 30)
else:
    print(f"Error: {response.status_code} - {response.text}")
