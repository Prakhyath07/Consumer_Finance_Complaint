import os
from pyspark.sql import SparkSession

spark_session = SparkSession.builder.master('local[*]').appName('finance_complaint') \
    .config('spark.jars.packages',"com.amazonaws:aws-java-sdk:1.7.4,org.apache.hadoop:hadoop-aws:2.7.3")\
    .getOrCreate()
