from pyspark.sql.types import *
from pyspark.sql.functions import *
from pyspark import pipelines as dp
source='/Volumes/driving/bronze/city'

@dp.materialized_view(  
    name='city_bronze'
)
def city_bronze():
    df= spark.read.format('csv')\
        .option('header',True)\
        .option('inferSchema',True)\
        .option('mode','PERMISSIVE')\
        .option('mergeSchema',True)\
        .option('columnNameOfCorruptRecord','corrupt_record')\
        .load(source)
    df= df.withColumn('ingestion_Time',current_timestamp())\
        .withColumn('file_name',col('_metadata.file_path'))
    return df