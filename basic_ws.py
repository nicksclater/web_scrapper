#! /usr/local/bin/python3

import bs4 as bs
import urllib.request

sauce = urllib.request.urlopen('https://bbc.co.uk').read()
# print(sauce)

print('\n')

soup = bs.BeautifulSoup(sauce, 'lxml')
# print(soup)

# print(soup.find_all('a'))

for url in soup.find_all('a'):
  print(url.get('href'))







