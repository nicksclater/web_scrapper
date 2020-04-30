#! usr/local/bin/python3

import bs4
import urllib.request
import json

url = 'https://www.bbc.co.uk/news/technology-52458759'
url2 = 'https://www.bbc.co.uk/search?q=RAF'

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

  for i in body.find_all('ul'):
    for j in i.find_all('li'):
      for k in j.find_all('div'):
        if k.get('data-datetime') != None:
          date = k.get('data-datetime')

  main_text = ''
  for i in body.find_all('p'):
    if len(i.text) > 60:
      main_text = main_text + i.text.replace("\"", '')

  result[title] = {'url': input_url, 'date': date, 'main_body': main_text}
  #result = json.dumps(result, indent=4,)

  return result


if __name__ == '__main__':
  result = news_scrap(url)
  print(result)