import pandas as pd

# Load the uploaded CSV to inspect its structure
file_path = "/home/cooldude/Desktop/Datamonk_Projects/data_eng/05_Postgres_sql/PostgreSQL_Project/02_scale_speed"
df = pd.read_csv(file_path, nrows=5)  # load only first few rows for preview
df.head()
