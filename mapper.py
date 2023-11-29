#/usr/bin/env/python

import sys
import nltk
import re
from nltk.corpus import stopwords
# from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
nltk.download('stopwords')
nltk.download('punkt')

stop_words = set(stopwords.words('english'))
# stemmer = PorterStemmer()

# Because there are inconsistancies in the structure of the customer
# complaints, after mapping we end up with some misinterpretations
# of the complaint text as new categories
# so if that occurs we will place the words in uncategorized
categories = [
        'debt collection',
        'mortgage',
        'credit reporting',
        'credit card or prepaid card']

# Some unhelpful words that showed up a lot as the only word in the list
# wasting network traffic and adding little-to-no value
extra_stops = [
        'nv',
        'ga',
        'com',
        'pymt',
        'mm',
        'dd',
        'yyyy',
        'mins',
        'secs',
        'seconds',
        'minutes',
        'x'
        ]

def process_text(text):
    text = ' '.join(text)
    # Remove anything that isn't an alphabet or space character
    text = re.sub(r'[^a-zA-Z\s]', ' ', text.lower())
    # Remove redacted things (XX/XX/XXX and XXXX for example)
    text = re.sub(r'\b(?:\w*xx\w*)\b', '', text)
    # tokenize and emit a list of words
    words = word_tokenize(text)
    # remove words that are stop words (if, then, the, as, etc)
    words = [word for word in words if((word.lower() not in stop_words) and (word.lower() not in extra_stops))]
    # Return a list of words to send to combiner
    return words

for line in sys.stdin:
    try:
        data = line.strip().split(',', 1)
        if len(data) < 2:
            pass
        else:
            # There were some product categories with weird " at the beginning
            data[0] = re.sub(r'[^a-zA-Z,\s]', '', data[0])
            product = data[0] if data[0].lower() in [cat.lower() for cat in categories] else 'Uncategorized'
            complaints = process_text(data[1:])
            # We don't want to waste traffic sending empty lists
            if complaints:
                print(f"{product}\t{complaints}")
            else:
                pass
    # catching all errors like this is poor practice
    except ValueError:
        pass
