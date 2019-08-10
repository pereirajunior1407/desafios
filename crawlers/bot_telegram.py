from crawler import return_data
import telepot

bot = telepot.Bot("816663224:AAGUBOIMUFOKSZIbRINdKf14jOTMLw-IAwU")

def recebe_comando(comando):
    if '/nadaparafazer' in comando['text']:
        lista_de_comandos = comando['text'][14:]

        chat_id = comando['chat']['id']

        output = return_data(lista_de_comandos)

        for thread in output:
            for subject in thread:
                answer = "\nTítulo: {}\nThread: {}\nUpvotes: {}\nLink para Comentários: {}\nLink para a Thread: {}".format(subject['title'], subject['thread'], subject['upvotes'], subject['comment_section_link'], subject['subject_thread_link'])

bot.message_loop(recebe_comando)