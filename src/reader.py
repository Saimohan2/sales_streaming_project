from pyspark.sql import DataFrame

def read_data(spark) -> DataFrame:

    df = (spark.read.format("csv")
          .option("header", True)
          .option("inferSchema", True)
          .load("data\input\sample.csv"))

    return df