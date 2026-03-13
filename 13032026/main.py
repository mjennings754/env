# word frequency counter
import string
from collections import Counter

text = input("Enter a paragraph: ")
text = text.lower()
text = text.translate(str.maketrans('', '', string.punctuation))

words = text.split()

word_counts = Counter(words)

for word, count in word_counts.most_common(5):
    print(word, ":", count)
    