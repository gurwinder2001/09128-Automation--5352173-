from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://www.youtube.com/")

search = driver.find_element(By.XPATH, "//input[@id='search']")
search.click()
search.send_keys("what is selenium and how it works")
search.send_keys(Keys.ENTER)

results = driver.find_elements(By.ID, "video-title")
print(len(results))
time.sleep(20)

count = len(results)

def test_a():
    expectedvalue = count
    actualvalue = 5
    assert 5 <= expectedvalue

