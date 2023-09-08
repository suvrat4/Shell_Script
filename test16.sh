#Create a shell script to extract text between two specified patterns in a file.
#!/bin/bash

# Check if the user provided a file and two patterns as arguments
if [ $# -ne 3 ]; then
    echo "Usage: $0 <file> <start_pattern> <end_pattern>"
    exit 1
fi

file="$1"
start_pattern="$2"
end_pattern="$3"

# Check if the provided file exists
if [ ! -f "$file" ]; then
    echo "File '$file' does not exist."
    exit 1
fi

# Use 'sed' to extract text between the specified patterns
sed -n "/$start_pattern/,/$end_pattern/p" "$file"
