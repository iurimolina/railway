from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
myDriver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

myDriver.get("https://www.google.com")
print("Deploy Feito!!!")
