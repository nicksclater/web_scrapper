

import urllib.request
import bs4
import json

#-----copy from here to-----
def news_scrap(url):

    sauce = urllib.request.urlopen(url).read()
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

    results_dict = {'url': url, 'title': title, 'date': date, 'content': content}

    results_json = json.dumps(results_dict, indent=4)

    return results_json

##---to here---

test = news_scrap('https://www.bbc.co.uk/news/uk-51004218')

print(test)
