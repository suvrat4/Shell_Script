#Write a shell script to calculate the difference between two dates in days, months, and years.

#!/bin/bash

# Check if the user provided two date strings as arguments
if [ $# -ne 2 ]; then
    echo "Usage: $0 <date1> <date2>"
    exit 1
fi

date1="$1"
date2="$2"

# Function to convert a date to the number of days since the epoch (January 1, 1970)
date_to_days_since_epoch() {
    date -d "$1" +%s
}

# Calculate the number of days since the epoch for both dates
days_since_epoch_date1=$(date_to_days_since_epoch "$date1")
days_since_epoch_date2=$(date_to_days_since_epoch "$date2")

# Calculate the difference in days
difference_in_days=$((days_since_epoch_date2 - days_since_epoch_date1))

# Calculate the difference in years, months, and days
years=$((difference_in_days / 365))
remainder_days=$((difference_in_days % 365))
months=$((remainder_days / 30))
days=$((remainder_days % 30))

# Display the results
echo "Difference:"
echo "Years: $years"
echo "Months: $months"
echo "Days: $days"
