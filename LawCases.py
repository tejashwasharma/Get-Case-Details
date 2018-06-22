from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time

def wait(browser, x):
    element = WebDriverWait(browser, 20).until(EC.presence_of_element_located((By.XPATH, x)))
    return element

def find_and_write():
    heading = len(browser.find_elements_by_xpath("//h4[@class='title media-heading']/a"))
    writer = open('case.txt', 'a')
    for head in range(heading):
        wait(browser, "//h4[@class='title media-heading']/a")
        writer.write(browser.find_elements_by_xpath("//h4[@class='title media-heading']/a")[head].text)
        browser.find_elements_by_xpath("//h4[@class='title media-heading']/a")[head].click()
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
    writer.close()

browser = webdriver.Chrome(executable_path='C:\\Users\\tej\\PycharmProjects\\chromedriver.exe')
browser.get('https://www.legalcrystal.com/')

searchbar = browser.find_element_by_id('JudgementName')
searchbar.send_keys('ram mandir\n')

writer = open('case.txt', 'w')
writer.close()

c_url = browser.current_url
for x in range(100):
    find_and_write()
    nxt = browser.find_element_by_xpath("//li[@class='next']/a")
    nxt.click()
    while c_url == browser.current_url:
        time.sleep(20)
    time.sleep(20)
    c_url = browser.current_url
