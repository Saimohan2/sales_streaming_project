from pyspark.sql import DataFrame

def write_data(df: DataFrame, config):

    output_config = config["output"]

    writer = df.write.format(output_config["format"]).mode(output_config["mode"])

    if "partitionBy" in output_config:

        writer.partitionBy(output_config["partitionBy"])
    
    writer.save(output_config["path"])