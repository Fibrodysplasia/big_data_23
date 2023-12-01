#!/usr/bin/env/python

import sys
from collections import defaultdict, Counter
from operator import itemgetter
import errno

current_product = None
# Using a defaultdict to easily limit to unique values
word_counts = defaultdict(Counter)
counter = 0

for line in sys.stdin:
    try:
        product, word = line.strip().split(',')
        word_counts[product][word] += 1

        # counter is for testing with various numbers
        # you can print the counter to be sure the 
        # program isn't hanging
        # print(counter)
        counter += 1
    except ValueError:
        pass
    except IOError:
        if IOError.errno == errno.EPIPE:
            pass
    # Take 10 million for testing (this may cause a broke pipe error if ran in hadoop)
    if counter >= 10000000:
       break
# We have to convert the counter dict to a normal one
result = {product: dict(count) for product, count in word_counts.items()}

# For testing the output use limited values,
# too many at a time looks horrible in terminal
# Otherwise use the other to print everything
for product, values in result.items():
    try:
        # test taking only the top 20 words
        # getting more than that was making the
        # output visuals very busy
        limited_values = dict(sorted(values.items(), key=itemgetter(1), reverse=True)[:20])
        print(f'{product}: {limited_values}')

        # in production you might want all the values for further 
        # insights (ML, NLP, sentiment analysis etc)
        # sorted_values = dict(sorted(values.items(), key=itemgetter(1), reverse=True)
        # print(f'{product}: {sorted_values}')
    except ValueError:
        pass
    except IOError:
        if IOError.errno == errno.EPIPE:
            pass
