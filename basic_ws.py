#! /usr/local/bin/python3

import bs4 as bs
import urllib.request
import pandas as pd

source = 'https://pythonprogramming.net/parsememcparseface/'

sauce = urllib.request.urlopen(source).read()
# print(sauce)

print('\n')

# soup = bs.BeautifulSoup(sauce, 'html.parser') # or 'lxml'
# for url in soup.find_all('a'):
#   print(url.get('href'))

soup = bs.BeautifulSoup(sauce,'lxml')

nav = soup.nav
body = soup.body
para = soup.find_all('p')
# para = soup.p
# print(para)


sections = [nav, body]

# for section in sections:
#   print('------------')
#   for url in section.find_all('a'): # hyperlink
#     print(url.get('href'))
#   print('\n')

table = soup.table

table_rows = table.find_all('tr') # table row

# print(table_rows)

for tr in table_rows:
  td = tr.find_all('td') # table data
  td = [i.text for i in td]
  print(td)

print('\n')
# using Pandas

dfs  = pd.read_html(source, header=0)

print(dfs) # returns a list of a dataframe
print('\n')

for df in dfs:
  print(df)

print('\n')

print(dfs[0].loc[0,:].values)





