import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

service = Service(executable_path=ChromeDriverManager().install())  # создаём объект service
driver = webdriver.Chrome(service=service)

driver.get("https://av.by")

time.sleep(8)

driver.back()

time.sleep(3)

driver.forward()

time.sleep(3)

driver.refresh()
