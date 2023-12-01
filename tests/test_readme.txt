# To test the dataset we have a test validation_test.txt
# this has two lines:

Random Name, wordone wordtwo wordtwo wordthree wordthree wordthree
Mortgage, XXXX XX/XX/XXXX wordone wordtwo wordtwo wordfour wordfour wordfour wordfour

# To run the test, from the tests directory run:
cat validation_test.txt | python ../mapreduce/mapper.py | python ../mapreduce/combiner.py | python ../mapreduce/reducer.py

# We expect the following output when running it through mapreduce:
Uncategorized: {'wordthree': 3, 'wordtwo': 2, 'wordone': 1}
Mortgage: {'wordfour': 4, 'wordtwo': 2, 'wordone': 1}

# This is because Random Name is not in the list of categories specified
# and is converted to Random Name. Also notice the redacted bits are 
# removed.

# You can see an example of this output in terminal 
# at ../images validation_test_out.png
# and a copy of the output in tests/validation_output.txt