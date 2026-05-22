from pyspark.sql import DataFrame
from pyspark.sql import functions as F

def transform_data(df: DataFrame, config) -> DataFrame:
    
    rules = config["transform"]

    # clean df

    df = (df.dropna(subset = ["name", "age"])
          .withColumn("city", F.trim(F.col("city")))
          )

    # Filter rows

    df = df.filter(F.col("age")>rules["age_threshold"])

    # add new column
    df = (df.withColumn("age_group", F.when(F.col("age")>rules["senior_age"], F.lit("senior"))
                                        .otherwise(F.lit("adult")))
                                        )
    
    return df