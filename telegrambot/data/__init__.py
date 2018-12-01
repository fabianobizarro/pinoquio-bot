import json
import os
from telegram import Update
from configparser import ConfigParser

DATA_PATH = os.path.dirname(os.path.realpath(__file__))


def get_allowed_chats():
    with open(DATA_PATH + '/.chats', 'r') as file:
        json_data = json.load(file)
        print(json_data)
        file.close()
        return json_data


def set_allowed_chats(chat_list: list):
    chats = []
    with open(DATA_PATH + '.chats', 'w') as file:
        json.dump(chats, file)


def get_bot_config():
    config = ConfigParser()
    config.read(DATA_PATH + '/config.ini')
    return config['default']


def load_bot_config():
    # load from database
    configs = {
        'HMODE': True
    }

    config = ConfigParser()
    config['default'] = configs

    with open('.config.ini', 'w') as file:
        config.write(file)


def get_frases():
    with open(DATA_PATH + '/frases.json', 'r') as file:
        json_data = json.load(file)
        file.close()
        return json_data
