import json
import matplotlib.pyplot as plt

with open('songdata.json', 'r') as file:
    data = json.load(file)
songs_below_minus_8 = [song for song in data if song['loudness'] < -8]
songs_at_or_above_minus_8 = [song for song in data if song['loudness'] >= -8]
tempo_below_minus_8 = [song['tempo'] for song in songs_below_minus_8]
tempo_at_or_above_minus_8 = [song['tempo'] for song in songs_at_or_above_minus_8]

# Chatgpt generated
plt.figure(figsize=(10, 6))

plt.subplot(2, 1, 1)
plt.hist(tempo_below_minus_8, bins=20, color='blue', alpha=0.7)
plt.title('Distribution of Tempo for Songs with Loudness Below -8')
plt.xlabel('Tempo')
plt.ylabel('Frequency')

plt.subplot(2, 1, 2)
plt.hist(tempo_at_or_above_minus_8, bins=20, color='green', alpha=0.7)
plt.title('Distribution of Tempo for Songs with Loudness At or Above -8')
plt.xlabel('Tempo')
plt.ylabel('Frequency')

plt.tight_layout()

# end of chatgpt
plt.savefig('hist1.png')
plt.savefig('hist2.png')
plt.show()
