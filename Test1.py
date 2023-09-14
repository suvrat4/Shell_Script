import requests
import pandas as pd
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# List of API endpoints to check
api_endpoints = [
    "https://api1.example.com/health",
    "https://api2.example.com/health",
    # Add more endpoints
]

# Function to check API status
def check_api_status(endpoint):
    try:
        response = requests.get(endpoint)
        if response.status_code == 200:
            return "Up"
        else:
            return "Down"
    except Exception as e:
        return "Error"

# Collect API status
api_status = {}
for endpoint in api_endpoints:
    status = check_api_status(endpoint)
    api_status[endpoint] = status

# Create a DataFrame for tabular representation
df = pd.DataFrame(list(api_status.items()), columns=["API Endpoint", "Status"])

# Send email with tabular data
email_address = "your_email@gmail.com"
password = "your_password"

msg = MIMEMultipart()
msg['From'] = email_address
msg['To'] = email_address
msg['Subject'] = "API Status Report"
body = df.to_html()

msg.attach(MIMEText(body, 'html'))

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(email_address, password)
server.sendmail(email_address, email_address, msg.as_string())
server.quit()
