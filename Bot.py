from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# دالة الرد على الرسائل
def respond_hello(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('hello')

def main():
    # استبدل "YOUR_TOKEN_HERE" برمز الـ API الخاص بالبوت
    updater = Updater("6505569921:AAEy-fhkO7AP2g5_1DlCqE-tWEMnmkRa0_c", use_context=True)

    dispatcher = updater.dispatcher

    # ربط الرسائل الواردة بدالة الرد
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, respond_hello))

    # بدء البوت
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
