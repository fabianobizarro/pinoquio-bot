import os
import configparser

# path = os.path.dirname(os.path.abspath(__file__)) + '/../.ini'

_default_port = 8443

config = configparser.ConfigParser()
config.read('.ini')

settings = config['default']

# getting the values from .ini file
API_KEY = settings['API_KEY']
PORT = int(os.environ.get('PORT', _default_port))
BOT_ENDPOINT = settings['ENDPOINT']
TELEGRAM_API_ENDPOINT = settings['API_TELEGRAM']
ENVIRONMENT = settings['ENV'] or 'development'
