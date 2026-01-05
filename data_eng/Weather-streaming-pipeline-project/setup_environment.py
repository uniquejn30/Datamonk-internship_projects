
# setup_environment.py
from kafka.admin import KafkaAdminClient, NewTopic
from dotenv import load_dotenv
from pathlib import Path
import os

env_path = Path("config") / ".env"
load_dotenv(dotenv_path=env_path)

def setup_kafka():
    broker = os.getenv("KAFKA_BROKER")
    topic = os.getenv("KAFKA_TOPIC")

    if not broker:
        raise ValueError("KAFKA_BROKER not found in .env file")

    admin_client = KafkaAdminClient(bootstrap_servers=broker)

    topic_list = [NewTopic(name=topic, num_partitions=3, replication_factor=1)]

    try:
        admin_client.create_topics(new_topics=topic_list, validate_only=False)
        print(f"Topic '{topic}' created successfully.")
    except Exception:
        print(f"Topic '{topic}' already exists.")

def setup_environment():
    setup_kafka()
    print("Environment setup completed successfully.")

if __name__ == "__main__":
    setup_environment()
