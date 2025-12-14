# daily_weather.py
import sqlite3

def aggregated_daily_weather(db_name="data.db"):
    conn = sqlite3.connect(db_name)
    cur = conn.cursor()

    cur.execute("""
    INSERT OR REPLACE INTO daily_weather (location_name, date, max_temp, min_temp, avg_humidity)
    SELECT location_name, date,
           MAX(temperature), MIN(temperature), AVG(humidity)
    FROM weather
    GROUP BY location_name, date;
    """)

    conn.commit()
    conn.close()
