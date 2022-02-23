from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, PicklePersistence
from Secret import teletele





updater = Updater(token=teletele, use_context=True)
dispatcher = updater.dispatcher

def hello(update, context):
    print(f'/hello command from {update.effective_chat.id}')
    context.bot.send_message(chat_id=update.effective_chat.id, text="Hello1!")

hello_handler = CommandHandler('hello', hello)
dispatcher.add_handler(hello_handler)


updater.start_polling()