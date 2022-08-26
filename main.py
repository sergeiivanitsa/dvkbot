import os

from dotenv import load_dotenv
from telegram import ReplyKeyboardMarkup
from telegram.ext import CommandHandler, Filters, MessageHandler, Updater

import api

load_dotenv()

updater = Updater(os.getenv('TOKEN'))
chat_id = 279293973


def wake_up(update, context):
    """Отправляет ответ на команду /start"""
    chat = update.effective_chat
    button = ReplyKeyboardMarkup([['/Start']], resize_keyboard=True)
    context.bot.send_message(chat_id=chat.id,
                             text='Привет, введи название или артикул '
                                  'плитки, которую хочешь '
                                  'найти',
                             reply_markup=button)


def request_base(update, context):
    """Запускает функцию, выполняющую запрос и формирует ответ"""
    format_request = "".join(update.message.text).replace(' ', '+')
    dict_responce = api.new_search(format_request)
    for product in dict_responce.keys():
        context.bot.send_message(chat_id=update.effective_chat.id,
                                 text=f'{product} — {dict_responce[product]}'
                                 'шт.')


updater.dispatcher.add_handler(CommandHandler('start', wake_up))
updater.dispatcher.add_handler(MessageHandler(Filters.text &
                               (~Filters.command), request_base))
updater.start_polling()
updater.idle()
