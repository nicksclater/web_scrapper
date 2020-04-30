
import urllib.request
import bs4
import json


from bbc_url_search import search_urls
from bbc_news_scrap import news_scrap

def grab_news():

  results = {}
  urls = search_urls()

  for url in urls:
    results[url] = news_scrap(url)

  json_obj = json.dumps(results, indent=4)

  with open("RAF.json", "w") as outfile:
    outfile.write(json_obj)


  return results



print(grab_news())




