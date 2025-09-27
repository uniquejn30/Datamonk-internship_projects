# ==============================================================================
# STEP 1: SETUP AND LOADING THE DATA
# ==============================================================================
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

print("--- Starting Data Loading ---")

# Connect to the SQLite database
conn = sqlite3.connect('sqlite-sakila.db')

# Load all tables into a dictionary of DataFrames
dfs = {}
table_names_query = "SELECT name FROM sqlite_master WHERE type='table';"
table_names = pd.read_sql_query(table_names_query, conn)['name'].tolist()

for table in table_names:
    dfs[table] = pd.read_sql_query(f'SELECT * FROM {table}', conn)
    print(f'Loaded table: {table}')

conn.close()

# Create variables for easier access to DataFrames
df_rental = dfs['rental']
df_inventory = dfs['inventory']
df_film = dfs['film']
df_category = dfs['category']
df_category_film = dfs['film_category']
df_payment = dfs['payment']
df_customer = dfs['customer']
df_store = dfs['store']


# ==============================================================================
# STEP 2: DATA CLEANING AND PREPARATION (THE ROBUST FIX)
# ==============================================================================
# NOTE: This is the most important fix. We convert the date columns here, ONCE.
# 'errors=coerce' will turn any unparseable date into 'NaT' (Not a Time),
# which prevents TypeErrors and ensures the columns are in datetime format.
df_rental['rental_date'] = pd.to_datetime(df_rental['rental_date'], errors='coerce')
df_rental['return_date'] = pd.to_datetime(df_rental['return_date'], errors='coerce')


print("\n--- Data Loading and Cleaning Complete ---\n")


# ==============================================================================
# STEP 3: ANALYSIS OF MONTHLY RENTAL TRENDS
# ==============================================================================
print("--- Analyzing Monthly Rentals ---")
# Calculate rentals per month using the now-corrected 'rental_date' column
monthly_rentals = (
    df_rental
    .assign(month=df_rental['rental_date'].dt.strftime('%Y-%m'))
    .groupby('month', as_index=False)
    .size()
    .rename(columns={'size': 'rentals'})
    .sort_values('month')
)

# Visualize Monthly Rentals
plt.figure(figsize=(10, 5))
plt.plot(monthly_rentals['month'], monthly_rentals['rentals'], marker='o', color='skyblue')
plt.title('Monthly Rental Over Time')
plt.xlabel('Month')
plt.ylabel('Number of Rentals')
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.show()


# ==============================================================================
# STEP 4: TOP 10 MOST RENTED FILMS
# ==============================================================================
print("\n--- Analyzing Top 10 Rented Films ---")
# Merge tables to link rentals to film titles
merged_films = (
    df_rental
    .merge(df_inventory.drop(columns=['last_update']), on='inventory_id')
    .merge(df_film.drop(columns=['last_update']), on='film_id')
)

# Calculate the top 10 most rented films
top_10_films = (
    merged_films.groupby('title', as_index=False)
    .size()
    .rename(columns={'size': 'rentals'})
    .sort_values('rentals', ascending=False)
    .head(10)
)

# Visualize Top 10 Films
plt.figure(figsize=(10, 5))
plt.bar(top_10_films['title'], top_10_films['rentals'])
plt.title('Top 10 Films Rented')
plt.xlabel('Films')
plt.ylabel('Number of Rentals')
plt.xticks(rotation=45, ha="right")
plt.grid(axis='y')
plt.tight_layout()
plt.show()


# ==============================================================================
# STEP 5: RENTALS BY CATEGORY
# ==============================================================================
print("\n--- Analyzing Rentals by Category ---")
# Merge tables to link rentals to categories
category_merged = (
    df_rental
    .merge(df_inventory.drop(columns=["last_update"]), on='inventory_id')
    .merge(df_category_film.drop(columns=["last_update"]), on='film_id')
    .merge(df_category.drop(columns=["last_update"]), on='category_id')
)

# Calculate rentals for each category
category_rentals = (
    category_merged.groupby("name", as_index=False)
    .size()
    .rename(columns={"name": "category", "size": "rentals"})
    .sort_values("rentals", ascending=False)
)

# Visualize Rentals by Category with a Pie Chart
plt.figure(figsize=(8, 10))
plt.pie(
    category_rentals["rentals"],
    labels=category_rentals["category"],
    autopct="%1.1f%%",
    startangle=140
)
plt.title("Percentage of Rentals by Category")
plt.axis("equal")
plt.show()


# ==============================================================================
# STEP 6: ANALYSIS OF REVENUE AND CUSTOMERS
# ==============================================================================
print("\n--- Analyzing Revenue and Top Customers ---")
# Calculate Revenue by Store
revenue_by_store = (
    df_payment
    .merge(df_rental.drop(columns=['last_update']), on='rental_id')
    .merge(df_inventory.drop(columns=['last_update']), on='inventory_id')
    .groupby('store_id', as_index=False)['amount']
    .sum()
    .rename(columns={'amount': 'total_revenue'})
)

# Visualize Store Revenue
plt.figure(figsize=(6, 4))
plt.bar(revenue_by_store['store_id'], revenue_by_store['total_revenue'], color=['#4CAF50', '#2196F3'])
plt.xticks(revenue_by_store['store_id'], [f"Store {sid}" for sid in revenue_by_store['store_id']])
plt.ylabel("Total Revenue ($)")
plt.title("Total Revenue by Store")
plt.show()


# Find and visualize the Top 5 Customers
top_customers = (
    df_rental
    .groupby("customer_id")
    .size()
    .reset_index(name="rental_count")
    .merge(df_customer, on="customer_id", how="left")
    .sort_values("rental_count", ascending=False)
    .head(5)
)

plt.figure(figsize=(8, 5))
plt.bar(top_customers["first_name"] + " " + top_customers["last_name"], top_customers["rental_count"])
plt.title("Top 5 Customers by Rentals")
plt.xlabel("Customer")
plt.ylabel("Number of Rentals")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.show()


# ==============================================================================
# STEP 7: AVERAGE RENTAL DURATION BY CATEGORY
# ==============================================================================
print("\n--- Analyzing Average Rental Duration ---")

# Calculate the rental duration in days. This will now work without error.
# The warning about performance is normal and can be ignored for this project.
category_merged['rental_duration_days'] = (category_merged['return_date'] - category_merged['rental_date']).dt.total_seconds() / (24 * 3600)

# Calculate the average duration for each category
avg_rental_dur = (
    category_merged.groupby('name')['rental_duration_days']
    .mean()
    .reset_index()
    .sort_values("rental_duration_days", ascending=False)
    .rename(columns={"name": "category"})
)

# Visualize Average Rental Duration
plt.figure(figsize=(10, 6))
plt.bar(avg_rental_dur["category"], avg_rental_dur["rental_duration_days"])
plt.title("Average Rental Duration by Category")
plt.xlabel("Category")
plt.ylabel("Average Duration (Days)")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.show()


print("\n--- Analysis Complete ---")