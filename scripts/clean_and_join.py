import pandas as pd
import random
def clean_and_join_data():

    # Read raw data

    customers_file_path = input("Enter customers raw file path : ").strip('"')
    customers = pd.read_csv(customers_file_path)

    orders_file_path = input("Enter orders raw file path : ").strip('"')
    orders = pd.read_csv(orders_file_path)

    products_file_path = input("Enter products raw file path : ").strip('"')
    print()
    products = pd.read_csv(products_file_path)
  
    # Basic Cleaning
    
    print("🔄 Cleaning customers table...")
    customers.columns = customers.columns.str.strip()
    customers['Customer_ID'] = customers['Customer_ID'].astype(int)
    customers.drop_duplicates(subset=['Customer_ID'], inplace=True)

    # Name cleanup and fill
    customers['Customer_Name'] = customers['Customer_Name'].str.title().str.strip()
    customers['Customer_Name'] = customers['Customer_Name'].apply(
    lambda x: random.choice(customers['Customer_Name'].dropna().tolist()) if pd.isna(x) else x
    )

    # City cleanup and fill
    customers['City'] = customers['City'].str.title().str.strip()
    customers['City'] = customers['City'].apply(lambda x: random.choice(customers['City'].dropna().tolist()) if pd.isna(x) else x)  

    # Email cleanup and fill
    customers['Email'] = customers['Email'].str.lower().str.strip()
    customers.drop_duplicates(subset=['Email'], inplace=True)
    customers['Email'].fillna('user_invalid@gmail.com', inplace=True)

    # Reset and reassign Customer_ID
    customers.reset_index(drop=True, inplace=True)
    customers['Customer_ID'] = range(1, len(customers) + 1)
    print("✅ Done cleaning customers table.")
    print("======================================")

    # Clean products
    print("🔄 Cleaning Products table...")

    # Strip whitespace from column names
    products.columns = products.columns.str.strip()

    # Remove duplicate Product_IDs and convert to integer
    products.drop_duplicates(subset=['Product_ID'], inplace=True)
    products['Product_ID'] = products['Product_ID'].astype(int)

    # Clean 'Product_Name' and 'Category' columns
    products['Product_Name'] = products['Product_Name'].str.title().str.strip()
    products['Category'] = products['Category'].str.title().str.strip()

    # Fill missing Product_Name with random valid names
    products.loc[products['Product_Name'].str.strip() == '', 'Product_Name'] = pd.NA
    products['Product_Name'] = products['Product_Name'].apply(lambda x: random.choice(products['Product_Name'].dropna().tolist()) if pd.isna(x) else x)

    # Convert Price column to numeric, fill NAs with mean, and round
    products['Price'] = pd.to_numeric(products['Price'], errors='coerce')
    products['Price'] = products['Price'].fillna(products['Price'].mean())
    products['Price'] = products['Price'].round(2)

    # Reset index and assign new Product_ID starting from 101
    products = products.reset_index(drop=True)
    products['Product_ID'] = range(101, 101 + len(products))

    print("✅ Done cleaning Products table.")
    print("======================================")
  
    # Clean orders
    print("🔄 Cleaning Orders table...")

    # Strip whitespace from column names
    orders.columns = orders.columns.str.strip()  

    # Drop duplicate orders based on unique combination of Customer_ID and Product_ID
    orders.drop_duplicates(subset=['Customer_ID', 'Product_ID'], inplace=True)

    # Reset index after removing duplicates
    orders.reset_index(drop=True, inplace=True)

    # Convert 'Order_Date' column to datetime format, invalid entries become NaT
    orders['Order_Date'] = pd.to_datetime(orders['Order_Date'], errors='coerce')

    # Create a date range starting from '2023-06-15' with 2-day intervals
    # This is used to fill missing Order_Date values
    daterange = pd.date_range('2023-06-15', periods=orders['Order_Date'].isna().sum(), freq='2D')

    # Assign generated dates to rows where Order_Date is missing
    orders.loc[orders['Order_Date'].isna(), 'Order_Date'] = daterange

    # Fill missing Quantity values with the mean of the column
    orders['Quantity'] = orders['Quantity'].fillna(orders['Quantity'].mean())

    # Round Quantity values to 2 decimal places
    orders['Quantity'] = orders['Quantity'].round(2)

    print("✅ Done cleaning Orders table.")
    print("=====================================")

    # Join
    merged = orders.merge(customers, on='Customer_ID', how='left')
    merged = merged.merge(products, on='Product_ID', how='left')
    
    cleaned_csv_file = input('Enter the path of Cleaned file : ').strip('"')
    merged.to_csv(cleaned_csv_file,index=False)



