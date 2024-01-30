import json
import timeit

# Step 1: Read the JSON file
with open('large-file.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

# Step 2: Modify the 'size' field in every record to the value 35
def modify_field():
    for record in data:
        record['size'] = 35

#check how long it takes to modify the 'size' field
elapsed_time = timeit.timeit(modify_field, number=10)
print(f'Time taken to modify size field: {elapsed_time} seconds')

# Step 3: Write the modified data back to a new JSON file in reverse order
output_data = list(reversed(data))
with open('output.2.3.json', 'w') as output_file:
    json.dump(output_data, output_file, indent=2)

print("Operation completed successfully.")


