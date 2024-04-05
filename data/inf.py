import json
import os

# Function to read JSON files
def read_json_file(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data

# Function to write JSON data to a file
def write_json_file(data, file_path):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)

def extract_category(file_name):
    return file_name.replace('Infinity_', '').replace('.json', '').replace('_', ' ').lower()



# List to store combined JSON data
combined_data = []





# Aarong men
json_dir = './inf/men'
for filename in os.listdir(json_dir):
    if filename.endswith('.json'):
        file_path = os.path.join(json_dir, filename)
        # Read JSON file
        json_data = read_json_file(file_path)
        # Extract category from file name
        category = extract_category(filename)
        # Take the first 57 elements from the array
        for item in json_data:
            item['Category'] = item['Gender'] +" "+ item['Category']
            combined_data.append(item)

json_dir = './inf/women'
for filename in os.listdir(json_dir):
    if filename.endswith('.json'):
        file_path = os.path.join(json_dir, filename)
        # Read JSON file
        json_data = read_json_file(file_path)
        # Extract category from file name
        category = extract_category(filename)
        # Take the first 57 elements from the array
        for item in json_data:
            item['Category'] = item['Gender'] +" "+ item['Category']
            combined_data.append(item)


write_json_file(combined_data, 'infinity2.json')