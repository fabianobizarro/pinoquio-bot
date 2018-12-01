import random
import json
from data import get_frases


def frase_aleatoria(text: str):
    print(text)
    frases = get_frases()
    frase = random.choice(frases)
    # print(frase)
    return '"{f}" - {a}'.format(f=frase['frase'], a=frase['autor'])



def saudacao(text: str):
    options = ['Oi', 'E ai', 'fala comigo']
    return random.choice(options)
