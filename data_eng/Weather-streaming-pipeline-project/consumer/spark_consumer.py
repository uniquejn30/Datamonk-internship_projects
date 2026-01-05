from pyspark.sql import SparkSession
from pyspark.sql.functions import from_json, col
from pyspark.sql.types import (
    StructType,
    StructField,
    StringType,
    DoubleType,
    IntegerType
)
from consumer.analytics import apply_transformations
from dotenv import load_dotenv
from pathlib import Path
import os


# Load environment variables
env_path = Path("config") / ".env"
load_dotenv(dotenv_path=env_path)


def start_spark_consumer():
    broker = os.getenv("KAFKA_BROKER")
    topic = os.getenv("KAFKA_TOPIC")

    spark = (
        SparkSession.builder
        .appName("WeatherConsumer")
        .config(
            "spark.jars.packages",
            "org.apache.spark:spark-sql-kafka-0-10_2.12:3.4.1"
        )
        .getOrCreate()
    )

    schema = StructType([
        StructField("timestamp", StringType(), True),
        StructField("city", StringType(), True),
        StructField("country", StringType(), True),
        StructField("temperature", DoubleType(), True),
        StructField("feels_like", DoubleType(), True),
        StructField("humidity", IntegerType(), True),
        StructField("pressure", IntegerType(), True),
        StructField("description", StringType(), True),
        StructField("wind_speed", DoubleType(), True),
        StructField("wind_direction", DoubleType(), True),
        StructField("cloudiness", IntegerType(), True),
        StructField("visibility", IntegerType(), True),
        StructField("latitude", DoubleType(), True),
        StructField("longitude", DoubleType(), True),
    ])

    kafka_df = (
        spark.readStream
        .format("kafka")
        .option("kafka.bootstrap.servers", broker)
        .option("subscribe", topic)
        .option("startingOffsets", "latest")
        .load()
    )

    value_df = kafka_df.selectExpr("CAST(value AS STRING)")

    weather_df = value_df.select(
        from_json(col("value"), schema).alias("data")
    ).select("data.*")

    transformed_df = apply_transformations(weather_df)

    query = (
        transformed_df.writeStream
        .outputMode("complete")
        .format("console")
        .option("checkpointLocation", "output/checkpoints")
        .start()
    )

    query.awaitTermination()
