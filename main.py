import requests
#from telegram import ReplyKeyboardMarkup
from telegram.ext import CommandHandler, Filters, MessageHandler, Updater
#from utility import SMILE
import api

updater = Updater(token='5795693615:AAHZGhvouRTcQh_JmC1SWdNBuh5y7QuyXrg')
chat_id = 279293973

def wake_up(update, context):
    chat = update.effective_chat
    name = update.message.chat.first_name
#   button = ReplyKeyboardMarkup([['/Amguema'],['/Egvekinot']], resize_keyboard=True)

    context.bot.send_message(
        chat_id=chat.id,
        text=('Привет, введи название или артикул плитки, которую хочешь найти').format(name),
        reply_markup=button
    )

updater.dispatcher.add_handler(CommandHandler('start', wake_up))
updater.dispatcher.add_handler(CommandHandler('Amguema', api.new_search))

updater.start_polling()
updater.idle()