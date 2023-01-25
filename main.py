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
time.sleep(5)
navegador.get("https://esaj.tjms.jus.br/sajcas/login?service=https%3A%2F%2Fesaj.tjms.jus.br%2Fesaj%2Fj_spring_cas_security_check")
navegador.find_element('xpath', '//*[@id="usernameForm"]').send_keys("52812952172", Keys.ARROW_DOWN)
time.sleep(5)
navegador.find_element('xpath', '//*[@id="passwordForm"]').send_keys("@Afonso4710", Keys.ARROW_DOWN)
time.sleep(5)
navegador.find_element('xpath', '//*[@id="pbEntrar"]').click()
time.sleep(5)
print("OKAYYYYYYYYYYYYYY")
