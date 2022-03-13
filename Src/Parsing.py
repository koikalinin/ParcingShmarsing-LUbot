from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

def parsing():
    url = 'https://www.totalwar.com/blog/'
    s = Service('C:\chromedriver_win32\chromedriver.exe')
    browser = webdriver.Chrome(service=s)
    browser.get(url)
    time.sleep(3)
    browser.find_element(by=By.XPATH, value='/html/body/div[4]/div/div[2]/button[1]').click()
    time.sleep(1)
    browser.find_element(by=By.XPATH, value='/html/body/div[2]/div[2]/div/div[10]/div/a').click()
    time.sleep(3)
    response = browser.page_source.encode('utf-8')
    soup = BeautifulSoup(response, 'html.parser')
    links = soup.find_all('a', class_='ws2-pusher-banner-anchor')
    linkslist = []
    for a in links[1::]:
        if (a.findChild('p').getText())=='Total War: WARHAMMER III':
            linkslist.append(a['href'])
    return linkslist

def showtext(url):
    #url = 'https://www.totalwar.com/blog/tw-warhammer3-patch101/'
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


