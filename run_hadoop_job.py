import sys
import subprocess

def run_hadoop_job(mapper_path, combiner_path, reducer_path, input_path, output_path):
    command = [
        'hadoop',
        'jar',
        '../../../../../opt/hadoop/share/hadoop/tools/lib/hadoop-streaming-3.3.6.jar',
        '-files',
        f'{mapper_path},{combiner_path},{reducer_path}',
        '-mapper',
        mapper_path,
        '-combiner',
        combiner_path,
        '-reducer',
        reducer_path,
        '-input',
        input_path,
        '-output',
        output_path,
    ]
    try:
        subprocess.run(command, check=True, stderr=subprocess.STDOUT, text=True)
        print("Hadoop job completed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Hadoop job failed with exit code {e.returncode}. Error message: {e.output}")

if __name__  == "__main__":

    mapper_path = 'mapreduce/mapper.py'
    combiner_path = 'mapreduce/combiner.py'
    reducer_path = 'mapreduce/reducer.py'
    input_path = '../../HADOOP_DATA/input/filtered.csv'
    output_path = '../../HADOOP_DATA/output'
   
    run_hadoop_job(mapper_path, combiner_path, reducer_path, input_path, output_path)
