from crawler import return_data
import telepot

bot = telepot.Bot("947060274:AAEL-i7oKiqIf0yCHussI85TBO9a_CuNuzE")

def recebe_comando(msg):
    if '/nadaparafazer' in msg['text']:
        lista_de_comandos = msg['text'][14:]

        chat_id = msg['chat']['id']

        output = return_data(lista_de_comandos)

        try:
            for thread in output:
                for subject in thread:
                    response = "\nTítulo: {}\nThread: {}\nUpvotes: {}\nLink para a Thread: {}".format(subject['title'], subject['thread'], subject['upvotes'], subject['subject_thread_link'])
        
        except ValueError:
            bot.sendMessage(chat_id, 'Erro na requisição. Confira se a lista de Threads está correta.')

bot.message_loop(recebe_comando)

while True:
    pass