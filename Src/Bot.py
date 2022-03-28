from Secret import teletele
#from Parsing import parsing, showtext
from ParsingHeadless import parsing, showtext
from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import (
    CallbackQueryHandler,
    Updater,
    CommandHandler,
    CallbackContext
)


updater = Updater(token=teletele, use_context=True)
dispatcher = updater.dispatcher

def start(update, context):
    print(f'/start command from {update.effective_chat.id}')
    context.bot.send_message(chat_id=update.effective_chat.id, text=
    '''Greetings! \n   Use /links and /text too see the latest Total War Warhammer 3 posts. \n 
    Due to code restrictions, it is advised to use /links before /text command.'''
                             )

start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

result = []
def parcecommand(update, context):
    #composes links into readable list
    print(f'/links command from {update.effective_chat.id}')
    global result
    text = parsing()
    result = text
    textstring = ''
    i = 1
    for elements in text:
        textstring += str(i)+'.  ' + elements + '\n'
        i+=1
    context.bot.send_message(chat_id=update.effective_chat.id, text=textstring)

links_handler = CommandHandler('links', parcecommand)
dispatcher.add_handler(links_handler)

def gettext(update, context):
    #creates keybord and sends data to query when user clicks on button
    
    chat_id = update.effective_chat.id
    print(f'/text command from {chat_id}')
    keyboard = [
        [
            InlineKeyboardButton("First link", callback_data='1'),
            InlineKeyboardButton("Second link", callback_data='2'),
        ],
        [
            InlineKeyboardButton("Third link", callback_data='3'),
            InlineKeyboardButton("Forth link", callback_data='4')
        ],
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    update.message.reply_text('Choose one:', reply_markup=reply_markup)

text_handler = CommandHandler('text', gettext)
dispatcher.add_handler(text_handler)

def button(update: Update, context: CallbackContext) -> None:
    #updates query info from pressed buttons and sends a respond
    
    query = update.callback_query
    query.answer()
    query.edit_message_text(text=f"You chose: {query.data}")
    query.edit_message_text(text=showtext(result[int(query.data)-1]))


updater.dispatcher.add_handler(CallbackQueryHandler(button)) #links any button with button() function
updater.start_polling()
