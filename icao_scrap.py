#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import urllib.request
import bs4
import pandas as pd

fh = open('icao.txt', '+w')

source ='https://en.wikipedia.org/wiki/List_of_airports_in_the_United_Kingdom_and_the_British_Crown_Dependencies'

sauce = urllib.request.urlopen(source).read()

soup = bs4.BeautifulSoup(sauce, 'html.parser')

table = soup.table
#print(table)

table_row = table.find_all('tr')

for tr in table_row:
  td = tr.find_all('td')
  td = [i.text.replace("\n","") for i in td]
  for i in td:
    if not i.isprintable() or i =='':
      td.remove(i)
  for i in td:
    if not i.isprintable() or i == '':
      td.remove(i)
  for i in td:
    if not i.isprintable() or i == '':
      td.remove(i)

  print(td)

  fh.writelines(str(td).replace('[','').replace(']',''))
  fh.writelines('\n')
fh.close()


# for tr in table_row:
#   print(tr)
#   print('\n')

# table_data = table.find_all('td')
# for td in table_data:
#   print(td)
#   print('\n')


#### Pandas

# dfs = pd.read_html(source, index_col=0)
# # print(dfs)
# eng = dfs[0] # dataframe

# # ## how to pull data:

# print(eng.loc['Waddington']['ICAO'])
# print('\n')
# print(eng.loc['Waddington']['ICAO'][0]) # pulls out string

# dfs = pd.read_html(source)
# print(dfs)
# eng = dfs[0] # dataframe

# icao ={}
# icao[eng.iloc[11]['Airport name'][0]] = [eng.iloc[11]['ICAO'][0]][0]
# print(icao['Wickenby Aerodrome'])
