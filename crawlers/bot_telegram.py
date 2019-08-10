import os

from crawler import return_data
from dotenv import load_dotenv
from telegram.ext import CommandHandler, Updater

load_dotenv()

token=os.getenv("TOKEN")

updater = Updater(token=token)
dispatcher = updater.dispatcher

def recebe_comando(bot, update):
    message = update.message
    text = message.text
    chat_id = message.chat.id
    command_length = message.entities[0].length + 1
    threads = text[command_length:]

    output = return_data(threads)

    try:
        for thread in output:
            for subject in thread:
                response = "\nTítulo: {}\nThread: {}\nUpvotes: {}\nLink para a Thread: {}".format(subject['title'], subject['thread'], subject['upvotes'], subject['thread_link'])

                bot.send_message(chat_id=chat_id, text=response)

    except ValueError as e:
        bot.send_message(chat_id=chat_id, text='Erro na requisição. Confira se a lista de Threads está correta.')


command_handler = CommandHandler('nadaparafazer', recebe_comando)
dispatcher.add_handler(command_handler)

updater.start_polling()
