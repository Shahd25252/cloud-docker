
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from collections import Counter

nltk.download('stopwords')
input_file = 'paragraphs.txt'

with open(input_file, 'r') as file:
    text = file.read()

stop_words = set(stopwords.words('english'))

tokens = word_tokenize(text)

filtered_tokens = [word for word in tokens if word.lower() not in stop_words]

word_counts = Counter(filtered_tokens)

for word, count in word_counts.items():
    print(f"{word}: {count}")