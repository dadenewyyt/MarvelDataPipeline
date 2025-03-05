import time as t
from hashlib import md5
import requests as req
from Utils.Config import Config
import time as time
import string
from ratelimit import limits
from DataLayer.DataService import DataService  # Import your DataService class
import logging

logging.basicConfig(filename='comic_service.log', level=logging.ERROR)

RATE = 1  # Adjust as needed
CALLS = 5  # Adjust as needed

"""service layer for comic API"""
class ComicService:
    def __init__(self, base_url="http://gateway.marvel.com/v1/public/"):
        self.base_url = base_url
        self.config = Config()
        self.data_service = DataService() #add data service.

    @limits(calls=CALLS, period=RATE)
    def get_list_with_offsets(self, name="characters", limit=100, offset=0, name_start_letter=None,modifiedSince=None):
        public_key = self.config.get_env_vars("PUBLIC_API_KEY")
        private_key = self.config.get_env_vars("PRIVATE_API_KEY")
        base_url = self.base_url
        ts = str(time.time())
        hash_string = f"{ts}{private_key}{public_key}"
        hashed = md5(hash_string.encode("utf-8")).hexdigest()

        url = f"{base_url}{name}?ts={ts}&apikey={public_key}&hash={hashed}"

        params = {
            "orderBy": "name",
            "limit": limit,
            "offset": offset,
            "modifiedSince": modifiedSince,
        }

        if name_start_letter:
            params["nameStartsWith"] = name_start_letter
        
        if modifiedSince:
            params["modifiedSince"] = modifiedSince


        try:
            response = req.get(url, params=params, verify=True)
            response.raise_for_status()
            data = response.json()
            return data["data"]["results"]
        except Exception as e:
            logging.error(f"Exception receiving {name} list: {e}")
            return None

    @limits(calls=CALLS, period=RATE)
    def get_all_characters(self):
        all_characters = []
        alphabet = str(string.ascii_uppercase)

        last_run = self.data_service.get_last_etl_run()
        modified_since = last_run.isoformat() if last_run else None
        #characters = self.get_all_characters(modified_since = modified_since)

        for starting_letter in alphabet:
            offset = 0
            while True:
                comic_characters = self.get_list_with_offsets(offset=offset, name_start_letter=starting_letter,modifiedSince=modified_since)
                if not comic_characters:
                    break
                """all character and comic array gets appended after each loop if not empty"""
                all_characters.extend(comic_characters)
                offset += 100
                time.sleep(1)

        offset = 0
        while True:
            comic_characters = self.get_list_with_offsets(offset=offset, name_start_letter=None)
            if not comic_characters:
                break
            all_characters.extend(comic_characters)
            offset += 100
            time.sleep(1)
        return all_characters

    @limits(calls=CALLS, period=RATE)
    def get_comics(self, character_id, limit=100, offset=0,modifiedSince=None):
        name = f"characters/{character_id}/comics"
        public_key = self.config.get_env_vars("PUBLIC_API_KEY")
        private_key = self.config.get_env_vars("PRIVATE_API_KEY")
        ts = str(time.time())
        hash_string = f"{ts}{private_key}{public_key}"
        hashed = md5(hash_string.encode("utf-8")).hexdigest()
        url = f"{self.base_url}{name}?ts={ts}&apikey={public_key}&hash={hashed}"

        params = {
            "limit": limit,
            "offset": offset,
            "modifiedSince":modifiedSince
        }

        try:
            response = req.get(url, verify=True, params=params)
            response.raise_for_status()
            data = response.json()
            return data["data"]["results"]
        except Exception as e:
            logging.error(f"Exception getting comics for character {character_id}: {e}")
            return None

    def insert_comics_to_db(self, character_id,modifiedSince=None):
        offset = 0
        while True:
            comics = self.get_comics(character_id, offset=offset)
            if not comics:
                break
            self.data_service.insert_comics_to_db(comics)
            for comic in comics:
                self.data_service.insert_character_comics_relationship(character_id, comic["id"])
            offset += 100

    def get_all_characters_and_comics(self,modifiedSince=None):
        last_run = self.data_service.get_last_etl_run()
        modified_since = last_run.isoformat() if last_run else None
        characters = self.get_all_characters(modified_since)
        if characters:
            for character in characters:
                self.data_service.insert_character_to_db(character,modifiedSince)
                self.insert_comics_to_db(character["id"],modified_since)
            self.data_service.close_connection()
