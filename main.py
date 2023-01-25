from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import os
import time


chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
navegador = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)


navegador.get("https://www.google.com.br/")
time.sleep(5)
navegador.find_element('xpath', '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys("@esaj tjms", Keys.ARROW_DOWN)
time.sleep(5)
navegador.find_element('xpath', '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[4]/center/input[1]').click()
time.sleep(5)
navegador.find_element('xpath', '//*[@id="rso"]/div[1]/div/div/div/div/div/div/div[1]/a/h3').click()
time.sleep(5)

print("OK")
