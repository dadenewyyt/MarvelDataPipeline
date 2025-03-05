import sqlite3
import logging
import datetime
logging.basicConfig(filename='data_service.log', level=logging.ERROR)

class DataService:
    def __init__(self):
        self.connection = None
        try:
            self.connection = sqlite3.connect("my_marvel.db")
            #self.after_init()
        except sqlite3.Error as e:
            logging.error(f"Database connection error: {e}")
            if self.connection:
                self.connection.rollback()
            self.connection = None

    def tentative_old_after_init(self):
        if self.connection:
            try:
                cursor = self.connection.cursor()
                cursor.execute("""
                    CREATE TABLE IF NOT EXISTS characters (
                        id INTEGER PRIMARY KEY,
                        name TEXT,
                        description TEXT,
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

    def insert_character_to_db(self, characters):
        if self.connection:
            try:
                with self.connection:
                    cursor = self.connection.cursor()
                    """get the current timestamp in the right format for the API as UTC"""
                    now = datetime.datetime.now(datetime.timezone.utc).isoformat()
                    data = [(character["id"], character["name"], character.get("description", ""), now) for character in characters]
                    cursor.executemany(
                    "INSERT OR REPLACE INTO characters (id, name, description, modified_at) VALUES (?, ?, ?, ?)",
                    data,
                )
            except sqlite3.Error as e:
                logging.error(f"Character insert error: {e}")
                if self.connection:
                    self.connection.rollback()
    """ batch insert """
    def insert_comics_to_db(self, comics):
        if self.connection:
            try:
                with self.connection:
                    cursor = self.connection.cursor()
                    """get the current timestamp in the right format for the API as UTC"""
                    now = datetime.datetime.now(datetime.timezone.utc).isoformat()
                    data = [(comic["id"], comic["title"], comic.get("issueNumber"),now) for comic in comics]
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
   
    def get_last_etl_run(self):
        
        if self.connection:
            try:
                with self.connection:
                    cursor = self.connection.cursor()
                    result = cursor.execute("SELECT last_run FROM etl_metadata ORDER BY last_run DESC LIMIT 1;")
                    result = self.cursor.fetchone()
                    logging.debug(f"last run data{result}")
                if result and result[0]:
                    return datetime.datetime.fromisoformat(result[0])
                else:
                    return None
            except Exception as e:
                logging.error(f"selecting last modified data error{e}")
                if self.connection:
                   self.connection.rollback()
    
    def insert_or_update_etl(self):
        """ get the last date, delete the last date, and replace the new date as new last date for next run"""
        now = datetime.datetime.now(datetime.timezone.utc)
        if self.connection:
            try:
                with self.connection:
                    cursor = self.connection.cursor()
                    self.cursor.execute("DELETE FROM etl_metadata")
                    self.cursor.execute("INSERT INTO etl_metadata (last_run) VALUES (?)", (now.isoformat(),))
                    self.conn.commit()
            except Exception as e:
                logging.error(f"Error updating etl meta data {e}")
                if self.connection:
                   self.connection.rollback()
        return
    
    def close_connection(self):
        if self.connection:
            self.connection.close()
            self.connection = None