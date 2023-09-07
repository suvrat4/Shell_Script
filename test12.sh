#Create a shell script that extracts and displays the top N lines with the highest word count from a text file.
#!/bin/bash

# Define the input file and the number of lines to display
input_file="your_text_file.txt"
N=10

# Check if the input file exists
if [ ! -f "$input_file" ]; then
    echo "Error: Input file not found: $input_file"
    exit 1
fi

# Use 'awk' to extract lines with word counts, sort, and display the top N lines
awk '{print NF, $0}' "$input_file" | sort -nr | head -n "$N" | cut -f2- -d' '
