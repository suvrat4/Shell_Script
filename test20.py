
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

# ... Previous code ...

# Save the Excel file
wb.save('jira_data.xlsx')
print('Jira data saved to jira_data.xlsx')

# Email configuration
sender_email = 'your_email@gmail.com'
receiver_email = 'recipient_email@example.com'
email_subject = 'Jira Data for the Past 15 Days'
email_body = 'Please find the attached Excel file with Jira data.'

# Create a multipart message
msg = MIMEMultipart()
msg['From'] = sender_email
msg['To'] = receiver_email
msg['Subject'] = email_subject

# Attach the Excel file to the email
attachment = open('jira_data.xlsx', 'rb')
part = MIMEBase('application', 'octet-stream')
part.set_payload(attachment.read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', 'attachment; filename="jira_data.xlsx"')
msg.attach(part)

# Add the email body as plain text
msg.attach(MIMEText(email_body, 'plain'))

# Connect to the SMTP server (Gmail SMTP server used in this example)
smtp_server = 'smtp.gmail.com'
smtp_port = 587
smtp_username = 'your_email@gmail.com'
smtp_password = 'your_email_password'

try:
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(smtp_username, smtp_password)

    # Send the email
    server.sendmail(sender_email, receiver_email, msg.as_string())
    print('Email sent successfully')
except Exception as e:
    print(f'Error sending email: {str(e)}')
finally:
    # Close the SMTP server connection
    server.quit()
