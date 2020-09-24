# -*- coding: utf-8 -*-

import settings
import telebot

bot = telebot.TeleBot(settings.TOKEN)


@bot.message_handler(commands=['start', 'help'])
def start_help_handler(message):
    bot.reply_to(message, "hello!")


@bot.message_handler(commands=['ask'])
def ask_handler(message):
    bot.reply_to(message, message.text)


bot.polling()
