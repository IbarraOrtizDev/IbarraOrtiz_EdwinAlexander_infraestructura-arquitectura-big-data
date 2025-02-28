import sqlite3
from dotenv import load_dotenv
import os

load_dotenv()

class ManageDB:
    def __init__(self):
        path_db = os.getenv('DB_PATH')
        self.db = sqlite3.connect(path_db)
        self.cursor = self.db.cursor()
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS users(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                userId INTEGER,
                title TEXT,
                completed BOOLEAN
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

    def fetch_all_users(self):
        self.cursor.execute('''
            SELECT * FROM users
        ''')
        return self.cursor.fetchall()

    def close(self):
        self.db.close()