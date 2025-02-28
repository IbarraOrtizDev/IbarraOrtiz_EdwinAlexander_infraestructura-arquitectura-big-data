import requests
import sqlite3
import pandas as pd

def fetch_data_from_api(api_url, params=None):
    response = requests.get(api_url, params=params)
    response.raise_for_status()  # Raise an exception for HTTP errors
    return response.json()

def create_database(db_path):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS data (
            id INTEGER PRIMARY KEY,
            field1 TEXT,
            field2 TEXT,
            field3 TEXT
        )
    ''')
    conn.commit()
    return conn

def insert_data_to_db(conn, data):
    cursor = conn.cursor()
    for item in data:
        cursor.execute('''
            INSERT INTO data (field1, field2, field3) VALUES (?, ?, ?)
        ''', (item['field1'], item['field2'], item['field3']))
    conn.commit()

def generate_sample_file(data, file_path):
    df = pd.DataFrame(data)
    df.to_excel(file_path, index=False)

def generate_audit_file(db_path, api_data, audit_file_path):
    conn = sqlite3.connect(db_path)
    df_db = pd.read_sql_query('SELECT * FROM data', conn)
    df_api = pd.DataFrame(api_data)
    
    with open(audit_file_path, 'w') as f:
        f.write(f"Number of records in API: {len(df_api)}\n")
        f.write(f"Number of records in DB: {len(df_db)}\n")
        f.write("Data integrity check:\n")
        f.write(df_db.equals(df_api))

def main():
    api_url = 'https://api.example.com/data'
    db_path = 'src/static/db/ingestion.db'
    sample_file_path = 'src/static/xlsx/ingestion.xlsx'
    audit_file_path = 'src/static/auditoria/ingestion.txt'

    # Fetch data from API
    data = fetch_data_from_api(api_url)

    # Create database and insert data
    conn = create_database(db_path)
    insert_data_to_db(conn, data)

    # Generate sample file
    generate_sample_file(data, sample_file_path)

    # Generate audit file
    generate_audit_file(db_path, data, audit_file_path)

if __name__ == '__main__':
    main()