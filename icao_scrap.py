#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 25 10:23:33 2020

@author: nicksclater1
"""

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

  td = [i for i in td]
  fh.writelines(str(td))
  fh.writelines('\n')
  print(list(td))
  print('\n')

fh.close()



# for tr in table_row:
#   print(tr)
#   print('\n')

# table_data = table.find_all('td')
# for td in table_data:
#   print(td)
#   print('\n')



