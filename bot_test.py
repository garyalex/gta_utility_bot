#!/usr/bin/python3

import bot_functions
from telegram.ext import Updater, InlineQueryHandler, CommandHandler
import requests
import re

# LOAD CONFIG
config = bot_functions.getconfig("config.yml")


def get_url():
    contents = requests.get('https://random.dog/woof.json').json()
    url = contents['url']
    return url


def bop(bot, update):
    url = get_url()
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)


def chatid(bot, update):
    chat_id = update.message.chat_id
    bot.send_message(chat_id=chat_id, text=f"Chat ID: {chat_id}")


def main():
    updater = Updater(config['telegram_api_token'])
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop', bop))
    dp.add_handler(CommandHandler('chatid', chatid))
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
