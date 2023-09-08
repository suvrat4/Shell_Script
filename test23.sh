#Write a shell script that renames all files in a directory with a ".txt" extension to have a ".bak" extension.
#!/bin/bash

# Directory containing the .txt files
directory="/path/to/directory"

# Check if the directory exists
if [ -d "$directory" ]; then
    # Loop through each .txt file in the directory and rename it
    for file in "$directory"/*.txt; do
        if [ -e "$file" ]; then
            # Get the filename without the path
            filename=$(basename "$file")

            # Remove the .txt extension and add .bak
            new_filename="${filename%.txt}.bak"

            # Rename the file
            mv "$file" "$directory/$new_filename"
            echo "Renamed '$filename' to '$new_filename'"
        fi
    done

    echo "All .txt files renamed to .bak in '$directory'"
else
    echo "Directory '$directory' not found."
fi

