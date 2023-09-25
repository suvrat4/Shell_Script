import win32com.client
import re
import datetime
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Outlook application ko shuru karen
outlook = win32com.client.Dispatch("Outlook.Application").GetNamespace("MAPI")

# Error aur failed pattern
error_pattern = re.compile(r'error', re.IGNORECASE)
failed_pattern = re.compile(r'failed', re.IGNORECASE)

# Summary report
report_text = "Summary Report for " + datetime.datetime.now().strftime("%Y-%m-%d") + "\n\n"

# Sabhi folders aur subfolders par chalein
def search_folders(folder, report_text):
    for item in folder.Items:
        if error_pattern.search(item.Subject) or error_pattern.search(item.Body):
            report_text += f"Subject: {item.Subject}\nReceived: {item.ReceivedTime}\n\n"
        if failed_pattern.search(item.Subject) or failed_pattern.search(item.Body):
            report_text += f"Subject: {item.Subject}\nReceived: {item.ReceivedTime}\n\n"
    
    for subfolder in folder.Folders:
        report_text = search_folders(subfolder, report_text)
    
    return report_text

# Outlook ke root folder se search shuru karen
root_folder = outlook.GetDefaultFolder(6)  # 6 corresponds to the Inbox folder, change as needed
report_text = search_folders(root_folder, report_text)

# Summary report ko email ke roop mein bhejen
email = MIMEMultipart()
email['From'] = 'your_email@example.com'
email['To'] = 'recipient@example.com'
email['Subject'] = 'Outlook Error and Failed Patterns Summary Report'

email.attach(MIMEText(report_text, 'plain'))

# SMTP server ka istemal karke email bhejen
smtp_server = 'smtp.example.com'
smtp_port = 587
smtp_username = 'your_email@example.com'
smtp_password = 'your_password'

server = smtplib.SMTP(smtp_server, smtp_port)
server.starttls()
server.login(smtp_username, smtp_password)
server.sendmail(smtp_username, 'recipient@example.com', email.as_string())
server.quit()
