import os
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

def get_csv_path_from_user():
    # Get the user's home directory
    home_dir = os.path.expanduser("~")

    # Construct the full path to the Downloads folder
    downloads_folder = os.path.join(home_dir, 'Downloads')

    # Specify the file name
    csv_file_name = input("Enter the CSV file name (including extension): ")

    # Construct the full path to the CSV file
    csv_file_path = os.path.join(downloads_folder, csv_file_name)

    return csv_file_path

# Check if CSV file exists in Downloads folder
downloads_csv_path = os.path.join(os.path.expanduser("~"), 'Downloads', 'data.csv')
if os.path.exists(downloads_csv_path):
    csv_file_path = downloads_csv_path
else:
    # Prompt user for CSV file path
    csv_file_path = get_csv_path_from_user()

# Specify the output JSON file path
json_file_path = 'output.json'

# Call the csv_to_json function with the full paths
csv_to_json(csv_file_path, json_file_path)
