from pyspark.sql.types import *
from pyspark.sql.functions import * 
from pyspark import pipelines as dp

source = '/Volumes/driving/bronze/trips/'

@dp.table(
    name='driving.bronze.bronze_trip'
)
def trip():
    
    df = spark.readStream.format("cloudFiles") \
        .option("cloudFiles.format", "csv") \
        .option("cloudFiles.inferColumnTypes", "true") \
        .option("cloudFiles.schemaEvolutionMode", "rescue") \
        .option("cloudFiles.maxFilesPerTrigger", 100) \
        .load(source)

    df = df.withColumnRenamed("distance_travelled(km)", "distance_travelled_km")
    df = df.withColumn('Ingestion_date_time', current_timestamp())
    return df
