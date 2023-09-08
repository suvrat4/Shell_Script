#Shell script to organise the files into sub directories based on the file extension
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

# Create subdirectories for each unique file extension
find "$directory" -type f | while read -r file; do
    extension="${file##*.}"  # Get the file extension
    if [ -n "$extension" ]; then
        # Create the subdirectory if it doesn't exist
        mkdir -p "$directory/$extension"
        # Move the file to the subdirectory
        mv "$file" "$directory/$extension/"
    fi
done

echo "Files in '$directory' have been organized into subdirectories based on their extensions."
