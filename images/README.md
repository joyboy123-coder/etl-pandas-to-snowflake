# 🧹 Data Cleaning & ETL Workflow Project

Welcome! This project showcases how messy real-world datasets — including **customers**, **orders**, and **products** — were cleaned and transformed using a structured ETL process. 🧼📊🛠️

---

## 🖼️ Screenshots of ETL Workflow

### 📁 `screenshots_etl/`
This folder documents the **entire ETL journey** with visuals:

- **`before_cleaning.png`** 🟥 — Snapshot of how the raw data looked across all three tables.
- **`before_cleaning_schema.png`** 🧩 — Shows initial schema issues like nulls, wrong data types, etc.
- **`after_cleaning.png`** ✅ — Visual of the cleaned data after processing.
- **`after_cleaning_schema.png`** 📐 — Displays the improved schema after cleaning and transformation.

These screenshots cover the **customers**, **orders**, and **products** datasets collectively.

---

## ❄️ Snowflake Integration

### 📁 `screenshots_snowflake/`

This folder documents the state of Snowflake before and after loading the cleaned data:

- **`before_loading_table_to_snowflake.png`** ❌  
  Shows the database and schema setup, but table retrieval fails (no data loaded yet).

- **`after_loading_table_to_snowflake.png`** ✅  
  Displays successful table creation and data availability inside Snowflake — all set up and working!

These screenshots visually confirm the successful connection and data loading process into Snowflake.

## 💻 Terminal Output (Final Run)

---
### 📁 `terminal_output_project/`

This folder contains the final terminal output of the ETL pipeline execution:

- **`terminal_output_ss1.png`**
- **`terminal_output_ss2.png`**

🟢 These two images are part of the same continuous log:

- Starts from: `"ETL is starting..."`
- Ends with: `"ETL successfully completed ✅"`

They visually capture the complete execution of your `etl_pipeline` script — from beginning to successful completion — making it easy for others to understand the runtime flow at a glance.
