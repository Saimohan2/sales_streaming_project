from common.spark_session import get_spark
from reader import read_data
from transformations.transform import transform_data

def main():

    spark = get_spark()

    print(spark)
    print(spark.sparkContext.master)

    df = read_data(spark)
    # print(df)
    # just tested logic
    # df = df.coalesce(2)
    # print("Partitions: ", df.rdd.getNumPartitions())
    df = transform_data(df)
    
    df.show()

    spark.stop()

if __name__ == "__main__":
    main()