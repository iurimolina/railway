from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import os
import time


chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
navegador = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)


navegador.get("https://esaj.tjms.jus.br/esaj/portal.do?servico=740000")
time.sleep(5)
navegador.find_element('xpath', '//*[@id="identificacao"]/strong/a').click()
time.sleep(5)
navegador.find_element('xpath', '//*[@id="usernameForm"]').send_keys("52812952172", Keys.ARROW_DOWN)
time.sleep(5)
navegador.find_element('xpath', '//*[@id="passwordForm"]').send_keys("@Afonso4710", Keys.ARROW_DOWN)
time.sleep(5)
navegador.find_element('xpath', '//*[@id="pbEntrar"]').click()
time.sleep(5)
print("OK")
