from telegram.ext import Updater, CommandHandler

def welcome(update, context):
    message =  'Olá, '+update.message.from_user.first_name+'. me contrata!'
    print(message)
    context.bot.send_message(chat_id=update.effective_chat.id, text=message)

def main():
    token = '1199113916:AAH0UqtxjAiXA7ad6kWuBAFlGIz6D59rhAM'
    updater = Updater(token=token, use_context=True)

    updater.dispatcher.add_handler(CommandHandler('start', welcome))

    updater.start_polling()
    print(str(updater))
    updater.idle()

if __name__ == "__main__":
    main()
