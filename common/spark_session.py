from pyspark.sql import SparkSession

def get_spark():

    spark = SparkSession.builder.appName("LocalPipeline").getOrCreate()
    
    return spark