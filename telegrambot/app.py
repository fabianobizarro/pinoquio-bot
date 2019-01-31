import json
from telegram import Update
from flask import Flask, request
from .updateinfo import UpdateInfo
import telegrambot.api as api


# def create_app(*args, **kwargs):

    # print(args)
    # print(kwargs)

app = Flask(__name__)

@app.route('/')
def index():
    return 'voce curte?'

@app.route('/API_KEY', methods=['POST'])
def webhook():

    try:

        params = request.data.decode('utf-8')
        json_params = json.loads(params)

        update = Update.de_json(json_params, None)
        info = UpdateInfo(update)

        api.process_request(info)

        return 'ok'

    except Exception as ex:
        print(ex)
        return 'error'

    # return app
