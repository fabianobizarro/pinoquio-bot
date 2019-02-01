import logging
import requests
import telegrambot.env as env
import telegrambot.data as data
from telegrambot.updateinfo import UpdateInfo
import telegrambot.pybot.commands as commands
from telegrambot.pybot import PyBot
from nltk.stem.rslp import RSLPStemmer
from telegrambot.pybot.exceptions import NotRecognizedError

logger = logging.getLogger()

CMD_FRASE = '/frase'
CMD_AUTORES = '/autores'


def send_message(chat_id: int, text: str, reply_to_message_id: int = None):

    if text is None:
        return

    url = env.TELEGRAM_API_ENDPOINT + '/bot{}/sendMessage'.format(env.API_KEY)
    request_data = {
        'chat_id': chat_id,
        'text': text,
        'reply_to_message_id': reply_to_message_id
    }

    r = requests.post(url, json=request_data)
    logger.info(
        'request sent to Telegram API. StatusCode: {}'.format(r.status_code))


def process_request(info: UpdateInfo):

    logger.info(data.DATA_PATH)
    chat_id = info.chat_id
    allowed_chat = info.is_allowed_chat(data.get_allowed_chats())
    allowed_to_reply = info.is_allowed_to_reply()

    logger.info('allowed chat and allowed to reply: {}'.format(
        allowed_chat and allowed_to_reply))

    if (allowed_chat and allowed_to_reply):
        resposta = process_reply(info.text, info)
        logger.info('resposta: %s' % resposta)
        if resposta:
            reply_id = info.message_id \
                if info.is_chat_type_group \
                else None

            send_message(
                chat_id,
                resposta,
                reply_id)
    else:
        logger.warn('not allowed to reply')

def process_reply(text: str, info: UpdateInfo):

    bot_config = data.get_bot_config()
    h_mode = bool(bot_config['HMODE'])

    if (info.is_photo and h_mode):
        return commands.resposta_imagem(text)
        # return u'\U0001F44F \U0001F44F \U0001F44F \U0001F44D \U0001F44D \U0001F44D'
    elif info.has_commands:
        cmd = info.bot_commands[0]
        command_name = info.text[cmd.offset:cmd.offset + cmd.length]
        if (command_name == CMD_FRASE):
            reply = commands.frase_aleatoria(info.text, info)
            return reply
        elif command_name == CMD_AUTORES:
            reply = commands.listar_autores(info.text, info)
            return reply
        else:
            return None
    else:
        try:
            message = info.text.lower()
            bot = initialize_bot()
            reply = bot.interact(message, info)
            return reply
        except NotRecognizedError:
            return 'Desculpe, não entendi o que você disse'
        except Exception as exp:
            return str(exp)


def initialize_bot():

    bot = PyBot(RSLPStemmer())

    bot.train_file('telegrambot/data/train.json')

    bot.register_action('saudacao', commands.saudacao)
    bot.register_action('frase', commands.frase_aleatoria)
    bot.register_action('vccurte', commands.curte)

    return bot
