from selenium import webdriver
from bs4 import BeautifulSoup
import time
import csv
import pandas as pd

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

            try :
                htmlLangHolder = []
                htmlTextHolder = []

                soup = BeautifulSoup(self.driver.page_source, 'html.parser')

                htmlParent = soup.find_all('div', class_='w-full bg-white mb-2 md:mb-0 px-4 md:px-8 py-6')

                for htmlIterator in htmlParent:
                    try:

                        htmlLang = htmlIterator.find('i', class_='ant-avatar-flag')
                        htmlLangStart = htmlLang['style'].find('flags/')
                        htmlLangEnd = htmlLang['style'].find('.svg')
                        htmlLang = htmlLang['style'][htmlLangStart + 6: htmlLangEnd]
                        htmlLangHolder.append(htmlLang)
                        if (htmlLang != 'tr'):
                            for textFinder in htmlIterator.find_all('div',
                                                                    class_='regular-body relative break-words whitespace-pre-wrap overflow-hidden'):
                                htmlTextHolder.append(textFinder.text)
                                break
                    except Exception as e:
                        print(e)
                        pass



                header = ["Text", "Language"]

                with open('dataHolder.csv', 'w', encoding='UTF8') as f:
                    writer = csv.writer(f)
                    writer.writerow(header)
                    writer.writerows(zip(htmlTextHolder, htmlLangHolder))
                f.close()

                data = pd.read_csv('dataHolder.csv')
                print(data.head(10))

            except Exception as e:
                print(e)
                time.sleep(1000000)







def scrapeWebFromArchive():
    url = "https://www.italki.com/en/community/exercises?language=turkish"

    mainScrape = scraperCreator(url)

    mainScrape.makeConnection()
    while True:

        mainScrape.scroolydowniytimeywimey()

        mainScrape.buttonClickShowMore()

        mainScrape.soupSpoon()



    mainScrape.closeConnection()

