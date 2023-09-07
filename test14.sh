#Create a shell script that parses Apache error logs and identifies common error patterns and send email
#!/bin/bash

# Set the path to your Apache error log file
error_log="/var/log/apache2/error.log"

# Define common error patterns (add more as needed)
error_patterns=(
  "PHP Notice"
  "PHP Warning"
  "500 Internal Server Error"
)

# Create a temporary file to store the error details
temp_file="/tmp/apache_error_report.txt"

# Check if the error log file exists
if [ ! -f "$error_log" ]; then
    echo "Error: Apache error log file not found: $error_log"
    exit 1
fi

# Initialize the error report
echo "Apache Error Report" > "$temp_file"
echo "-------------------" >> "$temp_file"
echo "Timestamp: $(date)" >> "$temp_file"
echo "" >> "$temp_file"

# Loop through the error patterns and extract matching lines
for pattern in "${error_patterns[@]}"; do
    echo "Errors matching pattern: $pattern" >> "$temp_file"
    grep -i "$pattern" "$error_log" >> "$temp_file"
    echo "" >> "$temp_file"
done

# Send the error report via email
recipient="recipient@example.com"
subject="Apache Error Report"
mail -s "$subject" "$recipient" < "$temp_file"

# Remove the temporary error report file
rm "$temp_file"
