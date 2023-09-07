#Write a shell script that generates an HTML report of disk usage statistics for a server and send it to email

#!/bin/bash

# Set recipient email address
recipient="recipient@example.com"

# Set the subject for the email
subject="Disk Usage Report"

# Set the path for the HTML report
report_path="/tmp/disk_usage_report.html"

# Create the HTML report
echo "<html>
<head>
    <title>Disk Usage Report</title>
</head>
<body>
    <h1>Disk Usage Report</h1>
    <pre>" > "$report_path"

df -h >> "$report_path"

echo "</pre>
</body>
</html>" >> "$report_path"

# Send the email with the report as an attachment
mail -s "$subject" "$recipient" < "$report_path"

# Remove the temporary HTML report file
rm "$report_path"
