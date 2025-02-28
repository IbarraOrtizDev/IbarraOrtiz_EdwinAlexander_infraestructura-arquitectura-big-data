import requests
import sqlite3
import pandas as pd

from manageDB import ManageDB

def fetch_data_from_api(api_url, params=None):
    response = requests.get(api_url, params=params)
    response.raise_for_status()  # Raise an exception for HTTP errors
    return response.json()

def generate_sample_file(data, file_path):
    df = pd.DataFrame(data)
    print(df.value_counts())
    df.to_excel(file_path, index=False)

def generate_audit_file(db_path, api_data, audit_file_path):
    conn = sqlite3.connect(db_path)
    df_db = pd.read_sql_query('SELECT * FROM users', conn)
    df_api = pd.DataFrame(api_data)
    
    with open(audit_file_path, 'w') as f:
        f.write(f"Number of records in API: {len(df_api)}\n")
        f.write(f"Number of records in DB: {len(df_db)}\n")
        f.write("Data integrity check:\n")
        f.write(str(df_db.equals(df_api)))

def main():
    api_url = 'https://jsonplaceholder.typicode.com/todos/'
    db_path = 'src/static/db/ingestion.db'
    sample_file_path = 'src/static/xlsx/ingestion.xlsx'
    audit_file_path = 'src/static/auditoria/ingestion.txt'

    # Fetch data from API
    data = fetch_data_from_api(api_url)

    print(data)
    # Generate sample file
    generate_sample_file(data, sample_file_path)

    manageDB = ManageDB()
    manageDB.insert_users_batch(data)

    # Generate audit file
    generate_audit_file(db_path, data, audit_file_path)

if __name__ == '__main__':
    main()