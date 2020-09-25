import settings
import telebot
import time
import threading
import logging
from compragamer import compragamer


logging.basicConfig(level=logging.INFO)
bot = telebot.TeleBot(settings.TOKEN)
chatids = []


@bot.message_handler(commands=['start', 'help'])
def start_help_handler(message):
    logging.debug(msg="start received from {id}".format(id="message.chat.id"))
    bot.reply_to(message, "hello!")


@bot.message_handler(commands=['ask'])
def ask_handler(message):
    logging.debug(msg="ask received from {id}".format(id="message.chat.id"))
    chatids.append((message.chat.id, message.text.partition(' ')[2]))
    bot.reply_to(message, "ok")


def botpolling():
    logging.info("Start Polling")
    bot.polling()


threading.Thread(target=botpolling).start()
while True:
    for id, criteria in chatids:
        cg = compragamer()
        articulos = cg.search(criteria)
        for articulo in articulos:
            bot.send_message(id, articulo)
    time.sleep(int(settings.INTERVAL))
