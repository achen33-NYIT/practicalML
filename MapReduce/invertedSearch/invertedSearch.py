import re
4  # INVERTED INDEX

document1 = []
document2 = []
document3 = []

word_source = {}

with open("ofMiceAndMenIntro.txt", mode="r") as file:
    for line in file:
        sentence = line.strip().lower().replace(",", "").replace(
            ".", "").replace("-", "").replace("'", "").replace('"', "")
        words = re.split(' ', sentence)
        document1.append(words)


flattened_doc1_list = [word for line in document1 for word in line]


with open("ofMiceAndMenCh2.txt", mode="r") as file:
    for line in file:
        sentence = line.strip().lower().replace(",", "").replace(
            ".", "").replace("-", "").replace("'", "").replace('"', "")
        words = re.split(' ', sentence)
        document2.append(words)

flattened_doc2_list = [word for line in document2 for word in line]


with open("ofMiceAndMenCh3.txt", mode="r") as file:
    for line in file:
        sentence = line.strip().lower().replace(",", "").replace(
            ".", "").replace("-", "").replace("'", "").replace('"', "")
        words = re.split(' ', sentence)
        document3.append(words)

flattened_doc3_list = [word for line in document3 for word in line]

# combine list and then loop checking if word in combined list is in each of source lists
combined_list = flattened_doc1_list + flattened_doc2_list + flattened_doc3_list

combined_list_no_dups = list(set(combined_list))

# create dictionary from words from combined list
for word in combined_list:
    if (word in flattened_doc1_list) and (word in flattened_doc2_list) and (word in flattened_doc3_list):
        word_source[word] = f'"Document 1, "Document 2", "Document 3"'
    elif (word in flattened_doc1_list) and (word in flattened_doc2_list):
        word_source[word] = f'"Document 1, "Document 2"'
    elif (word in flattened_doc1_list) and (word in flattened_doc3_list):
        word_source[word] = f'"Document 1, "Document 3"'
    elif (word in flattened_doc2_list) and (word in flattened_doc3_list):
        word_source[word] = f'"Document 2", "Document 3"'
    elif word in flattened_doc1_list:
        word_source[word] = f'"Document 1"'
    elif word in flattened_doc2_list:
        word_source[word] = f'"Document 2"'
    elif word in flattened_doc3_list:
        word_source[word] = f'"Document 3"'

print(word_source)
