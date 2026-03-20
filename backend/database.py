# Database Initialization and Operations

import sqlite3

class Database:
    def __init__(self, db_name=':memory:'):
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()
        self.create_tables()

    def create_tables(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS fighters (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            strength INTEGER,
            agility INTEGER,
            health INTEGER
        )''')
        self.connection.commit()

    def add_fighter(self, name, strength, agility, health):
        self.cursor.execute('''INSERT INTO fighters (name, strength, agility, health) VALUES (?, ?, ?, ?)''', (name, strength, agility, health))
        self.connection.commit()

    def get_fighter(self, fighter_id):
        self.cursor.execute('''SELECT * FROM fighters WHERE id = ?''', (fighter_id,))
        return self.cursor.fetchone()

    def get_all_fighters(self):
        self.cursor.execute('''SELECT * FROM fighters''')
        return self.cursor.fetchall()

    def update_fighter(self, fighter_id, name=None, strength=None, agility=None, health=None):
        updates = []
        params = []
        if name:
            updates.append('name = ?')
            params.append(name)
        if strength:
            updates.append('strength = ?')
            params.append(strength)
        if agility:
            updates.append('agility = ?')
            params.append(agility)
        if health:
            updates.append('health = ?')
            params.append(health)
        params.append(fighter_id)
        self.cursor.execute(f'''UPDATE fighters SET {', '.join(updates)} WHERE id = ?''', params)
        self.connection.commit()

    def delete_fighter(self, fighter_id):
        self.cursor.execute('''DELETE FROM fighters WHERE id = ?''', (fighter_id,))
        self.connection.commit()

    def close(self):
        self.connection.close()