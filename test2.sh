#Create a shell script that parses CSV files and performs calculations on the data (e.g., sum, average).
#!/bin/bash

# Check if the user provided a CSV file as an argument
if [ $# -ne 1 ]; then
    echo "Usage: $0 <csv_file>"
    exit 1
fi

csv_file="$1"

# Check if the provided file exists
if [ ! -f "$csv_file" ]; then
    echo "File '$csv_file' does not exist."
    exit 1
fi

# Function to calculate the sum of values in a column
calculate_sum() {
    column_number=$1
    awk -F ',' -v col="$column_number" '{sum += $col} END {print sum}' "$csv_file"
}

# Function to calculate the average of values in a column
calculate_average() {
    column_number=$1
    awk -F ',' -v col="$column_number" '{sum += $col; count++} END {print sum / count}' "$csv_file"
}

# Prompt the user to select a column for calculations
echo "Columns in the CSV file:"
head -n 1 "$csv_file" | tr ',' '\n' | cat -n
read -p "Enter the column number for calculations: " column_number

# Perform calculations based on user choice
echo "Calculations for column $column_number in '$csv_file':"
echo "Sum: $(calculate_sum $column_number)"
echo "Average: $(calculate_average $column_number)"
