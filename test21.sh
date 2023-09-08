#!/bin/bash

# Function to organize files into subdirectories
organize_files() {
    local source_dir="$1"
    local target_dir="$2"
    local log_file="$3"

    # Create a log file if specified
    if [ -n "$log_file" ]; then
        exec &>> "$log_file"
        echo "Logging started: $(date)"
    fi

    # Check if the source directory exists
    if [ ! -d "$source_dir" ]; then
        echo "Source directory '$source_dir' does not exist."
        exit 1
    fi

    # Create the target directory if it doesn't exist
    mkdir -p "$target_dir"

    # Find and organize files
    find "$source_dir" -type f | while read -r file; do
        # Get the file extension
        extension="${file##*.}"

        # Handle files without extensions
        if [ -z "$extension" ]; then
            extension="NoExtension"
        fi

        # Create the subdirectory if it doesn't exist
        mkdir -p "$target_dir/$extension"

        # Check for duplicates before moving
        if [ -f "$target_dir/$extension/$(basename "$file")" ]; then
            echo "Duplicate found: '$file' (Skipping)"
        else
            # Move the file to the subdirectory
            mv "$file" "$target_dir/$extension/"
            echo "Moved: '$file' -> '$target_dir/$extension/'"
        fi
    done

    echo "Files in '$source_dir' have been organized into subdirectories in '$target_dir'."

    if [ -n "$log_file" ]; then
        echo "Logging ended: $(date)"
    fi
}

# Check if the user provided source and target directories as arguments
if [ $# -lt 2 ]; then
    echo "Usage: $0 <source_directory> <target_directory> [log_file]"
    exit 1
fi

source_directory="$1"
target_directory="$2"
log_file="$3"

organize_files "$source_directory" "$target_directory" "$log_file"
