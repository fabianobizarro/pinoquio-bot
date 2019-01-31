from pymongo import MongoClient
import telegrambot.env as env
import telegrambot.data as data


def map_frase(frase: dict):
    return {
        'frase': frase['frase'],
        'autor': frase['autor']
    }


def map_train(train: dict):
    return {
        'class': train['class'],
        'sentences': train['sentences']
    }


def initialize():

    print('initializing values from database')
    print('connection to database')
    client = MongoClient(env.MONGODB_URI)
    db = client.get_database("bot")
    print('connected')

    # obter frases
    print('getting sentences')
    col = db.get_collection('frases')
    frases = list(col.find())
    frases = list(map(map_frase, frases))
    data.set_frases(frases)
    print('done')

    # obter treinamento
    print('getting training data')
    col = db.get_collection('training')
    train = col.find({})
    train = list(map(map_train, train))
    data.set_training(train)
    print('done')

    # config
    print('getting config data')
    col = db.get_collection('config')
    config = col.find({}).limit(1).skip(0)
    config = list(config)[0]
    data.load_bot_config({
        'HMODE': config['hmode'],
        'ALLOWED_CHATS': config['allowed_chats']
    })
    print('done')
