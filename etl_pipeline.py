from scripts.clean_and_join import clean_and_join_data
from scripts.load_to_snowflake import load_to_snowflake

def main():
    print("\n=================================")
    print("🚀 Starting ETL pipeline...")

    # Step 1: Clean and join data
    print("🧼 Cleaning and joining data...\n")
    clean_and_join_data()
    print("==================================")
    print("✅ Data cleaned and joined.")

    # Step 2: Load to Snowflake
    print("☁️ Loading data into Snowflake...")
    load_to_snowflake()
    print("\n=====================================================")
    print("🎉 ETL pipeline completed successfully!")

if __name__ == "__main__":
    main()
