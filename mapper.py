#!/usr/bin/env/python

import sys
import nltk
import re
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
nltk.download('stopwords')
nltk.download('punkt')

stop_words = set(stopwords.words('english'))
stemmer = PorterStemmer()

def process_text(text):
    # Clean up the data, see readme
    text = re.sub(r'[^\w\s]', '', text.lower())
    text = re.sub(r'\b[xX]+\b', '', text)
    text = re.sub(r'\b(?:xX{2}\/xX{2}\/xX{4})\b', '', text)
    words = word_tokenize(text)
    words = [word for word in words if word.lower() not in stop_words]

    return ' '.join(words)

for line in sys.stdin:
    try:
        product, complaints = line.strip().split('\t')
        processed_complaints = process_text(complaints)
        print(f"{product}, {processed_complaints}")
    except ValueError:
        pass
