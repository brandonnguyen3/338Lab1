def count_consonants(word):
    consonants = "bcdfghjklmnpqrstvwxyz"
    count = 0
    for letter in word:
        if letter.lower() in consonants:
            count += 1
    return count
file_path = r'C:\Users\ami_s\Downloads\ENSF_338\LAB1\pg2701.txt'
with open(file_path, 'r', encoding='utf-8') as file:
    lines = file.readlines()
total_consonants = 0
total_words = 0
start_counting = False
# this part of teh code was taken from chatgpt

# Iterate over each line in the file
for line in lines:
    # Check if the line contains the starting point
    if "CHAPTER 1. Loomings." in line or "Part 2.2. - Continued" in line:
        start_counting = True
        continue
    
    # Start counting consonants when the flag is True
    if start_counting:
        words = line.split()
        for word in words:
            total_consonants += count_consonants(word)
            total_words += 1

# chatgpt part ends here
average_consonants_per_word = total_consonants / total_words
print("Average number of consonants per word:", average_consonants_per_word)


