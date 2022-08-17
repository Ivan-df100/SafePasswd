import sqlite3

class Database:
    def __init__(self, filename: str):
        self.filename = filename
        self.connection = sqlite3.connect(self.filename)

    def query(self, q, p=[]):
        cursor = self.connection.cursor()

        cursor.execute(q, p)

        fetch = cursor.fetchall()
        
        self.connection.commit()
        cursor.close()

        return fetch