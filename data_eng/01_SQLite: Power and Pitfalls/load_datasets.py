import sqlite3
import pandas as pd
import time

def load_csv_to_sqlite(csv_path, db_name, table_name, chunksize=None):
    """
    Loads a CSV into a SQLite database table.
    
    Parameters:
    - csv_path (str): Path to the CSV file.
    - db_name (str): SQLite database file name.
    - table_name (str): Target table name.
    - chunksize (int): Number of rows per chunk (for large files). If None, loads at once.
    """
    start = time.time()
    conn = sqlite3.connect(db_name)

    if chunksize:
        # Chunked loading for large files (reduces memory usage)
        for chunk in pd.read_csv(csv_path, chunksize=chunksize):
            chunk.to_sql(table_name, conn, if_exists="append", index=False)
    else:
        # Direct loading for small files
        df = pd.read_csv(csv_path)
        df.to_sql(table_name, conn, if_exists="replace", index=False)

    conn.close()
    end = time.time()
    print(f"Loaded {csv_path} into {db_name}.{table_name} in {end - start:.2f} sec")

# --- Load datasets ---

# Small dataset (fast load)
load_csv_to_sqlite("people_small.csv", "people_small.db", "people")

# Large dataset (chunked to reduce memory load)
load_csv_to_sqlite("people_large.csv", "people_large.db", "people", chunksize=50000)

# Jobs table (also large, same DB as large people dataset for JOIN)
load_csv_to_sqlite("jobs_large.csv", "people_large.db", "jobs", chunksize=50000)
