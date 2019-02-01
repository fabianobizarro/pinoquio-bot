import json
import os
from telegram import Update
from configparser import ConfigParser, SectionProxy
import logging

logger = logging.getLogger()

DATA_PATH = os.path.dirname(os.path.realpath(__file__))


def get_allowed_chats():
    config = get_bot_config()

    chats = config.get('allowed_chats')
    chats = chats.replace('[', '').replace(']', '')
    chats = chats.split(',')
    return list(map(int, chats))

def get_bot_config() -> SectionProxy:
    config = ConfigParser()
    config.read(DATA_PATH + '/.config.ini')
    logger.info(config)
    return config['default']


def load_bot_config(configs: dict):
    config = ConfigParser()
    config['default'] = configs

    with open(DATA_PATH + '/.config.ini', 'w') as file:
        config.write(file)


def get_frases():
    with open(DATA_PATH + '/frases.json', 'r') as file:
        json_data = json.load(file)
        file.close()
        return json_data


def set_frases(frases: list):
    with open(DATA_PATH + '/frases.json', 'w', encoding='utf-8') as file:
        json.dump(frases, file)


def get_training():
    with open(DATA_PATH + '/train.json', 'r') as file:
        json_data = json.load(file)
        file.close()
        return json_data


def set_training(training_content: list):
    with open(DATA_PATH + '/train.json', 'w', encoding='utf-8') as file:
        json.dump(training_content, file)
