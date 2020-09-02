from telegram.ext import Updater, MessageHandler, Filters

def reply_callback(update, context):
    update.message.reply_text(update.message.text)

updater = Updater(token='110201543:AAHdqTcvCH1vGWJxfSeofSAs0K5PALDsaw', use_context=True)
dispatcher = updater.dispatcher

# add message handler
dispatcher.add_handler(MessageHandler(Filters.text, reply_callback))

# to run the bot
updater.start_polling()

updater.idle()
