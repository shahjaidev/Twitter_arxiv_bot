#import requests

from bs4 import BeautifulSoup



URL = 'http://www.arxiv-sanity.com/top'

page = requests.get(URL)

print(page.content)

soup = BeautifulSoup(page.content)   

results= soup.find_all(class_='apaper')

print(results)