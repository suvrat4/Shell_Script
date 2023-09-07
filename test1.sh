#Write a shell script that calculates the total size of files in a directory and its subdirectories.

#!/bin/bash

# Check if the user provided a directory as an argument
if [ $# -ne 1 ]; then
    echo "Usage: $0 <directory>"
    exit 1
fi

directory="$1"

# Check if the provided directory exists
if [ ! -d "$directory" ]; then
    echo "Directory '$directory' does not exist."
    exit 1
fi

# Use the 'du' command to calculate disk usage
total_size=$(du -sh "$directory" | awk '{print $1}')

echo "Total size of '$directory' and its subdirectories: $total_size"
