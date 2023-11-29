# Mapper

# Here we have the input in the form <'product string'\t'string of words'>
# we are using nltk to get stopwords, the PorterStemmer, and to tokenize the words in the complaint
# I ultimately took out the stemmer because having word fragments (secur instead of security, for example)
# and thought they will look strange on the word cloud/treemap comparison

# While in your python environment you will need to pip install nltk

# We define a function which processes the text
# First we use re.sub to replace non-words, punctuation, and then convert to lowercase
# Next we again use the re.sub to remove XX/XX/XXXX and words that are only X's (i.e XXXX and XXXXXX)
# The re module is installed with python, no need for install

# After regex we use nltk to tokenize the words and then emit the ones if not in stopwords
# We will send this list to a combiner which will count each word. See combiner_readme.txt
# Use maptest.csv to test, see maptest.png for example output
