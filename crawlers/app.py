from crawler import return_data

telegram_command = input('Digite uma lista de Threads do seu interesse separadas por ";". Exemplo: cats;brazil;worldnews\n')

threads = return_data(telegram_command)

for thread in threads:
    for subject in thread:
        print('\nTitúlo: ' + subject['title'],
            '\nThread: ' + subject['thread'],
            '\nUpvotes: ' + subject['upvotes'],
            '\nLink para os comentários: ' + subject['comment_section_link'],
            '\nLink da Thread: ' + subject['thread_link'])
