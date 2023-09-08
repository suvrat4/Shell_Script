#!/bin/bash

# Directory to watch for incoming files
watch_directory="/path/to/watched/directory"

# Destination directories for different file types
image_dir="$watch_directory/images"
document_dir="$watch_directory/documents"
other_dir="$watch_directory/others"

# Create the destination directories if they don't exist
mkdir -p "$image_dir" "$document_dir" "$other_dir"

# Start the file monitoring loop
inotifywait -m -r -e create --format '%w%f' "$watch_directory" | while read -r new_file
do
    # Check if the new file exists
    if [ -e "$new_file" ]; then
        # Get the file extension
        file_extension="${new_file##*.}"

        # Move the file to the appropriate destination directory based on its extension
        case "$file_extension" in
            jpg|jpeg|png|gif)
                destination="$image_dir"
                ;;
            pdf|doc|docx|txt)
                destination="$document_dir"
                ;;
            *)
                destination="$other_dir"
                ;;
        esac

        # Move the file
        mv "$new_file" "$destination"
        echo "Moved '$new_file' to '$destination'"
    fi
done
