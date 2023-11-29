#!/usr/bin/env/python

import sys
from collections import defaultdict, Counter
from operator import itemgetter
import errno

current_product = None
# Using a defaultdict to easily limit to unique values
products = defaultdict(set)
word_counts = defaultdict(Counter)
counter = 0

for line in sys.stdin:
    try:
        product, word = line.strip().split(',')
        # First product
        word_counts[product][word] += 1

        # counter is for testing with various numbers
        # you can print the counter to be sure the 
        # program isn't hanging
        print(counter)
        counter += 1
    except ValueError:
        pass
    except IOError:
        if IOError.errno == errno.EPIPE:
            pass
    if counter >= 100000:
        break
# We have to convert the counter dict to a normal one
result = {product: dict(count) for product, count in word_counts.items()}

# For testing the output use limited values, 
# too many at a time looks horrible in terminal
# Otherwise use the other to print everything
for product, values in result.items():
    # test
    limited_values = dict(sorted(values.items(), key=itemgetter(1), reverse=True)[:50])
    print(f'{product}: {limited_values}')

    # actual
    # sorted_values = dict(sorted(values.items(), key=itemgetter(1), reverse=True)
    # print(f'{product}: {sorted_values}')
