import json
import timeit
from matplotlib import pyplot as plt
import numpy as np

# Step 1: Read the JSON file
with open('large-file.json', 'r', encoding='utf-8') as file:
    data = json.load(file)
    
tests = [1000, 2000, 5000, 10000]
avgtimes = []

# Step 2: Modify the 'size' field in every record to the value 35
def modify_field(trial):
    for record in data[:trial]: 
        record['size'] = 35

#check how long it takes to modify the 'size' field
#Compute the time it takes to process the first 1000, 2000, 5000, and 10000 records
#use the code in the github class repo to plot the results
for trial in tests:
    elapsed_time = timeit.timeit(lambda:modify_field(trial), number=100)
    average_time = elapsed_time/100
    avgtimes.append(average_time)
    print(f'Average time taken to process the first {trial}: {average_time:.8f} seconds')

slope, intercept = np.polyfit(tests, avgtimes, 1)
plt.scatter(tests, avgtimes, label='Data points', color='purple')
linevalues = [slope * x + intercept for x in tests]
plt.plot(tests, linevalues, label='Linear regression', color='red')

plt.xlabel('Records Processed')
plt.ylabel('Average Time')
plt.title('Linear Regression Plot')
plt.legend()
plt.savefig('output.3.2.png')
plt.show()

# Step 3: Write the modified data back to a new JSON file in reverse order
output_data = list(reversed(data))
with open('output.2.3.json', 'w') as output_file:
    json.dump(output_data, output_file, indent=2)

print("Operation completed successfully.")


