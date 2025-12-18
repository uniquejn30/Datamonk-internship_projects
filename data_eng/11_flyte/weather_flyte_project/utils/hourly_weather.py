# hourly_weather.py
import sqlite3

def insert_hourly_weather(record, db_name="data.db"):
    conn = sqlite3.connect(db_name)
    cur = conn.cursor()

    cur.execute("""
    INSERT OR IGNORE INTO weather 
    (date, time, temperature, condition, humidity, location_name, region, country, latitude, longitude, local_time)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        record["date"], record["time"], record["temperature"], record["condition"], 
        record["humidity"], record["location_name"], record["region"], record["country"], 
        record["latitude"], record["longitude"], record["local_time"]
    ))

    conn.commit()
    conn.close()
