import re
3  # BIGRAMS COUNT
word_count_bigrams = {}
bigrams = []
lines = []  # reinitializing globals


def setBigram(word):
    if word not in word_count_bigrams:
        word_count_bigrams[word] = 1
    else:
        word_count_bigrams[word] += 1


with open("ofMiceAndMenIntro.txt", mode="r") as file:
    for line in file:
        sentence = line.strip().lower().replace(
            ",", "").replace(".", "").replace("-", "")
        words = re.split(' ', sentence)
        lines.append(words)

for line in lines:
    for idx, word in enumerate(line):
        if idx == len(line) - 1:
            break
        else:
            bigram = f"{line[idx]},{line[idx + 1]}"
            bigrams.append(bigram)

for bigram in bigrams:
    setBigram(bigram)


print(word_count_bigrams)
