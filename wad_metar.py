#! /usr/local/bin/python3


import bs4
import  urllib.request
import pandas as pd

source = 'https://www.notaminfo.com/metars?icao=EGXW'


sauce = urllib.request.urlopen(source).read()

soup = bs4.BeautifulSoup(sauce, 'html.parser')
table = soup.table
# print(table)

# table_row = table.find_all('tr')

# for tr in table_row:
#   td = tr.find_all('td')
#   td = [i.text for i in td]
#   print(td)

# print('\n')

dfs = pd.read_html(source, index_col=0)
print(dfs)
# print('\n')
# met = dfs[0][1][1]
# print(met)
