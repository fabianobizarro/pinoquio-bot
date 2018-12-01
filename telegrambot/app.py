import json
from telegram import Chat, Update, Message
from pprint import pprint
from flask import Flask, request
from updateinfo import UpdateInfo
from data import get_bot_config, get_allowed_chats
import api as api
# from pybot import PyBot
# from nltk.stem.rslp import RSLPStemmer

app = Flask(__name__)


@app.route('/')
def index():
    return 'Hello World'


@app.route('/API_KEY', methods=['POST'])
def webhook():

    try:

        params = request.data.decode('utf-8')
        json_params = json.loads(params)

        # params from request
        pprint(json_params)

        update = Update.de_json(json_params, None)
        info = UpdateInfo(update)

        api.process_request(info)

        return 'ok'

    except Exception as ex:
        print(ex)
        return 'error'


if __name__ == "__main__":
    app.run()
