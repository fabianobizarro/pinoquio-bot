import os
import configparser
from dotenv import load_dotenv

_default_port = 8443

load_dotenv()


API_KEY = os.getenv('API_KEY')
PORT = int(os.environ.get('PORT', _default_port))
BOT_ENDPOINT = os.getenv('ENDPOINT')
TELEGRAM_API_ENDPOINT = os.getenv('API_TELEGRAM')
ENVIRONMENT = os.getenv('ENV') or 'development'
ENDPOINT = os.getenv('ENDPOINT')
