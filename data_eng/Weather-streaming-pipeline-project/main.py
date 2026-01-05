# main.py
from threading import Thread
from setup_environment import setup_environment
from producer.weather_producer import start_weather_producer
from consumer.spark_consumer import start_spark_consumer

if __name__ == "__main__":
    setup_environment()

    producer_thread = Thread(target=start_weather_producer)
    producer_thread.start()

    start_spark_consumer()
