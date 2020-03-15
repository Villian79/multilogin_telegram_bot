#!/usr/bin/env python
import os
import sys
import requests
import logging
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

# Getting mode, so we could define run function for local and Heroku setup
mode = os.getenv("MODE")
TOKEN = os.getenv("TOKEN")
MAIN_URL = f"https://api.telegram.org/bot{ TOKEN }"

if mode == "dev":
    # Receive updates from the chat with the bot
    # r = requests.get(f"{ MAIN_URL }/getUpdates")
    # if r.status_code != 200:
    #     logger.error("Not connected to bot")
    #     sys.exit(1)
    # logger.info("Connection with bot established")
    # print(r.json())

    #Bot sending response
    payload = {
        "chat_id": 710231208,
        "text": "Howdy buddy"
    }

    r = requests.post(f"{ MAIN_URL }/sendMessage", data = payload)
    print(r.json())

    # def run(updater):
    #     updater.start_polling()
###-----------------------Connecting to Heroku server---------------------####
# elif mode == "prod":
#     def run(updater):
#         PORT = int(os.environ.get("PORT", "8443"))
#         HEROKU_APP_NAME = os.environ.get("HEROKU_APP_NAME")
#         # Code from https://github.com/python-telegram-bot/python-telegram-bot/wiki/Webhooks#heroku
#         updater.start_webhook(listen="0.0.0.0",
#                               port=PORT,
#                               url_path=TOKEN)
#         updater.bot.set_webhook("https://{}.herokuapp.com/{}".format(HEROKU_APP_NAME, TOKEN))

else:
    logger.error("No MODE specified! Check enviroment vars")
    sys.exit(1)
