#Write a shell script that takes a user input string and performs the following operations:

Count and print the number of vowels (a, e, i, o, u) in the input string.
Check if the input string is a palindrome (reads the same forwards and backwards) and print "Palindrome" or "Not a Palindrome" accordingly.
Extract all unique words from the input string (words are separated by spaces) and print them in alphabetical order.
Ensure that your script handles user input and errors gracefully.

#!/bin/bash

# Function to count vowels
count_vowels() {
  local input="$1"
  local vowel_count=0

  for ((i = 0; i < ${#input}; i++)); do
    char="${input:$i:1}"
    case "$char" in
      [aeiouAEIOU]) ((vowel_count++));;
    esac
  done

  echo "Number of vowels in the string: $vowel_count"
}

# Function to check if a string is a palindrome
is_palindrome() {
  local input="$1"
  local reversed=""
  
  for ((i = ${#input} - 1; i >= 0; i--)); do
    reversed="$reversed${input:$i:1}"
  done

  if [ "$input" == "$reversed" ]; then
    echo "Palindrome"
  else
    echo "Not a Palindrome"
  fi
}

# Function to extract unique words and sort them alphabetically
extract_unique_words() {
  local input="$1"
  local words=()
  
  # Use awk to split the input into words and remove duplicates
  words=($(echo "$input" | awk '{for(i=1;i<=NF;i++) print $i}' | sort -u))

  echo "Unique words in alphabetical order:"
  for word in "${words[@]}"; do
    echo "$word"
  done
}

# Read user input
echo "Enter a string: "
read input_string

# Call functions and print results
count_vowels "$input_string"
is_palindrome "$input_string"
extract_unique_words "$input_string"
