from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import os
import time


chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--incognito")
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
navegador = webdriver.Chrome(service=Service(ChromeDriverManager(version='108.0.5359.71').install()), options=chrome_options)

navegador.get("https://www.tjms.jus.br/")
print(navegador.title)
