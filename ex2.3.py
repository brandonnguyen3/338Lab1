import json

# Step 1: Read the JSON file
with open('large-file.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

# Step 2: Modify the 'size' field in every record to the value 35
for record in data:
    record['size'] = 35

# Step 3: Write the modified data back to a new JSON file in reverse order
output_data = list(reversed(data))
with open('output.2.3.json', 'w') as output_file:
    json.dump(output_data, output_file, indent=2)

print("Operation completed successfully.")


