# importing required modules
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time
# method to wait until some element shows its presence on web page
def wait(browser, x):
    element = WebDriverWait(browser, 20).until(EC.presence_of_element_located((By.XPATH, x)))
    return element
# method to go into each url of cases on a single page
def find_and_write():
    #  getting link headings of each cases
    heading = len(browser.find_elements_by_xpath("//h4[@class='title media-heading']/a"))
    # open file in append
    writer = open('case.txt', 'a')
    # visiting url and fetching data and come on to previous page for next url
    for head in range(heading):
        # waiting for link to be click able
        wait(browser, "//h4[@class='title media-heading']/a")
        # writing heading of cases and visit the case
        writer.write(browser.find_elements_by_xpath("//h4[@class='title media-heading']/a")[head].text)
        browser.find_elements_by_xpath("//h4[@class='title media-heading']/a")[head].click()
        # writing all details to text file
        alldetail = browser.find_elements_by_css_selector('td')
        i = 0
        for detail in alldetail:
            i += 1
            writer.write(detail.text)
            if i % 2:
                writer.write('\n')
        data = browser.find_elements_by_xpath("//div[@class='table-bordered']")
        for paragraph in data:
            writer.write(paragraph.text)
        browser.back()
        writer.write('\n\n')
    # closing file after finishing
    writer.close()

# enter keyword to be search
keyword = input("enter keywod to be search : ")
# open website in chrome
browser = webdriver.Chrome(executable_path='C:\\Users\\tej\\PycharmProjects\\chromedriver.exe')
browser.get('https://www.legalcrystal.com/')
# enter in search bar and search
searchbar = browser.find_element_by_id('JudgementName')
searchbar.send_keys(keyword)
searchbar.submit()
# creating file in same directory
writer = open('case.txt', 'w')
writer.close()
# for checking if url changes
c_url = browser.current_url
# for loop for going on next page
for x in range(100):
    # calling method for entering into url and fetching data
    find_and_write()
    # going on next page
    nxt = browser.find_element_by_xpath("//li[@class='next']/a")
    nxt.click()
    # waiting till loading of page
    while c_url == browser.current_url:
        time.sleep(20)
    time.sleep(20)
    # changing current url
    c_url = browser.current_url
