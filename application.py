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


@bot.message_handler(commands=['start'])
def command_start(message):
    start_markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    start_markup.row('/start', '/help', '/hide')

    bot.send_message(
            message.chat.id, 
            " 🤖 Мультилогин Бот готов к работе! \n\n⚙ Нажмите /help и увидите, что он может"
    )

    bot.send_message(
            message.from_user.id, 
            "⌨️ Кнопочное меню добавлено!\n⌨️ /hide и кнопочное меню будет закрыто", 
            reply_markup=start_markup
    )

@bot.message_handler(commands=['help'])
def help_command(message):
    help_markup = telebot.types.InlineKeyboardMarkup()
    help_markup.row(
        telebot.types.InlineKeyboardButton('Мультилогин - что это?', callback_data='get-about'), 
        telebot.types.InlineKeyboardButton('Документация', callback_data='get-docs')
    )
    help_markup.row(
        telebot.types.InlineKeyboardButton('Прайсинг', callback_data='get-price'), 
        telebot.types.InlineKeyboardButton('Прокси рекомендации', url='https://multilogin.com/ru/proxy/')
    )
    help_markup.row(
        telebot.types.InlineKeyboardButton('ЧаВо', callback_data='get-price'), 
        telebot.types.InlineKeyboardButton('Свяжитесь с нами', callback_data='get-contact')
    )


    bot.send_message(
        message.chat.id,
        '✅ "Мультилогин - что это?" - Узнайте больше о приложении\n\n' +
        '📚 "Документация" - Изучите наш функционал он-лайн\n\n' +
        '💵 "Прайсинг" - Цены и тарифные пакеты\n\n' +
        '🥇 "Прокси рекомендации" - Прокси, которые мы рекомендуем\n\n' +
        '📌 "ЧаВо" - ответы на реальные вопросы от реальных людей\n\n'+
        '📬 "Свяжитесь с нами" - просто кнопка для связи\n',
        reply_markup=help_markup
    )

@bot.message_handler(commands=['hide'])
def command_hide(message):
    hide_markup = telebot.types.ReplyKeyboardRemove()
    bot.send_message(message.chat.id, "⌨💤...", reply_markup=hide_markup)

  
@bot.message_handler(func=lambda m: True)
def echo_all(message):
    bot.send_message(message.chat.id, message.text)

@bot.message_handler(content_types=['sticker'])
def echo_any(message):
    print(message.sticker)  


bot.polling(timeout=60)