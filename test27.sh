#Write a shell script that takes a string as input and uses a while loop to print the characters of the string in reverse order.
#!/bin/bash

# Prompt the user for input
echo "Enter a string: "
read input_string

# Initialize variables
len=${#input_string}
reverse_string=""

# Use a while loop to reverse the string
while [ $len -gt 0 ]; do
    # Get the last character of the string
    last_char="${input_string: -1}"

    # Append the last character to the reversed string
    reverse_string="$reverse_string$last_char"

    # Remove the last character from the input string
    input_string="${input_string:0:($len-1)}"

    # Decrement the length
    len=$((len - 1))
done

# Print the reversed string
echo "Reversed string: $reverse_string"
