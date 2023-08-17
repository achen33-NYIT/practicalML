from pyspark import SparkContext, SparkConf
import re
import json

# Step 1: Set Up the Spark Environment
conf = SparkConf().setAppName('WordCountApp')
sc = SparkContext(conf=conf)

# Step 2: Load the Data
input_file_path = "s3://your-bucket-name/ofMiceAndMenIntro.txt"
lines = sc.textFile(input_file_path)

# Step 3: Process the Data
def clean_and_split_line(line):
    sentence = line.strip().lower().replace(",", "").replace(".", "").replace("-", "")
    words = re.split(' ', sentence)
    return words

# FlatMap: It produces multiple output elements for each input element
# Map: It produces one output element for each input element
# ReduceByKey: It groups the elements with the same key (word in this case) and reduces them by applying the provided function (in this case summing them)
word_count = (lines
              .flatMap(clean_and_split_line) # split each line into words
              .map(lambda word: (word, 1)) # map each word to a pair <word, 1>
              .reduceByKey(lambda a, b: a + b)) # sum counts for each word

# Step 4: Save the Data to S3
output_file_path = "s3://your-bucket-name/output"
word_count_json = word_count.map(lambda x: json.dumps({x[0]: x[1]}))
word_count_json.saveAsTextFile(output_file_path)

# Stop the SparkContext
sc.stop()
