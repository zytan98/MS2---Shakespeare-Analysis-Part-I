
with open("gutenberg.txt", encoding='utf-8') as f:
    contents = f.readlines()
    known_words = {}
    for line in contents:
        line = line.strip()
        # split the line into words
        words = line.split()
        for word in words:
            if word not in known_words:
                known_words.update({word: 1})
            else:
                known_words[word] = known_words.get(word,0)+1

known_words = dict(sorted(known_words.items(), key=lambda item: item[1]))

items = list(reversed(known_words.items()))[:100]

print(items)


