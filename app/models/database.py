# Работа с базой данных (SQLite)
import sqlite3

class Database:
    def __init__(self, db_name="notes.db"):
        self.connection = sqlite3.connect(db_name)
        self.create_table()

    def create_table(self):
        with self.connection:
            self.connection.execute("""
                CREATE TABLE IF NOT EXISTS notes (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    title TEXT NOT NULL,
                    date TEXT NOT NULL,
                    description TEXT
                )
            """)

    def add_note(self, title, date, description):
        with self.connection:
            self.connection.execute("""
                INSERT INTO notes (title, date, description)
                VALUES (?, ?, ?)
            """, (title, date, description))

    def get_notes(self):
        with self.connection:
            return self.connection.execute("SELECT * FROM notes").fetchall()

    def update_note(self, note_id, title, date, description):
        with self.connection:
            self.connection.execute("""
                UPDATE notes
                SET title = ?, date = ?, description = ?
                WHERE id = ?
            """, (title, date, description, note_id))

    def delete_note(self, note_id):
        with self.connection:
            self.connection.execute("""
                DELETE FROM notes WHERE id = ?
            """, (note_id,))
