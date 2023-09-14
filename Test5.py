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

# Add color and borders to each row based on status
def style_rows(row):
    border = 'border: 1px solid black;'
    if row['Status'] == 'Up':
        color = 'background-color: lime;'
    else:
        color = 'background-color: red;'
    return [f'{color} {border}' for _ in row]

# Style the DataFrame with background color and borders for each row
styled_df = df.apply(style_rows, axis=1)

# Add a new column for row numbering starting from 1
styled_df.insert(0, 'Row', range(1, 1 + len(styled_df)))

# Send email with styled tabular data including row numbers starting from 1
email_address = "your_email@gmail.com"
password = "your_password"

msg = MIMEMultipart()
msg['From'] = email_address
msg['To'] = email_address
msg['Subject'] = "API Status Report"

# Create an HTML table with borders for each row and row numbering
table_with_borders = f'<table border="0" style="border-collapse: collapse;">{styled_df.to_html(index=False, escape=False)}</table>'
msg.attach(MIMEText(table_with_borders, 'html'))

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(email_address, password)
server.sendmail(email_address, email_address, msg.as_string())
server.quit()
