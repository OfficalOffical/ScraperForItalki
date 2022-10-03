from selenium import webdriver
from bs4 import BeautifulSoup
import time

from selenium.webdriver.common.by import By


def mainWebScraper():
    scrapeWebFromArchive()


class scraperCreator():


    def __init__(self, url):
        self.url = url
        self.driver = webdriver.Chrome()


    def makeConnection(self):
        self.driver.get(self.url)

    def closeConnection(self):
        self.driver.close()

    def scroolydowniytimeywimey(self):

        SCROLL_PAUSE_TIME = 1

        last_height = self.driver.execute_script("return document.body.scrollHeight")

        while True:
            # Scroll down to bottom
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            # Wait to load page
            time.sleep(SCROLL_PAUSE_TIME)
            # Calculate new scroll height and compare with last scroll height
            new_height = self.driver.execute_script("return document.body.scrollHeight")

            if new_height == last_height:
                break
            last_height = new_height

    def buttonClickShowMore(self):
        self.driver.find_element(By.CSS_SELECTOR, ".text-normal").click()





def scrapeWebFromArchive():

    url = "https://www.italki.com/en/community/exercises?language=turkish"

    mainScrape = scraperCreator(url)

    mainScrape.makeConnection()




    mainScrape.scroolydowniytimeywimey()

    mainScrape.buttonClickShowMore()



    mainScrape.closeConnection()


    """# Find all the <a> tags
    links = soup.find_all('a', class_='au av aw ax ay az ba bb bc bd be bf bg bh bi')
    for link in links:
        if (link.get('aria-label') != None):
            tempCounter += 1
            if (tempCounter % 3 == 0):
                print(link.get('href'))
                webHolder.append("https://medium.com" + link.get('href'))"""











    # Close the browser

    #--print(len(links))

