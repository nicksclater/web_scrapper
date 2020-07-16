#! usr/local/bin/python3

import bs4
import urllib.request
import json

# f'https://www.bbc.co.uk/search?q={search_term}'

def search_urls():
  result = {}
  search_term = input('Enter search term: ')

  sauce = urllib.request.urlopen(f'https://www.bbc.co.uk/search?q={search_term}')


def news_scrap(url):
  result = {}
  sauce = urllib.request.urlopen(url).read()
  soup = bs4.BeautifulSoup(sauce, 'html.parser')
  body = soup.body
  title = body.h1.text

  for k in body.find_all('div'):
    if k.get('data-datetime') != None:
      date = k.get('data-datetime')
      break
    else:
      date = 'not found'

  content = ''
  for i in body.find_all('p'):
    if len(i.text) > 60:
      content = content + i.text.replace("\"", '').replace("\n", '')

  results_json = {'url': url, 'title': title, 'date': date, 'content': content}


  return results_json

test = news_scrap('https://www.bbc.co.uk/news/uk-51004218')


