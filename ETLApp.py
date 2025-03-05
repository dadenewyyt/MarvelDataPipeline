from Services.ComicService import ComicService
import logging

logging.basicConfig(filename='etl_app.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
#no need for base url but pass as needed to service constructor 

if __name__=="__main__":
    service = ComicService()
    try:
    #extract JSON all characters and comics
        characters = service.get_all_characters()
        if characters:
            logging.info(f"Retrieved {len(characters)} characters.")
            for character in characters:
                service.data_service.insert_character_to_db(character)
                service.insert_comics_to_db(character["id"])
            logging.info("Characters and comics inserted into the database.")
        else:
            logging.warning("No characters retrieved.")
    except Exception as e:
        logging.error(f"An error occurred during ETL: {e}")
    finally:
        service.data_service.close_connection()
