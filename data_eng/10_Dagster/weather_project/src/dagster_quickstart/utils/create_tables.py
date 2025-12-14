# create_tables.py
import sqlite3

def create_tables(db_name="data.db"):
    conn = sqlite3.connect(db_name)
    cur = conn.cursor()

    # Raw hourly weather data
    cur.execute("""
    CREATE TABLE IF NOT EXISTS weather (
        date TEXT,
        time TEXT,
        temperature REAL,
        condition TEXT,
        humidity REAL,
        location_name TEXT,
        region TEXT,
        country TEXT,
        latitude REAL,
        longitude REAL,
        local_time TEXT,
        PRIMARY KEY (date, time, location_name)
    );
    """)

    # Daily aggregated summaries
    cur.execute("""
    CREATE TABLE IF NOT EXISTS daily_weather (
        location_name TEXT,
        date TEXT,
        max_temp REAL,
        min_temp REAL,
        avg_humidity REAL,
        PRIMARY KEY (location_name, date)
    );
    """)

    # Long-term city-wide averages
    cur.execute("""
    CREATE TABLE IF NOT EXISTS global_weather (
        location_name TEXT PRIMARY KEY,
        avg_max_temp REAL,
        avg_min_temp REAL,
        avg_humidity REAL
    );
    """)

    conn.commit()
    conn.close()

if __name__ == "__main__":
    create_tables()
    print("Tables created successfully")
