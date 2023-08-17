from pathlib import Path

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from headers import LINK_MAIN


# Criando folders que serão utilizados para salvar os arquivos
PATH_DESKTOP = str(Path.home()) + "\Desktop"

# Cursores driver Browser
# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument('--kiosk-printing')
# chrome_options.add_argument('--no-sandbox')
# browser = webdriver.Chrome(r"chromedriver.exe", options=chrome_options)

browser = webdriver.Chrome()

browser.headless = True 
wait = WebDriverWait(browser, 10)

def getBrowserDriver():
    browser.get(LINK_MAIN)
    browser.maximize_window()
    return browser, wait