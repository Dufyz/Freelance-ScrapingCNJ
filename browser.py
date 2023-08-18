from pathlib import Path

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from headers import LINK_MAIN

# Criando folders que serão utilizados para salvar os arquivos
PATH_DESKTOP = str(Path.home()) + "\Desktop"

browser = webdriver.Chrome()

browser.headless = True 
wait = WebDriverWait(browser, 3)

def getBrowserDriver():
    browser.get(LINK_MAIN)
    browser.maximize_window()
    return browser, wait