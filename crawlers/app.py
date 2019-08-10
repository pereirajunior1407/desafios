from crawler import return_data

telegram_command = input('Digite uma lista de Threads do seu interesse separadas por ";". Exemplo: cats;brazil;worldnews\n')

try:
    threads = return_data(telegram_command)

    for thread in threads:
        for subject in thread:
            print('\nTitúlo: ' + subject['title'])
            print('\nThread: ' + subject['thread'])
            print('\nUpvotes: ' + subject['upvotes'])
            print('\nLink da Thread: ' + subject['thread_link'])

except ValueError:
    print('Erro na requisição. Confira se a lista de Threads está correta.')
