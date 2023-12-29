import csv
import json

def csv_to_json(csv_file_path, json_file_path):
    data = []

    # Read CSV file and convert to list of dictionaries
    with open(csv_file_path, 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        data = list(csv_reader)

    # Write JSON file
    with open(json_file_path, 'w') as json_file:
        json.dump(data, json_file, indent=2)

# Example usage
csv_to_json('input.csv', 'output.json')
