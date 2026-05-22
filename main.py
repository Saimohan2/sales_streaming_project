from common.spark_session import get_spark

def main():

    spark = get_spark()

    print(spark)
    print(spark.sparkContext.master)

    spark.stop

if __name__ == "__main__":
    main()