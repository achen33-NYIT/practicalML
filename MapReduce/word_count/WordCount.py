import re

word_count = {}
lines = []

# split each line in file on each word
with open("ofMiceAndMenIntro.txt", mode = "r") as file:
    for line in file:
        sentence = line.strip().lower().replace(",", "").replace(".", "").replace("-", "")
        words = re.split(' ', sentence)
        lines.append(words)

for line in lines:
    for word in line:
        if word not in word_count:
            word_count[word] = 1
        else:
            word_count[word] += 1

            
print(word_count)