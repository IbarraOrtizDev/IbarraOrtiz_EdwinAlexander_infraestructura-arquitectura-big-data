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

    def create_tables_partition(self, df):
        # Create a new SQLite connection
        conn = sqlite3.connect(self.path_db)

        columns_table = """
            ID INTEGER PRIMARY KEY,
            YEAR INTEGER NOT NULL,
            MONTH TEXT NOT NULL,
            CUSTOMER INTEGER NOT NULL,
            PRODUCT TEXT NOT NULL,
            UNITS_SOLD INTEGER NOT NULL,
            PRICE_PER_UNIT REAL NOT NULL,
            REVENUE REAL NOT NULL,
            MONTH_NUM REAL NOT NULL,
            CUSTOMER_NAME TEXT NOT NULL,
            GENDER TEXT,
            COUNTRY TEXT NOT NULL,
            BIRTH_DATE TEXT NOT NULL,  -- Se almacena como TEXT en formato 'YYYY-MM-DD'
            CATEGORY TEXT NOT NULL,
            SUPPLIER TEXT NOT NULL,
            STOCK_LEVEL INTEGER NOT NULL,
            DISCOUNT_AVAILABLE BOOLEAN NOT NULL
        """
        
        # Create a cursor object
        cursor = conn.cursor()
        
        # Create a table for each unique year in the DataFrame
        for year in df['YEAR'].unique():
            table_name = f'ventas_{year}'
            cursor.execute(f'''
                CREATE TABLE IF NOT EXISTS {table_name}(
                    {columns_table}
                )
            ''')
        
        # Commit the changes and close the connection
        conn.commit()
        conn.close()

    def insert_data_partition(self, df):
        # Create a new SQLite connection
        conn = sqlite3.connect(self.path_db)

        # Insert data into the appropriate partitioned table based on the year
        for year in df['YEAR'].unique():
            table_name = f'ventas_{year}'
            df_year = df[df['YEAR'] == year]
            df_year.to_sql(table_name, conn, if_exists='append', index=False)
        
        # Commit the changes and close the connection
        conn.commit()
        conn.close()

    def returnTables(self):
        # Create a new SQLite connection
        conn = sqlite3.connect(self.path_db)
        cursor = conn.cursor()
        
        # Get the list of all tables in the database
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = cursor.fetchall()
        
        # Close the connection
        conn.close()
        
        return [table[0] for table in tables]