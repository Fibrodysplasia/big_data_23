#!/usr/bin/env/python

import sys
import re
import errno

for line in sys.stdin:
    try:
        product, words = line.split('\t')
        words = words.split()
        for word in words:
            # for some reason first word had [
            # and last word had ] 
            # and random commas and quotes made
            # it through. Probably something to do
            # with tokenization
            word = re.sub(r'[\[\],\']', '', word)
            print(f'{product}, {word}')
    except ValueError:
        pass
    except IOError:
        if IOError.errno == errno.EPIPE:
            pass
