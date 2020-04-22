#! /usr/local/bin/python3

## simple web scraper

import urllib.request
from bs4 import BeautifulSoup

class Scraper:
	def __init__ (self, site):
		self.site = site

	headlines = []
	def scrape(self):
		r = urllib.request.urlopen(self.site)
		html = r.read()
		parser = 'html.parser'
		sp = BeautifulSoup(html, parser)

		for tag in sp.find_all('a'):
			url = tag.get('href')
		
			if url is None:
				continue
			if 'story' in url:
				print('\n' + url)
				self.headlines.append(url[7:-9])

		return self.headlines

news = 'https://news.sky.com'

headlines = Scraper(news).scrape()




