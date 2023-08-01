import re

stop_words = []

with open("stopWords.txt", mode="r") as file:
    for line in file:
        stop_word = line.strip().lower()
        stop_words.append(stop_word)

word_count_with_stopwords = {}
lines = []


def setWord(word):
    if word not in word_count_with_stopwords:
        word_count_with_stopwords[word] = 1
    else:
        word_count_with_stopwords[word] += 1


with open("ofMiceAndMenIntro.txt", mode="r") as file:
    for line in file:
        sentence = line.strip().lower().replace(
            ",", "").replace(".", "").replace("-", "")
        words = re.split(' ', sentence)
        lines.append(words)

# print(stop_words)
for line in lines:
    for word in line:
        if word not in stop_words:  # only set word in dict if not in stop words
            setWord(word)

print(word_count_with_stopwords)
