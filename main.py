from telegram import ReplyKeyboardMarkup
from telegram.ext import CommandHandler, Filters, MessageHandler, Updater
import api

updater = Updater(token='5795693615:AAHZGhvouRTcQh_JmC1SWdNBuh5y7QuyXrg')
chat_id = 279293973


def wake_up(update, context):
    chat = update.effective_chat
    name = update.message.chat.first_name
    button = ReplyKeyboardMarkup([['/Start']], resize_keyboard=True)
    context.bot.send_message(
        chat_id=chat.id,
        text=('Привет, введи название или артикул плитки, которую хочешь'
             'найти').format(name),
        reply_markup=button
    )


def request_base(update, context):
    format_request = "".join(update.message.text).replace(' ', '+')
    dict_responce = api.new_search(format_request)
    for product in dict_responce.keys():
        context.bot.send_message(chat_id=update.effective_chat.id, 
                                text=f'{product} — {dict_responce[product]} шт.')


updater.dispatcher.add_handler(CommandHandler('start', wake_up))
updater.dispatcher.add_handler(MessageHandler(Filters.text &
                              (~Filters.command), request_base))
updater.start_polling()
updater.idle()
