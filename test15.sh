##!/bin/bash

# XML file to parse
xml_file="example.xml"

# Define the XML tag you want to extract data from
xml_tag="element_to_extract"

# Use grep to extract lines containing the opening and closing tags
data_lines=$(grep -n "<$xml_tag\|</$xml_tag>" "$xml_file")

# Extract and format the data
parsed_data=""
start_tag=""
while read -r line; do
  if [[ $line == *"<$xml_tag"* ]]; then
    start_tag="$line"
  elif [[ $line == *"</$xml_tag>"* ]]; then
    parsed_data+="${start_tag%%:*}:${line##*>}"
  fi
done <<< "$data_lines"

# Display the parsed data
echo "Parsed Data:"
echo "$parsed_data"
