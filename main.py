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
navegador = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

navegador.get("https://www.google.com.br/")
print(navegador.title)

#navegador.find_element('xpath', '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys("instagram", Keys.ARROW_DOWN)
#navegador.find_element('xpath', '//*[@id="rso"]/div[1]/div/div/div/div/div/div/div[1]/a').click()
#print("ESAJ")
navegador.close()
