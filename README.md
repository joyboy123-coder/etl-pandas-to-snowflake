# 🧹 ETL Project: Pandas to Snowflake❄️

![ETL Pandas to Snowflake Thumbnail](images/thumbnail/thumbnail_image.png)


This project is all about building a full ETL (Extract, Transform, Load) pipeline using Python and Snowflake. It helps take messy raw data, clean it using pandas, and load it into a Snowflake table — all step-by-step with interactive user prompts 🧑‍💻⚙️❄️

---

## 🚦 What’s the Project About?

- You’ll start with **raw messy data** files — 3 of them: customers, orders, and products 📄📦🧾  
- Then, the data goes through a **cleaning process** using pandas. We handle nulls, rename columns, and fix any inconsistencies 🔍🧽  
- Next, the cleaned data from all 3 tables is saved into a single CSV file ✅  
- Finally, that combined cleaned file is read and pushed into **Snowflake**, where it gets stored in a proper table 🧊📥

---

## 🗂️ Folders and Their Purpose

- **`raw_data/`**  
  Contains the 3 messy CSV files: `customers_messy.csv`, `orders_messy.csv`, and `products_messy.csv`. These are the starting point of our ETL pipeline.

- **`cleaned_data/`**  
  Inside this, you’ll find `cleaned_data.csv`, which is an **empty file at first**. After processing, it will contain the final cleaned version of your data 🧼📁

- **`screenshots_etl/`**  
  Contains before and after cleaning screenshots for all 3 tables (customers, orders, products). You can visually see how the data looked before vs after applying cleaning logic 🖼️✨

- **`screenshots_snowflake/`**  
  Shows Snowflake database and schema:
  - Before loading: just DB and schema (no table ❌)
  - After loading: DB, schema, and the newly created table (✅)

- **`terminal_output_project/`**  
  Has two continuous terminal screenshots. They show the full output while running the ETL script — from “ETL started” to “ETL completed successfully” 🔁📸

---

## 🎯 How Does It Work?

The whole flow is user-friendly and prompt-based:

1. First, the script will ask for your **Snowflake credentials** to connect safely (don’t worry, credentials are hidden in terminal 🔒)
2. Then, it asks you to give the path of raw data files — just go into the `raw_data/` folder and copy-paste the paths 🔗
3. The script will then clean the data from all 3 files using pandas 🐼🧹
4. It saves the final cleaned data into the `cleaned_data.csv` file (initially empty) 📄
5. Then, that cleaned file is automatically read again 📖 and uploaded into your Snowflake table 🧊📤
6. Now just head over to Snowflake and check — your table will be there, all clean and ready 🚀

---

## 🎉 ETL Completed Successfully!

That’s a wrap. From start to finish, everything is handled step-by-step — cleaning, saving, and uploading.

🔥 You just need to **clone the project**, run the script, and the pipeline will guide you through the rest.

