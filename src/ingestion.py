import requests
import sqlite3
import pandas as pd
from dotenv import load_dotenv
import os

from manageDB import ManageDB

load_dotenv()

def fetch_data_from_api(params=None):
    api_url = os.getenv('API_URL')
    response = requests.get(api_url, params=params)
    response.raise_for_status()  # Raise an exception for HTTP errors
    return response.json()

def generate_sample_file(data):
    file_path = os.getenv('SAMPLE_FILE_PATH')
    df = pd.DataFrame(data)
    print(df.value_counts())
    df.to_excel(file_path, index=False)

def generate_audit_file(api_data):
    db_path = os.getenv('DB_PATH')
    audit_file_path = os.getenv('AUDIT_FILE_PATH')
    conn = sqlite3.connect(db_path)
    df_db = pd.read_sql_query('SELECT * FROM users', conn)
    df_api = pd.DataFrame(api_data)
    
    with open(audit_file_path, 'w') as f:
        f.write(f"Number of records in API: {len(df_api)}\n")
        f.write(f"Number of records in DB: {len(df_db)}\n")
        f.write("Data integrity check:\n")
        f.write(str(df_db.equals(df_api)))

def main():
    # Fetch data from API
    data = fetch_data_from_api()

    print(data)
    # Generate sample file
    generate_sample_file(data)

    manageDB = ManageDB()
    manageDB.insert_users_batch(data)

    # Generate audit file
    generate_audit_file(data)

if __name__ == '__main__':
    main()