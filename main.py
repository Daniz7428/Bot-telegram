#http://t.me/cldani_bot
from telegram.ext import Updater,CommandHandler
import datetime
from random import randint


def start(update,context):
    context.bot.send_message(chat_id = update.effective_chat.id,text = "¡Hola soy un bot básico, me llamo Bender")


def help(update,context):
    context.bot.send_message(chat_id = update.effective_chat.id,text = "Soy un bot con los Comandos: \n/start: Empezar \n/help: Ayuda \n/hora: Digo la hora y el dia \n/suma: hago una suma \n/dato: Te digo un dato curioso")


def hora(update,context):
    tday = str(datetime.date.today())
    hora = str(datetime.datetime.now())[11:16]
    missatge = "Hoy es: " + tday + "\n Y son las: " + hora
    context.bot.send_message(chat_id = update.effective_chat.id,text = missatge)


def dato(update,context):
    datos=["El primer correo electrónico fue QWERTYUIOP","Chanel realizó el anuncio más caro de la historia, gastó alrededor de $33 millones de dólares en un anuncio publicitario", " En Japón los números 4 y 9 son signos de muerte", "La palabra cementerio viene del griego “dormitorio”"]
    context.bot.send_message(chat_id = update.effective_chat.id,text = datos[randint(0,3)])


def suma(update,context):
    try:
        x = float(context.args[0])
        y = float(context.args[1])
        s = x+y
        context.bot.send_message(chat_id = update.effective_chat.id,text = str(s))
    except Exception as e:
        print(e)
        context.bot.send_message(chat_id=update.effective_chat.id, text="tienes que pasar 2 numeros")


def ak(update,context):
    context.bot.send_photo(chat_id = update.effective_chat.id, photo=open('fotos/ak47.jpg','rb'))
    context.bot.send_message(chat_id=update.effective_chat.id, text="Jan AK")

def vd(update,context):
    context.bot.send_document(chat_id = update.effective_chat.id, document=open('videu.mov','rb'))
    context.bot.send_message(chat_id=update.effective_chat.id, text="Jan AK")


TOKEN = open('token.txt').read().strip()
updater = Updater(token=TOKEN,use_context=True)
dispatcher = updater.dispatcher
dispatcher.add_handler(CommandHandler('start',start))
dispatcher.add_handler(CommandHandler('help',help))
dispatcher.add_handler(CommandHandler('hora',hora))
dispatcher.add_handler(CommandHandler('dato',dato))
dispatcher.add_handler(CommandHandler('suma',suma))
dispatcher.add_handler(CommandHandler('ak',ak))
dispatcher.add_handler(CommandHandler('vd',vd))

updater.start_polling()

