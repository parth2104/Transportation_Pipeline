from pyspark import pipelines as dp
from pyspark.sql.functions import *


@dp.view(
    name="trips_silver_staging"
)
def trips_silver():
    df= spark.readStream.table("driving.bronze.bronze_trip")
    df= df.withColumn("passenger_type", lower("passenger_type"))

    df = df.select(
         col("trip_id").alias("id"),
         col("date").cast("date").alias("business_date"),
         col("city_id").alias("city_id"),
         col("passenger_type").alias("passenger_category"),
         col("distance_travelled_km").alias("distance_kms"),
         col("fare_amount").alias("sales_amt"),
         col("passenger_rating").alias("passenger_rating"),
         col("driver_rating").alias("driver_rating"),
         col("Ingestion_date_time").alias("bronze_ingest_timestamp"),
    )


    return df


dp.create_streaming_table(
    name="driving.silver.trips"
)

dp.create_auto_cdc_flow(
    target="driving.silver.trips",
    source="trips_silver_staging",
    keys=["id"],
    sequence_by="bronze_ingest_timestamp",
    stored_as_scd_type=1,
    except_column_list=[],
)
