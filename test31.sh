#!/bin/bash

# Input string
input_string="aapka_input_string_yahan_daliye"

# Ginti nikalein
char_count=$(echo "$input_string" | grep -o . | sort | uniq -c)

# Output dikhayein
echo "Character Counts:"
echo "$char_count"
