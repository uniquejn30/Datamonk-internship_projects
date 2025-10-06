#  DuckDB Sakila Advanced Analytics Challenge

## 📌 Overview
This project explores the **Sakila DVD Rental Database** using **DuckDB**.  
The challenge simulates a real-world analytics task at a cinema company, where management wants insights into **film rentals, customers, and revenue patterns**.

The project is divided into two main parts:

1. **Complex SQL queries on the Sakila database (SQLite + DuckDB)**  
   - Multi-table joins  
   - Subqueries / window functions  
   - Exporting insights to CSV  

2. **Querying the exported CSV directly in DuckDB**  
   - Treating it as a standalone dataset  
   - Performing further aggregations and visualizations  

---

### Q1. How the CSV approach changed your query logic?
When I was working directly on the Sakila database, I could easily join multiple tables, use subqueries, and leverage the relational structure to answer complex business questions. However, once the results were exported to CSV, my query logic had to change. Instead of thinking in terms of multiple normalized tables, I treated the CSV as a single flat dataset. This meant my focus shifted from building complex joins to analyzing pre-aggregated data with simpler filtering, grouping, and aggregation queries. In other words, the CSV approach forced me to simplify the logic and think more like a data analyst working on a denormalized dataset rather than a database engineer working on a relational schema.

### Q2. Benefits and limitations of working with CSVs in DuckDB?
The biggest benefit of querying CSVs in DuckDB is convenience — I didn’t need to re-import the file into a database, and I could run SQL queries directly on top of the CSV. This made it quick and flexible for ad-hoc analysis, especially for sharing results with others who may not have the original database. However, there are also limitations. CSVs don’t preserve data types strictly (everything is stored as text), they can be slower to query on very large files, and you lose the relational structure that enables complex joins. Essentially, CSVs are great for lightweight analysis and portability, but they aren’t a replacement for the full power of a relational database when working with raw transactional data.
