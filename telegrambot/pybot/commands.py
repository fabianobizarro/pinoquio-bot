import random
import json
from telegrambot.data import get_frases
from telegrambot.updateinfo import UpdateInfo


def frase_aleatoria(text: str, context: UpdateInfo = None):
    frase = None
    if context.has_hastags:
        hsh = context.hashtags[0]
        offset = hsh.offset
        length = hsh.length
        value = context.text[hsh.offset:offset + length]
        value = value.replace('#', '').lower()

        frases = [frase for frase in get_frases(
        ) if frase['autor'].lower() == value]

        if len(frases) == 0:
            return 'nao encontrei uma frase do #{}'.format(value)

        frase = random.choice(frases)
    else:
        frases = get_frases()
        frase = random.choice(frases)

    return '"{f}" - {a}'.format(f=frase['frase'], a=frase['autor'])


def listar_autores(text: str, context: UpdateInfo):
    list_autores = [frase['autor'].lower() for frase in get_frases()]
    autores = set(list_autores)

    reply = 'Autores:\n'

    for a in autores:
        reply = reply + '- {}\n'.format(a.lower())

    return reply


def saudacao(text: str, context: UpdateInfo = None):
    options = ['Oi', 'E ai', 'fala comigo', 'opa']
    return random.choice(options)


def resposta_imagem(text: str):
    replies = [
        'Topper',
        u'\U0001F44F \U0001F44F \U0001F44F \U0001F44D \U0001F44D \U0001F44D'
    ]
    return random.choice(replies)


def curte(text: str, context=None):
    res = [
        'xulas',
        'xulispa',
        'file.com'
    ]
    return random.choice(res)
