import os
import json
from telegram import Update
from flask import Flask, request, abort
from flask_
from .updateinfo import UpdateInfo
import telegrambot.api as api
import telegrambot.env as env


app = Flask(__name__)

webhook_route = '/{}'.format(env.ENDPOINT)


@app.route('/')
def index():
    return 'voce curte?'


@app.route(webhook_route, methods=['POST'])
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
        abort(500)
