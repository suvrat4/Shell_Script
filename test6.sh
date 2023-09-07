#Write a shellscript that scans a log file for IP addresses and counts the occurrences of each unique IP address.
#!/bin/bash

# Check if a log file is provided as an argument
if [ $# -ne 1 ]; then
    echo "Usage: $0 <log_file>"
    exit 1
fi

log_file="$1"

# Check if the file exists
if [ ! -e "$log_file" ]; then
    echo "Error: File '$log_file' does not exist."
    exit 1
fi

# Use 'grep' to extract IP addresses from the log file
# The regular expression \b(?:\d{1,3}\.){3}\d{1,3}\b matches IPv4 addresses
ip_addresses=$(grep -oE '\b(?:\d{1,3}\.){3}\d{1,3}\b' "$log_file")

# Use 'sort' and 'uniq -c' to count the occurrences of each unique IP address
ip_counts=$(echo "$ip_addresses" | sort | uniq -c)

# Display the IP addresses and their counts
echo "IP Address Counts in '$log_file':"
echo "$ip_counts"
