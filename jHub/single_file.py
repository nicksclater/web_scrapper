

import urllib.request
import bs4
import json


def search_urls():

    url_list = []
    search_term = input('Enter search term: ')
    returns = int(input('enter number of returns: '))

    for n in range(1, 5):

        if len(url_list) >= returns:
            break

        page = urllib.request.urlopen(f'https://www.bbc.co.uk/search?q={search_term}&page={n}')
        soup = bs4.BeautifulSoup(page, 'html.parser')
        body = soup.body

        while len(url_list) < returns:

            for i in body.find_all('a'):
                for j in i.find_all('span'):
                    if (j.get('aria-hidden')) == 'false' and len(url_list) < returns:
                        url_list.append(i.get('href'))

    return url_list


def news_scrap(input_url: str):

    sauce = urllib.request.urlopen(input_url).read()
    soup = bs4.BeautifulSoup(sauce, 'html.parser')
    body = soup.body
    title = body.h1.text
    date = ''

    for k in body.find_all('div'):
        if k.get('data-datetime') is not None:
            date = k.get('data-datetime')
            break
        else:
            date = 'not found'

    content = ''
    for i in body.find_all('p'):
        if len(i.text) > 60:
            content = content + i.text.replace("\"", '').replace("\n", '')

    result = {'title': title, 'date': date, 'content': content}

    return result


def grab_news():
    file_name = input('enter filename: ')
    results = {}
    urls = search_urls()

    for url in urls:
        results[url] = news_scrap(url)

    json_obj = json.dumps(results, indent=4)

    with open(f"{file_name}.json", "w") as outfile:
        outfile.write(json_obj)

    return results


print(grab_news())
