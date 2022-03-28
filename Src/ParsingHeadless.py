from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def parsing():
    # extract url source code using Headless Senenium
    # parse code with BS
    # create list with links leading to required blogs
    url = 'https://www.totalwar.com/blog/'
    options = Options()
    options.headless = True
    s = Service('C:\chromedriver_win32\chromedriver.exe')
    browser = webdriver.Chrome(service=s, options=options)
    browser.set_window_size(1920, 1080)
    browser.get(url)
    #time.sleep(1)
    #browser.save_screenshot('D:\screen_shot.png')
    #browser.set_window_size(1920, 1080)
    browser.find_element(by=By.XPATH, value='//*[@id="ccc-notify-accept"]').click()
    #time.sleep(1)
    #element = WebDriverWait(browser, 10).until(
    #    EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[2]/div/div[10]/div/a')))
    #browser.execute_script("arguments[0].click();", element2)
    browser.find_element(by=By.XPATH, value='/html/body/div[2]/div[2]/div/div[10]/div/a').click()
    #time.sleep(1)
    #driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    #time.sleep(2)
    #print(WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='qa6 qmz qn0']"))).text)

    response = browser.page_source.encode('utf-8')
    soup = BeautifulSoup(response, 'html.parser')
    links = soup.find_all('a', class_='ws2-pusher-banner-anchor')
    linkslist = []
    for a in links[1::]:
        if (a.findChild('p').getText()) == 'Total War: WARHAMMER III':
            linkslist.append(a['href'])
    return linkslist
#print(parsing())
def showtext(url):
    # extract and compose text from requested URL
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    linktitle = soup.find_all('h1', class_='tw18-single-title')
    headstring = ''
    for elem in linktitle:
        headstring += elem.getText()
    linktext = soup.find_all('div', class_='ca-block-wrapper blockName-')
    textstring = ''
    for el in linktext:
        for letter in el.getText():
            textstring += letter
            if len(textstring) > 3500 and letter == '\n':
                textstring += f' \n Продолжение по ссылке:'
                break
    return f'{headstring} \n {textstring} \n {url}'



