import timeit
def count_vowels(word):
    vowels = "aeiou"
    count = 0
    for letter in word:
        if letter.lower() in vowels:
            count += 1
    return count
file_path = 'pg2701.txt'
with open(file_path, 'r', encoding='utf-8') as file:
    lines = file.readlines()
total_vowels = 0
total_words = 0
start_counting = False
# This loop was generated using chatgpt
# Iterate over each line in the file (exclude from timing)
for line in lines:
    # Check if the line contains the starting point
    if "CHAPTER 1. Loomings." in line or "Part 2.2. - Continued" in line:
        start_counting = True
        continue
    
    # Start counting vowels when the flag is True (exclude from timing)
    if start_counting:
        words = line.split()
        for word in words:
            total_vowels += count_vowels(word)
            total_words += 1

# Chatgpt ends
def compute_average_vowels():
    return total_vowels / total_words
time_taken = timeit.timeit(compute_average_vowels, number=100)
average_time = time_taken / 100
print("Average time taken across 100 repetitions:", average_time)

