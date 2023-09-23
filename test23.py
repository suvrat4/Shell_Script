import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
import requests
import pandas as pd
from datetime import datetime, timedelta
from openpyxl import Workbook
from openpyxl.drawing.image import Image
import matplotlib.pyplot as plt
import io

# ... (previous code)

# Create a bar chart using matplotlib
plt.bar(status_counts['index'], status_counts['Status'])
plt.title('Issue Status Counts')
plt.xlabel('Status')
plt.ylabel('Count')
plt.xticks(rotation=45)  # Rotate x-axis labels for better readability

# Save the chart as an image
chart_image_filename = "chart_image.png"
chart_image_path = f"{excel_filename.split('.')[0]}_{chart_image_filename}"
plt.savefig(chart_image_path, bbox_inches='tight')

# Close the matplotlib plot
plt.close()

# Add the chart image to the Excel file
status_wb = openpyxl.load_workbook(excel_filename)
status_ws = status_wb.active
img = Image(chart_image_path)
status_ws.add_image(img, 'E5')  # Adjust the cell reference as needed

# Save the updated Excel file
status_wb.save(excel_filename)

# ... (rest of the code remains the same)
