import os
import configparser

# path = os.path.dirname(os.path.abspath(__file__)) + '/../.ini'

config = configparser.ConfigParser()
config.read('.ini')

settings = config['default']

API_KEY = settings['API_KEY']
PORT = int(os.environ.get('PORT', '8443'))
BOT_ENDPOINT = settings['ENDPOINT']
TELEGRAM_API_ENDPOINT = settings['API_TELEGRAM']
