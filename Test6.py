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

# Add color and borders based on status
def style_cells(val):
    if val == 'Up':
        return 'background-color: lime; border: 1px solid black;'
    else:
        return 'background-color: red; border: 1px solid black;'

styled_df = df.style.applymap(style_cells)

# Create separate DataFrames for Up and Down APIs
up_df = df[df["Status"] == "Up"]
down_df = df[df["Status"] == "Down"]

# Send email with greetings, complete table, and separate tables
email_address = "your_email@gmail.com"
password = "your_password"

msg = MIMEMultipart()
msg['From'] = email_address
msg['To'] = email_address
msg['Subject'] = "API Status Report"

# Greet the team
greeting = "Hello Team,\n\nHere is the API status report:\n"
msg.attach(MIMEText(greeting, 'plain'))

# Add the complete table
body = styled_df.render()
msg.attach(MIMEText(body, 'html'))

# Add separate tables for Up and Down APIs
up_table = up_df.to_html(index=False, classes='table table-bordered')
down_table = down_df.to_html(index=False, classes='table table-bordered')

msg.attach(MIMEText("<h3>Up APIs:</h3>", 'html'))
msg.attach(MIMEText(up_table, 'html'))

msg.attach(MIMEText("<h3>Down APIs:</h3>", 'html'))
msg.attach(MIMEText(down_table, 'html'))

# Send the email
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(email_address, password)
server.sendmail(email_address, email_address, msg.as_string())
server.quit()
