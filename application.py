#!/usr/bin/env python
import os
import time
import telebot
from dotenv import load_dotenv
load_dotenv()

#Enabling logging
# log_filename = 'logs_multilogin.log'
# log_filemode = 'w'
# log_level = logging.DEBUG
# log_format = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
# log_datefmt='%m-%d-%Y %H:%M:%S'

# logging.basicConfig(filename=log_filename, filemode=log_filemode, level=log_level, format=log_format, datefmt=log_datefmt)
# logger = logging.getLogger('telegram_logs')

#Starting the Bot
TOKEN = os.getenv("TOKEN")
bot = telebot.TeleBot(TOKEN)

#Create main inline markup to be used on different pages
def main_help_markup():
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
    return help_markup


@bot.message_handler(commands=['start'])
def command_start(message):
    start_markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    start_markup.row('/start', '/help', '/hide')
 
    bot.send_photo(
        message.chat.id,
        photo='AgACAgIAAxkBAAIBKF6Az021ySPi6gABf8HhoBu2MQYvDQAC060xG-wpCUjgxFp4ZavFkggmwQ4ABAEAAwIAA20AA5-KBAABGAQ'
    )

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
    help_markup = main_help_markup()

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

@bot.callback_query_handler(func=lambda call: True)
def test_callback(query):
    data = query.data
    if data == 'get-about':
        get_about_callback(query)
    elif data == 'get-docs':
        get_docs_callback(query)
    else:
        print('Undefined callback')

def get_about_callback(query):
    bot.send_message(
        query.message.chat.id,
        "<strong>Приложение Мультилогин, что это?</strong>\n\n"
        + "Деск-топ приложение Мультилогин является лицензионным продуктом компании Multilogin Software Ltd.\n\n"
        + "<i>Месторасположение:</i>\n<i>10151 Estonia,</i>\n<i>Ahtri 6a, Tallinn</i>\n\n"
        + "Приложение Мультилогин позволяет создавать большое количество браузерных профилей с уникальными отпечатками, что позволяет объединить работу на многих машинах воедино на Вашем ПК.\n\n"
        + "При создании браузерного профиля Multilogin Вы получаете полностью отделенную среды для работы в интернете. Куки-файлы, локальные кэши и хранилища помещаются в полностью изолированные хранилища и не могут просачиваться между разными браузерными профилями.\n\n"
        + "Multilogin подходит к вопросу браузерных отпечатков своим уникальным способом. Вместо того, чтобы препятствовать чтению сайтами браузерного отпечатка, Multilogjn позволяет его считать, но заменяет оригинальный отпечаток Вашего компьютера на другой.\n"
        + "<a href='https://multilogin.com/ru/'>inline URL</a>",
        reply_markup=main_help_markup(),
        parse_mode="HTML"
    )

def get_docs_callback(query):
    docs_markup = telebot.types.InlineKeyboardMarkup()
    docs_markup.add(telebot.types.InlineKeyboardButton('Как начать?', url='https://docs.multilogin.com/l/ru/category/Xgyn06jSkV-'))
    docs_markup.add(telebot.types.InlineKeyboardButton('Управление браузерным профилем', url='https://docs.multilogin.com/l/ru/category/xjaceu68r0-'))
    docs_markup.add(telebot.types.InlineKeyboardButton('Браузерные отпечатки', url='https://docs.multilogin.com/l/ru/category/o40iDKTlyQ-'))
    docs_markup.add(telebot.types.InlineKeyboardButton('Настройки прокси', url='https://docs.multilogin.com/l/ru/category/B75BuVtULu-'))
    docs_markup.add(telebot.types.InlineKeyboardButton('Настройки браузерного профиля', url='https://docs.multilogin.com/l/ru/category/TmaPFZpgqk-'))
    docs_markup.add(telebot.types.InlineKeyboardButton('Интеграции', url='https://docs.multilogin.com/l/ru/category/y8mchdhz7v-'))
    docs_markup.add(telebot.types.InlineKeyboardButton('API', url='https://docs.multilogin.com/l/ru/category/0ik9sebp2x-api'))
    docs_markup.add(telebot.types.InlineKeyboardButton('Устранение неполадок', url='https://docs.multilogin.com/l/ru/category/zs3p07okfz-'))

    bot.send_message(
        query.message.chat.id,
        "<strong>Он-лайн документация приложения Мультилогин</strong>\n\n"
        + "Наша документация довольно обширна и доступна всем пользователям на сайте нашей компании.\n"
        + "Выберите интересующий Вас раздел ниже:\n\n",
        parse_mode="HTML",
        reply_markup=docs_markup
    )

@bot.message_handler(commands=['hide'])
def command_hide(message):
    hide_markup = telebot.types.ReplyKeyboardRemove()
    bot.send_message(message.chat.id, "⌨💤...", reply_markup=hide_markup)

  
@bot.message_handler(func=lambda m: True)
def echo_all(message):
    print(message)
    # bot.send_message(message.chat.id, message.text)

@bot.message_handler(content_types=['sticker'])
def echo_any(message):
    print(message.sticker)  


while True:
    try:
	    bot.infinity_polling(True)
    except Exception:
	    time.sleep(1)