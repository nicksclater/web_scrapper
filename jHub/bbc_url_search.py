
#! usr/local/bin/python3

import urllib.request
import bs4


def search_urls():
  url_list = []
  search_term = input('Enter search term: ')
  sauce = urllib.request.urlopen(f'https://www.bbc.co.uk/search?q={search_term}')
  soup = bs4.BeautifulSoup(sauce, 'html.parser')
  body = soup.body

  for i in body.find_all('a'):
    for j in i.find_all('span'):
      if  (j.get('aria-hidden')) == 'false':
        print(i.text)
        url_list.append(i.get('href'))

  return url_list



if __name__ == '__main__':
  print(search_urls())
