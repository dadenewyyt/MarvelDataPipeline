import sqlite3
import logging

logging.basicConfig(filename='data_service.log', level=logging.ERROR)

class DataService:
    def __init__(self):
        self.connection = None
        try:
            self.connection = sqlite3.connect("my_marvel.db")
            self.after_init()
        except sqlite3.Error as e:
            logging.error(f"Database connection error: {e}")
            if self.connection:
                self.connection.rollback()
            self.connection = None

    def after_init(self):
        if self.connection:
            try:
                cursor = self.connection.cursor()
                cursor.execute("""
                    CREATE TABLE IF NOT EXISTS characters (
                        id INTEGER PRIMARY KEY,
                        name TEXT,
                        description TEXT
                    )
                """)
                cursor.execute("""
                    CREATE TABLE IF NOT EXISTS comics (
                        id INTEGER PRIMARY KEY,
                        title TEXT,
                        issueNumber INTEGER
                    )
                """)
                cursor.execute("""
                    CREATE TABLE IF NOT EXISTS character_comics (
                        character_id INTEGER,
                        comic_id INTEGER,
                        PRIMARY KEY (character_id, comic_id),
                        FOREIGN KEY (character_id) REFERENCES characters (id),
                        FOREIGN KEY (comic_id) REFERENCES comics (id)
                    )
                """)
                self.connection.commit()
            except sqlite3.Error as e:
                logging.error(f"Table creation error: {e}")
                if self.connection:
                    self.connection.rollback()

    def insert_character_to_db(self, character):
        if self.connection:
            try:
                with self.connection:
                    cursor = self.connection.cursor()
                    cursor.execute(
                        "INSERT OR REPLACE INTO characters (id, name, description) VALUES (?, ?, ?)",
                        (character["id"], character["name"], character["description"]),
                    )
            except sqlite3.Error as e:
                logging.error(f"Character insert error: {e}")
                if self.connection:
                    self.connection.rollback()

    def insert_comics_to_db(self, comics):
        if self.connection:
            try:
                with self.connection:
                    cursor = self.connection.cursor()
                    data = [(comic["id"], comic["title"], comic.get("issueNumber")) for comic in comics]
                    cursor.executemany(
                        "INSERT OR REPLACE INTO comics (id, title, issueNumber) VALUES (?, ?, ?)",
                        data,
                    )
            except sqlite3.Error as e:
                logging.error(f"Comics insert error: {e}")
                if self.connection:
                    self.connection.rollback()

    def insert_character_comics_relationship(self, character_id, comic_id):
        if self.connection:
            try:
                with self.connection:
                    cursor = self.connection.cursor()
                    cursor.execute(
                        "INSERT OR REPLACE INTO character_comics (character_id, comic_id) VALUES (?, ?)",
                        (character_id, comic_id),
                    )
            except sqlite3.Error as e:
                logging.error(f"Relationship insert error: {e}")
                if self.connection:
                    self.connection.rollback()

    def close_connection(self):
        if self.connection:
            self.connection.close()
            self.connection = None