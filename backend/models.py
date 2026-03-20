import sqlite3

class Database:
    def __init__(self, db_name='game.db'):
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()

    def create_table(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS characters (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            health INTEGER NOT NULL,
            power INTEGER NOT NULL
        )''')
        self.connection.commit()

    def add_character(self, name, health, power):
        self.cursor.execute('''INSERT INTO characters (name, health, power) VALUES (?, ?, ?)''', (name, health, power))
        self.connection.commit()

    def get_characters(self):
        self.cursor.execute('SELECT * FROM characters')
        return self.cursor.fetchall()

    def close(self):
        self.connection.close()