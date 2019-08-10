import bs4
import requests
import time

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
            
            if thread_link.startswith('/r/'):
                thread_link = 'https://old.reddit.com' + thread_link

            output_dict = {}
            output_dict['title'] = thread_title.text
            output_dict['thread'] = thread
            output_dict['upvotes'] = str(upvotes)
            output_dict['thread_link'] = thread_link
            thread_list.append(output_dict)
            
    return thread_list

def return_data(thread_command):
    if not thread_command:
        raise ValueError
    
    thread_command = thread_command.split(';')

    thread_list = []

    for command in thread_command:

        url = requests.get('https://old.reddit.com/r/{}/'.format(command))
        while url.status_code == 429:
            time.sleep(5)
            url = requests.get('https://old.reddit.com/r/{}/'.format(command))

        thread_list.append(data_scrapping(command, url.text))
    
    return thread_list



