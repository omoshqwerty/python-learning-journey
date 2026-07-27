fav = input("What is your favourite language and why? ")
words = fav.split(" ")
total = len(words)
long = max(words, key=len)
capitalized_words = []
for w in words:
    capitalized_words.append(w.capitalize())
title_sentence = " ".join(capitalized_words)
print(f"Sentence: {title_sentence}")
print(f"Total words: {total}")
print(f"Longest word: {long}")
