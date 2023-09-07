#Write a shell script that takes a filename as input and counts the number of lines, words, and characters in the file.

#!/bin/bash

# Check if a filename is provided as an argument
if [ $# -ne 1 ]; then
    echo "Usage: $0 <filename>"
    exit 1
fi

filename="$1"

# Check if the file exists
if [ ! -e "$filename" ]; then
    echo "Error: File '$filename' does not exist."
    exit 1
fi

# Count lines, words, and characters using 'wc'
lines=$(wc -l < "$filename")
words=$(wc -w < "$filename")
characters=$(wc -m < "$filename")

# Display the counts
echo "File: $filename"
echo "Lines: $lines"
echo "Words: $words"
echo "Characters: $characters"
