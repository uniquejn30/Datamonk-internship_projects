import sqlite3
import time

# Function to run a query and measure time
def run_query(db_name, query, description):
    conn = sqlite3.connect(db_name)
    cur = conn.cursor()
    start = time.time()
    try:
        cur.execute(query)
        results = cur.fetchall()
    except sqlite3.OperationalError as e:
        results = []
        print(f"Error: {e}")
    end = time.time()
    conn.close()

    print(f"\nQuery: {description}")
    print(f"Time taken: {end - start:.4f} sec")
    print("Results (first 5 rows):", results[:5])

# ======== queries ========
queries = [
    ("SELECT COUNT(*) FROM people;", "Count total people"),
    ("SELECT * FROM people WHERE age > 50;", "People older than 50"),
    ("""
    SELECT p."Job Title", AVG(j.Salary)
    FROM people p
    JOIN jobs j
    ON p."Job Title" = j."Job Title"
    GROUP BY p."Job Title";
    """, "Average salary by job title"),
    ("""
    SELECT p.Name, p."Job Title", j.Salary
    FROM people p
    JOIN jobs j
    ON p."Job Title" = j."Job Title"
    ORDER BY j.Salary DESC
    LIMIT 5;
    """, "Top 5 highest-paid people"),
    ("SELECT Country, COUNT(*) FROM people GROUP BY Country;", "People per country")
]

# ======== Run on small dataset ========
print("===== Small Dataset =====")
for q, desc in queries[:2]:  # first 2 queries only
    run_query("people_small.db", q, desc)

# ======== Run on large dataset ========
print("\n===== Large Dataset =====")
for q, desc in queries:  # run all queries
    run_query("people_large.db", q, desc)
