#Write a shell script that displays the top 5 largest files in a directory, sorted by file size.
#!/bin/bash

# Check if a directory is provided as an argument
if [ $# -ne 1 ]; then
    echo "Usage: $0 <directory>"
    exit 1
fi

directory="$1"

# Check if the directory exists
if [ ! -d "$directory" ]; then
    echo "Error: Directory '$directory' does not exist."
    exit 1
fi

# Use 'du' to calculate file sizes, 'sort' to sort by size in reverse order, and 'head' to display the top 5
largest_files=$(du -h "$directory"/* 2>/dev/null | sort -rh | head -5)

# Display the top 5 largest files
echo "Top 5 Largest Files in '$directory':"
echo "$largest_files"
