from selenium import webdriver
from bs4 import BeautifulSoup
import time

from selenium.webdriver.common.by import By


def mainWebScraper():
    scrapeWebFromArchive()


class scraperCreator():

    def __init__(self, url, name, path):
        self.url = url
        self.driver = webdriver.Chrome()




def scrapeWebFromArchive():
    tempCounter = 0
    webHolder = []
    driver = webdriver.Chrome()
    # Open the URL
    driver.get("https://www.italki.com/en/community/exercises?language=turkish")
    SCROLL_PAUSE_TIME = 1
    # Get scroll height
    last_height = driver.execute_script("return document.body.scrollHeight")
    while True:
        # Scroll down to bottom
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        driver.find_element(By.CSS_SELECTOR, ".text-normal").click()
        # Wait to load page
        time.sleep(SCROLL_PAUSE_TIME)
        # Calculate new scroll height and compare with last scroll height
        new_height = driver.execute_script("return document.body.scrollHeight")



        if new_height == last_height:
            break
        last_height = new_height
    soup = BeautifulSoup(driver.page_source, "html.parser")
    """# Find all the <a> tags
    links = soup.find_all('a', class_='au av aw ax ay az ba bb bc bd be bf bg bh bi')
    for link in links:
        if (link.get('aria-label') != None):
            tempCounter += 1
            if (tempCounter % 3 == 0):
                print(link.get('href'))
                webHolder.append("https://medium.com" + link.get('href'))"""











    # Close the browser
    driver.quit()
    #--print(len(links))

