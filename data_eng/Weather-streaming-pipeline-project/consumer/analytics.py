# consumer/analytics.py
from pyspark.sql.functions import col, avg, max, min, window

def apply_transformations(df):
    return df.groupBy(
        window(col("timestamp"), "10 minutes"),
        col("city")
    ).agg(
        avg("temperature").alias("avg_temp"),
        max("temperature").alias("max_temp"),
        min("temperature").alias("min_temp"),
        avg("humidity").alias("avg_humidity")
    )
