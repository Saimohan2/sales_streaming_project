from pyspark.sql import DataFrame

def read_data(spark, config) -> DataFrame:
    
    input_path = config["input"]

    df = (spark.read.format(input_path["format"])
          .option("header", input_path["header"])
          .option("inferSchema", input_path["inferSchema"])
          .load(input_path["path"]))

    return df