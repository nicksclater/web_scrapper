#! /usr/local/bin/python3

import bs4 as bs
import urllib.request

sauce = urllib.request.urlopen('https://bbc.co.uk').read()
# print(sauce)

print('\n')

# soup = bs.BeautifulSoup(sauce, 'html.parser') # or 'lxml'
# for url in soup.find_all('a'):
#   print(url.get('href'))

soup = bs.BeautifulSoup(sauce,'lxml')


nav = soup.nav
body = soup.body
para = soup.a

print(soup.nav.prettify())



sections = [nav, body]

# for section in sections:
#   print('------------')
#   for url in section.find_all('a'):
#     print(url.get('href'))
#   print('\n')









