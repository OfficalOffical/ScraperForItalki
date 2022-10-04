from selenium import webdriver
from bs4 import BeautifulSoup
import time
import re

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
        self.driver.find_element(By.CSS_SELECTOR, ".text-normal").click()


    def buttonClickShowMore(self):


        try:
            for x in self.driver.find_elements(By.CSS_SELECTOR, ".pr-4"):
                self.driver.execute_script("arguments[0].click();", x)

        except:
            print("No more buttons to click")














    def soupSpoon(self):
        tempCounter = 0
        popCounter = 0
        indexToDelTr = []
        TurkishLangChecker = "url(\"https://scdn.italki.com/orion/static/flags/tr.svg\")"


        soup = BeautifulSoup(self.driver.page_source, 'html.parser')



        #getting text
        htmlTxt = soup.find_all('div', class_='regular-body relative break-words whitespace-pre-wrap overflow-hidden')
        #getting parent



        a = htmlTxt[0].find_parent('div', class_='w-full bg-white mb-2 md:mb-0 px-4 md:px-8 py-6')


        print(a.text)




        """#getting flag
        a = a.find('i', class_='ant-avatar-flag')
        #regex to get the url
        temp = a['style'].find('flags/')
        temp2 = a['style'].find('.svg')"""


        print(a['style'][temp+6:temp2])














        print(len(htmlTxt))



        """tempFlagHolder = self.driver.find_elements(By.CSS_SELECTOR, ".ant-avatar-flag")

        for flags in tempFlagHolder:
            tempCounter+= 1
            if flags.value_of_css_property('background-image') == TurkishLangChecker:
                indexToDelTr.append(tempCounter)
            else:
                continue"""











        """for txt in htmlTxt:
            print(txt.text)"""

        print("All Turkish reviews are deleted")




def scrapeWebFromArchive():

    url = "https://www.italki.com/en/community/exercises?language=turkish"

    mainScrape = scraperCreator(url)

    mainScrape.makeConnection()



    for x in range(0, 1):
        mainScrape.scroolydowniytimeywimey()

    mainScrape.buttonClickShowMore()

    mainScrape.soupSpoon()

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

