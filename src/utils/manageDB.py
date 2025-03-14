import sqlite3
from dotenv import load_dotenv
import os
import pandas as pd

load_dotenv()

class ManageDB:
    def __init__(self):
        self.path_db = os.getenv('DB_PATH')
        self.db = sqlite3.connect(self.path_db)
        self.cursor = self.db.cursor()
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS users(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                userId INTEGER,
                title TEXT,
                completed BOOLEAN
            )
        ''')
        # Year Month      Customer    Product  Units_Sold  Price_per_Unit      Revenue     Customer_Name
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS ventas(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                Year INTEGER,
                Month TEXT,
                Customer TEXT,
                Product TEXT,
                Units_Sold INTEGER,
                Price_per_Unit INTEGER,
                Revenue INTEGER,
                Customer_Name TEXT
            )
        ''')
        self.db.commit()

    def insert_user(self, userId, id, title, completed):
        self.cursor.execute('''
            INSERT INTO users(userId, id, title, completed)
            VALUES(?, ?, ?, ?)
        ''', (userId, id, title, completed))
        self.db.commit()

    def insert_users_batch(self, users):
        users_tuples = [(user['userId'], user['id'], user['title'], user['completed']) for user in users]
        self.cursor.executemany('''
            INSERT INTO users(userId, id, title, completed)
            VALUES(?, ?, ?, ?)
        ''', users_tuples)
        self.db.commit()

    def insert_ventas_batch(self, ventas):
        
        
        ventas_tuples = [
            (row.Year, row.Month, row.Customer, row.Product, row.Units_Sold, row.Price_per_Unit, row.Revenue, row.Customer_Name)
            for row in ventas.itertuples(index=False)
        ]

        self.cursor.executemany('''
            INSERT INTO ventas(Year, Month, Customer, Product, Units_Sold, Price_per_Unit, Revenue, Customer_Name)
            VALUES(?, ?, ?, ?, ?, ?, ?, ?)
        ''', ventas_tuples)
        self.db.commit()

    def fetch_all_users(self):
        self.cursor.execute('''
            SELECT * FROM users
        ''')
        return self.cursor.fetchall()
    
    def fetch_all_ventas(self):
        conn = sqlite3.connect(self.path_db)
        response = pd.read_sql_query("SELECT * FROM ventas", conn)
        conn.close()
        return response

    def close(self):
        self.db.close()