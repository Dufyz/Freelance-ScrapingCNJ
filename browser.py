from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from headers import LINK_MAIN

browser = webdriver.Chrome()

browser.headless = True 
wait = WebDriverWait(browser, 5)

def getBrowserDriver():
    browser.get(LINK_MAIN)
    browser.maximize_window()
    return browser, wait