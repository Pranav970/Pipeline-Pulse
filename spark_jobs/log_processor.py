from pyspark.sql import SparkSession
spark=SparkSession.builder.appName('processor').master('local[*]').getOrCreate()
print('Spark processor initialized')
