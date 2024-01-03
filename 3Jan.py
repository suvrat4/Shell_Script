import prettytable
import json
import re

json_file_path = 'output.json'

# Function to recursively remove leading and trailing whitespaces in a JSON object
def clean_json(obj):
    if isinstance(obj, dict):
        return {key.strip(): clean_json(value) for key, value in obj.items()}
    elif isinstance(obj, list):
        return [clean_json(element) for element in obj]
    elif isinstance(obj, str):
        # Replace consecutive whitespace characters with a single space
        return re.sub(r'\s+', ' ', obj).strip()
    else:
        return obj

try:
    with open(json_file_path, 'r', encoding='utf-8') as file:
        json_content = file.read()
        cleaned_json_content = json.loads(json_content, object_hook=clean_json)
except json.JSONDecodeError as e:
    print(f"Error decoding JSON: {e}")
    problematic_part = json_content[e.pos:e.pos + 10]  # Print the problematic part of the JSON
    print(f"Problematic part of JSON: {problematic_part}")
    exit(1)

# Rest of your code using the 'cleaned_json_content' variable
for entry in cleaned_json_content:
    # Your processing logic here
    timestamp = entry["_time"]
    host = entry["host"]
    source = entry["source"]
    event_type = entry["eventtype"]
    msg_type = entry["msg_type"]
    proc_code = entry["proc_code"]
    resp_code = entry["resp_code"]
    trace_no = entry["trace_no"]

    table.add_row([timestamp, host, source, event_type, msg_type, proc_code, resp_code, trace_no])

# Print the table
print(table)
