import requests
from dotenv import load_dotenv
import os
import sqlite3
import pandas as pd

load_dotenv()

class FileOperator:
    def __init__(self):
        self.path = os.getenv('FILE_PATH')

    def read(self):
        with open(self.path, 'r') as file:
            return file.read()
        
    def writeExcel(self, data):
        file_path = os.getenv('SAMPLE_FILE_PATH')
        df = pd.DataFrame(data)
        print(df.value_counts())
        dfTen = df.head(10)
        dfTen.to_excel(file_path, index=False)

    def generateAuditFile(self, api_data):
        db_path = os.getenv('DB_PATH')
        audit_file_path = os.getenv('AUDIT_FILE_PATH')
        conn = sqlite3.connect(db_path)
        df_db = pd.read_sql_query('SELECT * FROM ventas', conn)
        df_api = pd.DataFrame(api_data)
        
        with open(audit_file_path, 'w') as f:
            f.write(f"Number of records in API: {len(df_api)}\n")
            f.write(f"Number of records in DB: {len(df_db)}\n")
            
            # Check if the number of columns is the same
            if len(df_api.columns) != len(df_db.columns):
                f.write("Number of columns is different\n")
            else:
                f.write("Number of columns is the same\n")