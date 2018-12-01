import requests
import env
import data
from updateinfo import UpdateInfo
import pybot.commands as commands
from pybot import PyBot
from nltk.stem.rslp import RSLPStemmer
from pybot.exceptions import NotRecognizedError

CMD_FRASE = '/frase'


def send_message(chat_id: int, text: str, reply_to_message_id: int = None):

    if text is None:
        return

    url = env.TELEGRAM_API_ENDPOINT + '/bot{}/sendMessage'.format(env.API_KEY)
    # print(url)
    request_data = {
        'chat_id': chat_id,
        'text': text,
        'reply_to_message_id': reply_to_message_id
    }
    # print(request_data)
    
    r = requests.post(url, json=request_data)

    print(r.status_code)
    # print(r.content)


def process_request(info: UpdateInfo):

    chat_id = info.chat_id
    # print(chat_id)
    allowed_chat = info.is_allowed_chat(data.get_allowed_chats())
    allowed_to_reply = info.is_allowed_to_reply()

    # print(allowed_chat)
    # print(allowed_to_reply)

    if (allowed_chat and allowed_to_reply):
        # print('process reply')
        resposta = process_reply(info.text, info)
        # print(resposta)
        if resposta:
            reply_id = info.message_id \
                if info.is_chat_type_group \
                else None
            # print('sending message')

            send_message(
                chat_id,
                resposta,
                reply_id)
    else:
        print('no response')


def process_reply(text: str, info: UpdateInfo):

    bot_config = data.get_bot_config()
    h_mode = bool(bot_config['HMODE'])

    if (info.is_photo and h_mode):
        return u'\U0001F44F \U0001F44F \U0001F44F \U0001F44D \U0001F44D \U0001F44D'
    elif info.has_commands:

        # for now, the only available command is /frase
        cmd = info.bot_commands[0]
        if (info.text[cmd.offset:cmd.offset + cmd.length] == CMD_FRASE):
            reply = commands.frase_aleatoria(info.text)
            return reply
        else:
            # nothing
            return None

    else:
        try:
            message = info.text.lower()
            bot = initialize_bot()
            reply = bot.interact(message)
            print(reply)
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

    return bot
