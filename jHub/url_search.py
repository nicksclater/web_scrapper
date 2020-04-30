
#! usr/local/bin/python3

import urllib.request
import bs4


def search_urls():

  search_term = input('Enter search term: ')
  sauce = urllib.request.urlopen(f'https://www.bbc.co.uk/search?q={search_term}')
  soup = bs4.BeautifulSoup(sauce, 'html.parser')
  print(soup)

  return soup

search_urls()
