import bs4
import requests

def data_scrapping(thread, url):
    bsoup = bs4.BeautifulSoup(url, 'lxml')

    thread_list = []

    for div in bsoup.find_all('div', class_='thing'):
        upvotes = div.find('div', class_='score unvoted').get('title')

        if upvotes:
            upvotes = int(upvotes)
        else:
            upvotes = 0
        

        if upvotes > 5000:
            find_thread = div.find('div', class_='entry unvoted')
            thread_title = find_thread.find('p', class_='title')
            thread_link = thread_title.find('a').get('href')
            comment_section = div.find('li', class_='first')
            comment_section_link = comment_section.find('a').get('href')

            if thread_link.startswith('/r/'):
                thread_link = 'https://old.reddit.com' + thread_link

            if comment_section_link.startswith('/r/'):
                comment_section_link = 'https://old.reddit.com' + comment_section_link

            output_dict = {}
            output_dict['title'] = thread_title.text
            output_dict['thread'] = thread
            output_dict['upvotes'] = str(upvotes)
            output_dict['thread_link'] = thread_link
            output_dict['comment_section_link'] = comment_section_link

            thread_list.append(output_dict)
            
    print(thread_list)

def return_data(thread_command):
    
    thread_command = thread_command.split(';')

    thread_list = []

    for command in thread_command:

        url = requests.get('https://old.reddit.com/r/%s/' % command)

        thread_list.append(data_scrapping(command, url.text))

    return thread_list



