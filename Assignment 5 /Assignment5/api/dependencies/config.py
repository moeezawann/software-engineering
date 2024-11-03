import os
from dotenv import load_dotenv

# load environment variables from the pass.env file 
load_dotenv('pass.env') 

class conf:
    host = "localhost"
    database = "sandwich_maker_api"
    port = 3306
    user = "root"
    password = os.getenv("DB_PASSWORD", "")