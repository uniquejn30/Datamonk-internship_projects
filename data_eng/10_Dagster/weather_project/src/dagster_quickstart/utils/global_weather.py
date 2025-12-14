# global_weather.py
import sqlite3

def aggregated_global_weather(db_name="data.db"):
    conn = sqlite3.connect(db_name)
    cur = conn.cursor()

    cur.execute("""
    INSERT INTO global_weather (location_name, avg_max_temp, avg_min_temp, avg_humidity)
    SELECT location_name,
           AVG(max_temp), AVG(min_temp), AVG(avg_humidity)
    FROM daily_weather
    GROUP BY location_name
    ON CONFLICT(location_name) DO UPDATE SET
        avg_max_temp=excluded.avg_max_temp,
        avg_min_temp=excluded.avg_min_temp,
        avg_humidity=excluded.avg_humidity;
    """)

    conn.commit()
    conn.close()
