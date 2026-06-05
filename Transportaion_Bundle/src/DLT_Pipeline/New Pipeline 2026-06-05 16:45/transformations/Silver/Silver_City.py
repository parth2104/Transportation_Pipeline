from pyspark.sql.functions import *
from pyspark.sql.types import *
from pyspark import pipelines as dp

@dp.materialized_view(
    name='driving.silver.city_silver'
)
def city_silver():
    df_bronze= spark.read.table("driving.bronze.city_bronze")
    df_silver= df_bronze.withColumn('time_stemp',current_timestamp())
    return df_silver