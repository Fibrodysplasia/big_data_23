#!/usr/bin/env/python

import sys

for line in sys.stdin:
    try:
        product, complaints = line.strip().split('\t')
        print(f"{product}, {complaints}")
    except ValueError:
        pass
