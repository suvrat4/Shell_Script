#Shell script to check if required files are present to process

#!/bin/bash

# Define the list of required files
required_files=("file1.txt" "file2.txt" "file3.txt")

# Loop through the required files and check if each exists
for file in "${required_files[@]}"; do
    if [ ! -e "$file" ]; then
        echo "Required file '$file' is missing. Cannot proceed."
        exit 1
    fi
done

# If all required files are present, proceed with processing
echo "All required files are present. Processing..."
# Your processing logic here
