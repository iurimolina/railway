from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import os
import time


chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0;Win64) AppleWebkit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36")
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
navegador = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

time.sleep(25)
navegador.get("https://www.tjms.jus.br/")


print("OK")
