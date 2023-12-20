import requests
from requests.auth import HTTPBasicAuth

# Splunk connection settings
splunk_url = "https://your_splunk_instance:8089"
splunk_username = "your_username"
splunk_password = "your_password"

# Specify your Splunk search query with app name
search_query = 'search your_search_query_here earliest="-24h" latest="now" app="your_app_name"'

# Splunk REST API endpoint for search
search_endpoint = f"{splunk_url}/services/search/jobs"

# Define search parameters
search_params = {
    "search": search_query,
    "exec_mode": "blocking",  # Use "normal" for asynchronous execution
}

# Make the request to start the search
response = requests.post(
    search_endpoint,
    params=search_params,
    auth=HTTPBasicAuth(splunk_username, splunk_password),
    verify=False,  # You may want to handle SSL verification more securely in production
)

# Check if the search was successful
if response.status_code == 201:
    search_results = response.json()
    sid = search_results["sid"]

    # Retrieve search results
    results_endpoint = f"{splunk_url}/services/search/jobs/{sid}/results"
    response = requests.get(
        results_endpoint,
        auth=HTTPBasicAuth(splunk_username, splunk_password),
        verify=False,
    )

    if response.status_code == 200:
        search_results = response.text
        print(search_results)
    else:
        print(f"Failed to retrieve search results. Status code: {response.status_code}")

else:
    print(f"Failed to start search. Status code: {response.status_code}")
