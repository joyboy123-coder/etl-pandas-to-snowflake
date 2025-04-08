import pandas as pd 
import random
import snowflake.connector
from snowflake.connector.pandas_tools import write_pandas

# Get Snowflake connection details from user
user = input('🔐 Enter Snowflake user: ')
password = input('🔑 Enter your Snowflake Password: ')
account = input('🏢 Enter your Snowflake Account: ')
warehouse = input('📦 Enter your Warehouse: ')
database = input('🗃️ Enter your Database Name: ')
schema = input('📂 Enter your Schema Name: ')
table = input('📋 Enter your Table Name: ')
print()

def load_to_snowflake():
    try:
        print("🔌 Connecting to Snowflake...")
        conn = snowflake.connector.connect(
            user=user,
            password=password,
            account=account,
            warehouse=warehouse,
            database=database,
            schema=schema
        )
        print("✅ Connected successfully!\n")
        print("======================================================")

        # Load input file
        input_file = input('📄 Enter your merged data input file path: \n').strip('"')
        df = pd.read_csv(input_file)
        print("📥 File loaded into DataFrame.")

        # Data cleaning and transformation
        df.drop_duplicates(inplace=True)
        df['Order_Date'] = pd.to_datetime(df['Order_Date'], errors='coerce')
        df['Order_Date'] = df['Order_Date'].dt.date
        
        df['Email'] = df['Email'].fillna('invalid_user@gmail.com')

        df['Customer_Name'] = df['Customer_Name'].apply(
            lambda x: random.choice(df['Customer_Name'].dropna().tolist()) if pd.isna(x) else x
        )
        df['City'] = df['City'].apply(
            lambda x: random.choice(df['City'].dropna().tolist()) if pd.isna(x) else x
        )
        df['Product_Name'] = df['Product_Name'].apply(
            lambda x: random.choice(df['Product_Name'].dropna().tolist()) if pd.isna(x) else x
        )

        df['Amount'] = df['Quantity'] * df['Price']
        df['Amount'] = df['Amount'].round(2)
        df.columns = df.columns.str.upper()

        print("🧹 Data cleaned and transformed!")

        # Upload to Snowflake
        print("📤 Uploading data to Snowflake...")
        success, nchunks, nrows, _ = write_pandas(
            conn=conn,
            df=df,
            table_name=table,
            schema=schema,
            database=database,
            auto_create_table=True
        )

        if success:
            print(f"🎉 Successfully loaded {nrows} rows into Snowflake! 🚀")
        else:
            print("❌ Upload failed. Please check your table or data format.")

    except Exception as e:
        print("⚠️ An error occurred:", e)

    finally:
        conn.close()
        print("🔒 Connection closed.")
