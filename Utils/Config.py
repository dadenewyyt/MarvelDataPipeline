import os
import dotenv as env

"""load once using singleton pattern"""
class Config:
    _isinstance=None
    _isinitialised=False

    def __new__(cls):
        if(cls._isinstance is None):
            cls._isinstance = super(Config,cls).__new__(cls)
        return cls._isinstance
    
    def __init__(self):
        print("init called")
        if not Config._isinitialised:
            base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) #base dir.
            print(f"path path{base_dir}")
            dotenv_path = os.path.join(base_dir, '.env')
            env.load_dotenv(dotenv_path=dotenv_path) #load the .env from the base path.
        else:
            self._isinitialised = True
    """generic method to get env vars from the loadenv
       default=None if env key doesn't exist"""
    
    def get_env_vars(self,key):
        print(f"getting env var for key: {key}")
        return os.environ.get(key)


if __name__ == "__main__":
    conf = Config()
    print(conf.get_env_vars("PUBLIC_API_KEY"))
