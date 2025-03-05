import hashlib
import time
import requests
from Utils.Config import Config

config = Config()
public_key = config.get_env_vars("PUBLIC_API_KEY")
private_key = config.get_env_vars("PRIVATE_API_KEY")

ts = str(int(time.time()))

string_to_hash = ts + private_key + public_key
hash_value = hashlib.md5(string_to_hash.encode('utf-8')).hexdigest()

url = f"http://gateway.marvel.com/v1/public/characters?ts={ts}&apikey={public_key}&hash={hash_value}"

response = requests.get(url)

print(response.json())