from common.spark_session import get_spark
from reader import read_data
from transformations.transform import transform_data
from common.config_loader import load_config

def main():

    spark = get_spark()

    print(spark)
    print(spark.sparkContext.master)

    config = load_config("src\configs\config.yaml")

    print(config)
    print(type(config))

    df = read_data(spark, config)
    # print(df)
    # just tested logic
    # df = df.coalesce(2)
    # print("Partitions: ", df.rdd.getNumPartitions())
    df = transform_data(df, config)
    
    df.show()

    spark.stop()

if __name__ == "__main__":
    main()