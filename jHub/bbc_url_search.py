
#! usr/local/bin/python3

import urllib.request
import bs4


def search_urls():

  url_list = []
  search_term = input('Enter search term: ')
  returns = int(input('enter number of returns: '))

  for n in range(1,5):

    if len(url_list) >= returns:
      break

    page = urllib.request.urlopen(f'https://www.bbc.co.uk/search?q={search_term}&page={n}')
    soup = bs4.BeautifulSoup(page, 'html.parser')
    body = soup.body

    while len(url_list) < returns:

      for i in body.find_all('a'):
        for j in i.find_all('span'):
          if  (j.get('aria-hidden')) == 'false' and len(url_list) < returns:
            url_list.append(i.get('href'))
  print(url_list)
  return url_list


if __name__ == '__main__':
  print(search_urls())

