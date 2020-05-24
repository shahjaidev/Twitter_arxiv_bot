

#Scraping with JS support:
from selenium import webdriver

my_url= 'http://www.arxiv-sanity.com/top'
driver = webdriver.PhantomJS()
driver.get(my_url)
li = driver.find_elements_by_class_name('apaper')
for element in li:
    print(element.text)












"""

link_li = driver.find_elements_by_class_name('dllinks')
for element in link_li:
    print(element.get_attribute('spid') )
Scraping with JS support:
import dryscrape
from bs4 import BeautifulSoup
session = dryscrape.Session()
session.visit(my_url)
response = session.body()
soup = BeautifulSoup(response)
soup.find(id="intro-text")
# Result:
<p id="intro-text">Yay! Supports javascript</p>
"""

