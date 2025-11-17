from clickhouse_driver import Client
import time
import random

client = Client('localhost')

i = 1
print("Starting inserts...")
while True:
    client.execute(
        "INSERT INTO test_speed (id, value) VALUES",
        [(i, f"value_{random.randint(1, 10)}")]
    )
    print(f"Inserted row: {i}")
    i += 1
    time.sleep(0.01)   # 10ms delay
