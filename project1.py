#! usr/local/bin/python3
import bs4
import urllib.request

url = 'https://www.bbc.co.uk/news/technology-52458759'
def news_scrap(input_url: str):
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
    main_text = main_text + i.text + ' '

  print(title)
  print(date)
  print(main_text)


news_scrap(url)