#!/usr/bin/env python
import os
import sys
import logging
import telebot
from dotenv import load_dotenv
load_dotenv()

#Enabling logging
log_filename = 'logs_multilogin.log'
log_filemode = 'w'
log_level = logging.DEBUG
log_format = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
log_datefmt='%m-%d-%Y %H:%M:%S'

logging.basicConfig(filename=log_filename, filemode=log_filemode, level=log_level, format=log_format, datefmt=log_datefmt)
logger = logging.getLogger('telegram_logs')

#Starting the Bot
TOKEN = os.getenv("TOKEN")
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.send_message(message.chat.id, "Howdy!!! How are you doing?", disable_notification=True)

@bot.message_handler(func=lambda m: True)
def echo_all(message):
    print(message)
	#bot.send_message(message.chat.id, message.text)

@bot.message_handler(content_types=['sticker'])
def echo_any(message):
    print(message.sticker)


bot.polling(timeout=60)