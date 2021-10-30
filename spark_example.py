from pyspark.sql import SparkSession
spark = SparkSession.builder.appName("New York City Taxi").getOrCreate()
