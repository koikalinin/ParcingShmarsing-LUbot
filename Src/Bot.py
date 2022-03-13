from Secret import teletele
from Parsing import parsing, showtext
from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import (
    CallbackQueryHandler,
    Updater,
    CommandHandler,
    CallbackContext,
)


updater = Updater(token=teletele, use_context=True)
dispatcher = updater.dispatcher

def hello(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=
    '''Greetings, mortal. \n By the will of the Chaos Gods I will show you the latest Total War Warhammer 3 posts. 
     Use /showlinks and /showtext too see what we have'''
                             )

hello_handler = CommandHandler('hello', hello)
dispatcher.add_handler(hello_handler)

result = []
def parcecommand(update, context):
    global result
    text = parsing()
    result = text
    textstring = ''
    i = 1
    for elements in text:
        textstring += str(i)+'.  ' + elements + '\n'
        i+=1
    context.bot.send_message(chat_id=update.effective_chat.id, text=textstring)


showlinks_handler = CommandHandler('showlinks', parcecommand)
dispatcher.add_handler(showlinks_handler)

def gettext(update, context):
    keyboard = [
        [
            InlineKeyboardButton("First link", callback_data='1'),
            InlineKeyboardButton("Second link", callback_data='2'),
        ],
        [
            InlineKeyboardButton("Third link", callback_data='3'),
            InlineKeyboardButton("Forth link", callback_data='4')
        ],
    ] #когда на тебя нажмут, отправь в query callback_data

    reply_markup = InlineKeyboardMarkup(keyboard) #создает окошко с кнопками

    update.message.reply_text('Choose one:', reply_markup=reply_markup) #добавляет окошко на экран с текстом

showtext_handler = CommandHandler('showtext', gettext)
dispatcher.add_handler(showtext_handler)

def button(update: Update, context: CallbackContext) -> None: #мы получаем инфу о кнопке и
    query = update.callback_query #здесь получаем инфу о том, какая кнопка нажата


    query.answer()
    #print(result[int(query.data)-1])
    #print(showtext(result[int(query.data)-1]))
    query.edit_message_text(text=f"You chose: {query.data}") #передает инфу записанную в квери.дата
    query.edit_message_text(text=showtext(result[int(query.data)-1]))


updater.dispatcher.add_handler(CallbackQueryHandler(button)) #тут мы говорим - свяжи нажатие на кнопку(любую) с функцией Button
updater.start_polling()