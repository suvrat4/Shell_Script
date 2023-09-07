#Create a shell script that monitors open network ports on a server and sends alerts when unexpected ports are open or certain services are not running.

#!/bin/bash

# Define the list of expected ports and services
expected_ports=("22" "80" "443")  # Adjust with the ports you expect
email_recipient="admin@example.com"  # Replace with your email address

# Check if the required network tools are installed
if ! command -v netstat &>/dev/null; then
    echo "Error: netstat is not installed. Please install it."
    exit 1
fi

# Check for unexpected open ports
unexpected_ports=()
for port in "${expected_ports[@]}"; do
    if ! netstat -tuln | grep ":$port " &>/dev/null; then
        unexpected_ports+=("$port")
    fi
done

# Send an email alert if unexpected ports are open
if [ ${#unexpected_ports[@]} -gt 0 ]; then
    alert_message="Unexpected open ports detected on server:"
    for port in "${unexpected_ports[@]}"; do
        alert_message+=" Port $port"
    done
    echo "$alert_message" | mail -s "Server Alert" "$email_recipient"
    echo "Alert sent: $alert_message"
fi

# Check if specific services are not running
# Example: Check if Apache web server is not running
if ! systemctl is-active --quiet apache2.service; then
    echo "Apache web server is not running. Sending an alert."
    echo "Apache web server is not running on $(hostname)" | mail -s "Service Alert" "$email_recipient"
fi

# Add more service checks as needed

exit 0
