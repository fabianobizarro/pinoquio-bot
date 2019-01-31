import os
import json
import logging
from logging.config import dictConfig
from telegram import Update
from flask import Flask, request, abort
from .updateinfo import UpdateInfo
import telegrambot.api as api
import telegrambot.env as env

dictConfig({
    'version': 1,
    'formatters':{
        'default': {
            'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s'
        }
    },
})

logger = logging.getLogger()

app = Flask(__name__)

_webhook_route = '/{}'.format(env.ENDPOINT)


@app.route('/')
def index():
    return 'voce curte?'


@app.route(_webhook_route, methods=['POST'])
def webhook():

    try:

        logger.info(request.data)
        params = request.data.decode('utf-8')
        logger.info(params)
        json_params = json.loads(params)
        logger.info(json_params)

        update = Update.de_json(json_params, None)
        info = UpdateInfo(update)
        logger.info(info)


        api.process_request(info)

        return 'ok'

    except Exception as ex:
        logger.error(ex)
        abort(500)
