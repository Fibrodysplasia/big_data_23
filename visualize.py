#!/usr/bin/env/python
import sys
import errno
import plotly.express as px
import numpy as np
# output will be used to store the output of the reducer
output = {}

for line in sys.stdin:
    # Here I'm just building a dictionary of dictionaries
    # to feed into the code that was written below
    category, values = line.strip().split(':', 1)
    output[category] = {}
    values_and_counts = values.strip().split(',')
    for data in values_and_counts:
        value, count = data.strip().split(': ')
        output[category][value] = count

# we can probably combine much of this logic

# names/parents are lists used for the treemap
names = ["Customer Complaints"]
parents = [""]
# loop through each key in the output of the reduce job
for key in output:
    names.append(key)   # add each key to names list
    parents.append("Customer Complaints")     # add the "Top 10 Complaints" parent for each key
    for key2 in output[key]:    # loop through each sub key, can set to top 20 or whatever is needed
        names.append(f'{key2} - {output[key][key2]}')   # add each key and corresponding word count to names list
        parents.append(key)     # add the key as the parent in the parents list
# pass the names and parents list to the treemap function
# for it to create the treemap
fig = px.treemap(
    names = names,
    parents = parents
)
fig.update_traces(root_color="lightgrey")
fig.update_layout(margin = dict(t=50, l=25, r=25, b=25))
fig.show()
