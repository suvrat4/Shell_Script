#Write a shell script to find and replace a specific word in a text file, preserving the case of the original word.

#!/bin/bash

# Check if the user provided a file, the word to find, and the replacement word as arguments
if [ $# -ne 3 ]; then
    echo "Usage: $0 <file> <word_to_find> <replacement_word>"
    exit 1
fi

file="$1"
word_to_find="$2"
replacement_word="$3"

# Check if the provided file exists
if [ ! -f "$file" ]; then
    echo "File '$file' does not exist."
    exit 1
fi

# Use 'sed' to find and replace the word while preserving case
sed -i "s/\b${word_to_find}\b/${replacement_word}/gI" "$file"
