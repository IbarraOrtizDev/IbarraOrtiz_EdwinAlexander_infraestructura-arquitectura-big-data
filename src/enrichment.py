from utils.generateAuditEnrichment import generateAuditReport
from utils.loadDataEnrichment import loadCustomerInformation, loadDataCleaning, loadProductInformation
from utils.manageDB import ManageDB
from dotenv import load_dotenv
import os

load_dotenv()


def main():
    # Load data cleaning
    df_data_initial = loadDataCleaning()
    df_sales = df_data_initial.copy()
    # Load product information
    df_product = loadProductInformation()
    # Load customer information
    df_customer = loadCustomerInformation()
    # remove 'Customer ' str from column 'Customer'
    df_sales['Customer'] = df_sales['Customer'].str.replace('Customer ', '')
    # convert 'Customer' column to int
    df_sales['Customer'] = df_sales['Customer'].astype(int)
    # remove 'Customer_Name' of df_sales
    df_sales.drop(columns=['Customer_Name'], inplace=True)

    # merge df_sales with df_customer on 'Customer' column
    df_sales = df_sales.merge(df_customer, on='Customer', how='left')

    # merge df_sales with df_product on 'Product' column though columns upper case
    df_product.columns = df_product.columns.str.upper()
    df_sales.columns = df_sales.columns.str.upper()
    df_sales = df_sales.merge(df_product, on='PRODUCT', how='left')

    print(df_sales.dtypes)

    generateAuditReport(df_sales, df_data_initial)

    # Export the enriched data to CSV
    df_sales.to_csv(os.getenv('ENRICHED_FILE_PATH'), index=False)
    print("Enrichment completed successfully!")

    print("Inserting data into the database...")
    db = ManageDB()
    # Create the database and tables
    db.create_tables_partition(df_sales)
    # Insert the enriched data into the database
    db.insert_data_partition(df_sales)

    print("Data inserted into the database successfully!")
    
    # Tables
    tables = db.returnTables()
    print("Tables in the database:")
    for table in tables:
        print(table)

if __name__ == '__main__':
    main()