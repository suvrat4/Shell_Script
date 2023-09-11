#!/bin/bash

# Define the directory where the files should be located
target_directory="/path/to/your/directory"

# List of expected files
expected_files=("file1.txt" "file2.txt" "file3.txt")

# Initialize variables to track missing and received files
missing_files=()
received_count=0

# Check if each expected file exists in the target directory
for file in "${expected_files[@]}"; do
    if [ -e "$target_directory/$file" ]; then
        ((received_count++))
    else
        missing_files+=("$file")
    fi
done

# Compose the email message
email_subject="File Check Report"
email_recipient="your@email.com"
email_message="Received files count: $received_count\n\nMissing files:\n${missing_files[*]}"

# Send the email
echo -e "$email_message" | mail -s "$email_subject" "$email_recipient"
