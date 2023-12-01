# Usage:

# Follow the instructions in data_readme.txt if you do not
# have a cleaned dataset already.

# Start your python environment
source venv/bin/activate

# Start hadoop
start-dfs.sh
start-yarn.sh

# Verify you have datanodes running
jps

# Create a symlink to your hadoop jar in the same directory as 
# the rest of the files if you want.
hadoop fs -createSymlink /path/to/hadoop.jar hadoop-streaming.jar

# Copy the filtered.csv file into hadoop dfs
hadoop fs -copyFromLocal filtered.csv /path/to/input/folder

# Open the run_hadoop_job.jar
# Change line 8 with the path to your hadoop-streaming.jar
# Change line 33 with the path to your input file on hadoop fs
# Change line 34 with the path to your output folder on hadoop fs
# Save and exit

# Run the job with the following
python run_hadoop_job.python

# If you get weird errors about files paths being incorrect 
# you will have to run the command manually so change
# line 36 below with the streaming jar path and 41, 42 with input, output:

hadoop jar /opt/hadoop/share/hadoop/tools/lib/hadoop-streaming*.jar \
-files 'mapreduce/mapper.py,mapreduce/combiner.py,mapreduce/reducer.py' \
-mapper 'python3 mapreduce/mapper.py' \
-combiner 'python3 mapreduce/combiner.py' \
-reducer 'python3 mapreduce/reducer.py' \
-input '/HADOOP_DATA/input/filtered.csv' \
-output '/HADOOP_DATA/output'

# Copy the output to local (save to the same folder as visualize.py for simplicity)
hadoop fs -copyToLocal /path/to/output/part-00000 /path/to/local/output.txt

# Now to visualize it:
pip install plotly_express==0.4.0

# Assuming visualize.py and your output.txt are in the same folder:
cat output.txt | python visualize.py

# Or to run the entire thing through with python:
cat filtered.csv | python mapreduce/mapper.py | python mapreduce/combiner.py | python mapreduce/reducer.py | python visualize.py

See the expected output in images/visual_out*.png
