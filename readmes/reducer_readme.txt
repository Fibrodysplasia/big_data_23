# Reducer

# here we are using a defaultdict to easily keep only unique values
# we will count each word as products come in and then emit them

# there is a counter for testint purposes and two outputs, 
# one limits the output values to 50 words, the other 
# outputs all of them.

# the output is sorted. This will be passed to the script for generating
# visuals (wordcloud, treemap)
