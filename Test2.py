import requests

# Define the list of API URLs
api_urls = [
    "https://api1.example.com/health",
    "https://api2.example.com/health",
    # Add more API URLs here
]

# Function to perform health checks
def check_health(api_url):
    try:
        response = requests.get(api_url)
        response.raise_for_status()  # Raise an exception if status code is not 2xx
        json_data = response.json()
        # Check the JSON response for health status, adapt this to your API's JSON structure
        if json_data.get("status") == "up":
            return True
        else:
            return False
    except Exception as e:
        return False

# Iterate through the API URLs and perform checks
for url in api_urls:
    status = check_health(url)
    if status:
        print(f"{url} is UP")
    else:
        print(f"{url} is DOWN")
