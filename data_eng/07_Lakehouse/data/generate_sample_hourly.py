import csv
from datetime import datetime, timedelta
import random
import os

os.makedirs("data", exist_ok=True)
start = datetime(2025, 5, 17, 0, 0)
rows = []
cities = ["Mumbai","Delhi","Bengaluru","Kolkata"]
for city in cities:
    for h in range(48):  # 2 days * 24 hours
        t = start + timedelta(hours=h)
        rows.append({
            "time": t.strftime("%Y-%m-%d %H:%M"),
            "location_name": city,
            "temperature": round(random.uniform(20, 35), 1),
            "humidity": round(random.uniform(40, 85), 1),
            "weather_desc": random.choice(["Sunny","Cloudy","Rain","Clear"])
        })

with open("data/hourly_weather.csv", "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=["time","location_name","temperature","humidity","weather_desc"])
    writer.writeheader()
    writer.writerows(rows)

print("Successfully created data/hourly_weather.csv")
