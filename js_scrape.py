

#Scraping with JS support:
from selenium import webdriver
from random import randint

my_url= 'http://www.arxiv-sanity.com/top'
"""
li = driver.find_elements_by_class_name('apaper')
paper_all=[]

for element in li:
    paper_all.append(element.text)
    #print(element.text)
"""


class scrape:
    def __init__(self, url= 'http://www.arxiv-sanity.com/top' ):
        self.driver = webdriver.PhantomJS()
        self.driver.get(my_url)

    def get_links(self):
        link_li= self.driver.find_elements_by_link_text('pdf')
        paper_links=[]
        for element in link_li:
            #print(element.get_attribute('href'))
            paper_links.append( element.get_attribute('href') )
        
        #print(len(paper_links) )

        return paper_links


    def get_titles(self):
        paper_titles=[]
        link_li= self.driver.find_elements_by_class_name('ts')
        for element in link_li:
            #print(element.text)
            paper_titles.append(element.text)
        
        return paper_titles



#Paper descriptions/ condensed abstracts
    def get_descs(self):
        paper_descs=[]
        link_li= self.driver.find_elements_by_class_name('tt')
        for element in link_li:
            paper_descs.append(element.text)
        
        return paper_descs



s=scrape()

titles= s.get_titles()
descs= s.get_descs()
links=s.get_links()

idx= randint(0,5)

tweet= titles[idx]+" \n PDF: " + links[idx]
print(tweet)

sys.stdout.flush()