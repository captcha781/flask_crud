import json
from dotenv import load_dotenv

load_dotenv()
config = json.load(open('config/config.json'))
