from pyspark.sql import DataFrame
from pyspark.sql import functions as F

def transform_data(df: DataFrame) -> DataFrame:

    # clean df

    df = (df.dropna(subset = ["name", "age"])
          .withColumn("city", F.trim(F.col("city")))
          )

    # Filter rows

    df = df.filter(F.col("age")>25)

    # add new column
    df = (df.withColumn("age_group", F.when(F.col("age")>40, F.lit("senior"))
                                        .otherwise(F.lit("adult")))
                                        )
    
    return df