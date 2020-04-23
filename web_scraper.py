#! /usr/local/bin/python3

## simple web scraper

import urllib.request
from bs4 import BeautifulSoup

class Scraper:
  def __init__ (self, site):
    self.site = site


  def scrape(self):
    headlines = []
    r = urllib.request.urlopen(self.site)
    html = r.read()
    parser = 'html.parser'
    sp = BeautifulSoup(html, parser)

    for tag in sp.find_all('a'):
      url = tag.get('href')
      print(url)
      if 'story' in url:
        print(url[7:-9].replace('-',' ') + '\n')
        headlines.append(url[7:-9].replace('-', ' '))

    return headlines

news = 'https://news.sky.com'

headlines = Scraper(news).scrape()




