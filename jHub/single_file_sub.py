

import urllib.request
import bs4
import json
import nltk
nltk.download('averaged_perceptron_tagger')
nltk.download('maxent_ne_chunker')
nltk.download('words')

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




def extract_entities(string):

    tagger = nltk.pos_tag(string.split())
    chucker = nltk.ne_chunk(tagger)
    tmp = {'people':[], 'places':[], 'organisation':[]}

    for i in chucker:

        if isinstance(i, nltk.tree.Tree):
            print(i)
            if i.label() == 'PERSON':
                tmp['people'] = i[0][0]
            if i.label() == ('GPE' or 'LOCATION'):
                tmp['places'] = i[0][0]
            if i.label() == 'ORGANIZATION':
                tmp['organisation'] = i[0][0]

    entities_json = json.dumps(tmp, indent=4)

    return entities_json

##---to here---

test = news_scrap('https://www.bbc.co.uk/news/uk-51004218')

print(test)

test1 = 'My name is Nick and I live in England and work for the RAF'
test2 = "My name is Charlotte and I live in Heighington"
test3 = 'I work for the Council'

test_cases = [test1, test2, test3]

for test in test_cases:
    res = extract_entities(test)
    print(res)
