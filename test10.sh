# Parse json file and keep the data in a tabular format shell script

[
  {
    "name": "John",
    "age": 30,
    "city": "New York"
  },
  {
    "name": "Alice",
    "age": 25,
    "city": "Los Angeles"
  }
]

====================================
#!/bin/bash

# Use jq to extract JSON data and format it as tab-separated values
jq -r '.[] | [.name, .age, .city] | @tsv' data.json > table.txt

# Print the tabular data
cat table.txt

# Optionally, you can clean up the temporary file
# rm table.txt
