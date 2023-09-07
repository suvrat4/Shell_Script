#Create a shell script that extracts data from a JSON file and formats it into a human-readable table or report.
#!/bin/bash

# Check if a filename is provided as an argument
if [ $# -ne 1 ]; then
    echo "Usage: $0 <json_file>"
    exit 1
fi

json_file="$1"

# Check if the file exists
if [ ! -e "$json_file" ]; then
    echo "Error: File '$json_file' does not exist."
    exit 1
fi

# Use 'jq' to extract data from the JSON file and format it into a table
output=$(jq -r '.[] | [.name, .age, .city] | @tsv' "$json_file")

# Display the formatted data
echo -e "Name\tAge\tCity"
echo -e "$output"
