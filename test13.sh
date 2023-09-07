#Write a shell script that monitors changes to a specific file and sends an email notification when it's modified.

#!/bin/bash

# Set the path to the file you want to monitor
file_to_monitor="/path/to/your/file.txt"

# Set the recipient email address
recipient="recipient@example.com"

# Function to send an email notification
send_email_notification() {
    subject="File Modification Alert: $file_to_monitor"
    message="The file $file_to_monitor has been modified."

    echo "$message" | mail -s "$subject" "$recipient"
}

# Monitor the file for changes
while true; do
    inotifywait -e modify "$file_to_monitor"
    send_email_notification
done
