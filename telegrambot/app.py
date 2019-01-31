import os
import json
from telegram import Chat, Update, Message
from telegram.ext import Updater, MessageHandler, ConversationHandler
from telegram.ext.filters import Filters
from telegram.bot import Bot
from telegram.update import Update
from pprint import pprint
from flask import Flask, request
from updateinfo import UpdateInfo
from data import get_bot_config, get_allowed_chats
import api as api
import env as env



def create_app():

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

    return app


def custom_handler(bot: Bot, update: Update):
    info = UpdateInfo(update)
    api.process_request(info)


if __name__ == "__main__":
    print('app running in %s mode' %
          ("production" if env.ENVIRONMENT == "production" else "development"))

    if env.ENVIRONMENT == 'production':
        app = create_app()
        app.run(port=os.getenv('PORT'))
    else:
        updater = Updater(env.API_KEY)
        updater.dispatcher.add_handler(MessageHandler(Filters.text | Filters.photo | Filters.command, custom_handler))
        updater.start_polling()
        print('running...')
        updater.idle()
