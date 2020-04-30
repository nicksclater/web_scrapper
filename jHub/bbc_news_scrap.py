#! usr/local/bin/python3

import bs4
import urllib.request
import json

def search_urls():
  result = {}
  search_term = input('Enter search term: ')

  sauce = urllib.request.urlopen(f'https://www.bbc.co.uk/search?q={search_term}')


def news_scrap(input_url: str):
  result = {}
  sauce = urllib.request.urlopen(input_url).read()
  soup = bs4.BeautifulSoup(sauce, 'html.parser')
  body = soup.body
  title = body.h1.text

  for k in body.find_all('div'):
    if k.get('data-datetime') != None:
      date = k.get('data-datetime')
      break
    else:
      date = 'fail'

  main_text = ''
  for i in body.find_all('p'):
    if len(i.text) > 60:
      main_text = main_text + i.text.replace("\"", '').replace("\n", '')

  result = {'title': title, 'date': date, 'main_body': main_text}


  return result


# x = news_scrap('https://www.bbc.co.uk/news/uk-52378491')
# print(x)