# 🧩 PostgreSQL Project – Section 1: Use What You Learned

This section focuses on using advanced PostgreSQL data types and extensions — **JSONB, citext, hstore, range types, materialized views, and backups**.  
You’ll also practice enabling extensions and using real-world use cases for flexible data, analytics, and data recovery.

---

## 📘 Table of Contents
1. [JSONB Column](#1-jsonb-column)
2. [citext for Emails](#2-citext-for-emails)
3. [hstore Key-Value Storage](#3-hstore-key-value-storage)
4. [Range Types (Booking Windows)](#4-range-types-booking-windows)
5. [Materialized Views for Analytics](#5-materialized-views-for-analytics)
6. [Backups with pg_dump](#6-backups-with-pg_dump)
7. [Proof Submission Checklist](#7-proof-submission-checklist)

---

## 🧱 1. JSONB Column

### 🧭 Task
- Add a JSONB column to store flexible product specifications.
- Insert data with different JSON structures.
- Query specific keys from the JSONB data.

### 🧩 Queries
```sql
-- Create table
CREATE TABLE products (
    id SERIAL PRIMARY KEY,
    name TEXT,
    price NUMERIC,
    specs JSONB
);

-- Insert flexible JSON data
INSERT INTO products (name, price, specs)
VALUES 
('Laptop', 80000, '{"ram": "16GB", "ssd": "512GB", "os": "Windows"}'),
('Phone', 40000, '{"battery": "5000mAh", "color": "black"}'),
('Tablet', 30000, '{"screen_size": "10inch", "storage": "128GB"}');

-- View data
SELECT * FROM products;

-- Query JSON key
SELECT name, specs->>'ram' AS ram_size FROM products;

-- Query where specific key exists
SELECT name, specs FROM products WHERE specs ? 'color';
```

### ✅ Proof to Include
- Screenshot of `\d products` (showing `specs JSONB`)
- `SELECT` output with JSON data and key extraction

---

## 📧 2. citext for Emails

### 🧭 Task
- Enable the **citext** extension.
- Create an email column that ignores case sensitivity.
- Insert similar emails with different cases and test duplicates.

### 🧩 Queries
```sql
-- Enable extension
CREATE EXTENSION IF NOT EXISTS citext;

-- Create users table
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    email CITEXT UNIQUE
);

-- Insert case-insensitive emails
INSERT INTO users (email)
VALUES ('Test@Example.com'), ('test@example.com');

-- Query data
SELECT * FROM users;
```

🧠 PostgreSQL will treat both emails as the same because of `citext`.

### ✅ Proof to Include
- Screenshot of `\d users` (showing `citext` type)
- Query output showing case-insensitive behavior

---

## 🧩 3. hstore Key-Value Storage

### 🧭 Task
- Enable **hstore** extension.
- Store dynamic key-value pairs (user preferences).
- Query individual values from the hstore column.

### 🧩 Queries
```sql
-- Enable extension
CREATE EXTENSION IF NOT EXISTS hstore;

-- Create table
CREATE TABLE user_prefs (
    id SERIAL PRIMARY KEY,
    username TEXT,
    preferences hstore
);

-- Insert key-value pairs
INSERT INTO user_prefs (username, preferences)
VALUES
('alice', '"theme"=>"dark", "language"=>"en"'),
('bob', '"theme"=>"light", "language"=>"fr"');

-- View full preferences
SELECT * FROM user_prefs;

-- Query a specific key
SELECT username, preferences->'theme' AS theme FROM user_prefs;
```

### ✅ Proof to Include
- Screenshot of `\dx` showing `hstore`
- `\d user_prefs` (with `hstore` column)
- Query output selecting key value (`preferences->'theme'`)

---

## 🏨 4. Range Types (Booking Windows)

### 🧭 Task
- Create a booking table with a **daterange** column.
- Insert multiple bookings.
- Query all bookings that overlap with a given range.

### 🧩 Queries
```sql
-- Create table
CREATE TABLE bookings (
    id SERIAL PRIMARY KEY,
    customer TEXT,
    stay DATERANGE
);

-- Insert data
INSERT INTO bookings (customer, stay)
VALUES
('Alice', '[2025-02-01,2025-02-10)'),
('Bob', '[2025-02-05,2025-02-08)'),
('Charlie', '[2025-02-15,2025-02-18)');

-- View all bookings
SELECT * FROM bookings;

-- Find overlapping bookings
SELECT * FROM bookings WHERE stay && '[2025-02-06,2025-02-09)';
```

### ✅ Proof to Include
- Screenshot of `\d bookings` (showing `daterange`)
- Output showing only overlapping bookings

---

## 📊 5. Materialized Views for Analytics

### 🧭 Task
- Create a materialized view for slow queries.
- Compare performance before and after using the view.
- Refresh materialized view to update results.

### 🧩 Queries
```sql
-- Create source tables
CREATE TABLE orders (
    id SERIAL PRIMARY KEY,
    product_id INT,
    quantity INT
);

-- Insert sample orders
INSERT INTO orders (product_id, quantity)
VALUES (1, 2), (2, 3), (1, 1), (3, 5);

-- Create materialized view for analytics
CREATE MATERIALIZED VIEW sales_summary AS
SELECT p.name, SUM(o.quantity * p.price) AS total_sales
FROM products p
JOIN orders o ON p.id = o.product_id
GROUP BY p.name;

-- Query the materialized view
SELECT * FROM sales_summary;

-- Refresh the view after new data
REFRESH MATERIALIZED VIEW sales_summary;

-- Recheck data after refresh
SELECT * FROM sales_summary;
```

### ✅ Proof to Include
- Screenshot of `\dv+` showing the materialized view
- Query output before & after `REFRESH MATERIALIZED VIEW`

---

## 💾 6. Backups with pg_dump

### 🧭 Task
- Create a backup of your database.
- Restore into a new database.
- Confirm that all tables and data are restored correctly.

### 🧩 Commands (Run in Terminal)
```bash
# Backup (custom format)
pg_dump -Fc practice_db > practice_db.backup

# Create a new empty database
createdb restore_db

# Restore backup into new database
pg_restore -d restore_db practice_db.backup
```

### ✅ Proof to Include
- The `.backup` file
- Screenshot of restored database schema (`\dt`)
- Query output confirming data restored correctly

---

## 🧾 7. Proof Submission Checklist

| Feature | Proof Required |
|----------|----------------|
| **JSONB** | `\d products` + JSON query output |
| **citext** | `\d users` + duplicate email test |
| **hstore** | `\dx` + query output for specific key |
| **Range Types** | `\d bookings` + overlap query output |
| **Materialized View** | `\dv+` + before/after refresh |
| **Backup** | `.backup` file + restored schema screenshot |

---

## 🧠 Notes & Learnings

- `CREATE EXTENSION` enables PostgreSQL’s modular power (citext, hstore, etc.).  
- `JSONB` and `hstore` give schema flexibility like NoSQL inside PostgreSQL.  
- `Range types` simplify interval logic (great for bookings or scheduling).  
- `Materialized views` precompute and store query results for faster analytics.  
- `pg_dump` backups are critical for production reliability and migration.

---

**Author:** [Unique Jain](https://github.com/uniquejn30)  
**Database:** PostgreSQL  
**Section:** 1 – Use What You Learned  
**Goal:** Learn advanced PostgreSQL data types, extensions, and maintenance tools.
