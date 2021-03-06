import os
from telegram.bot import Bot
from telegram.update import Update
from telegram.ext import Updater, MessageHandler
from telegram.ext.filters import Filters
from telegrambot.updateinfo import UpdateInfo
from telegrambot.app import app
import telegrambot.api as api
import telegrambot.env as env

from initialize import initialize

def base_handler(bot: Bot, update: Update):
    info = UpdateInfo(update)
    api.process_request(info)


print('app running in %s mode' %
      ("production" if env.ENVIRONMENT == "production" else "development"))



if __name__ == "__main__":
    initialize()
    if env.ENVIRONMENT == 'production':
        app.run(port=os.getenv('PORT'))
    else:
        updater = Updater(env.API_KEY)
        updater.dispatcher.add_handler(MessageHandler(
            Filters.text | Filters.photo | Filters.command, base_handler))
        updater.start_polling()
        print('running...')
        updater.idle()
