from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://www.google.com/")

search = driver.find_element(By.XPATH, "//input[@title='Search']")
search.click()
search.send_keys("World's most powerful computers")
search.send_keys(Keys.ENTER)

results = driver.find_elements(By.TAG_NAME, "a")
print(len(results))

count = len(results)

def test1():
    expectedvalue = count
    actualvalue = 10
    assert 10 <= expectedvalue
