import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("https://www.google.com")
time.sleep(6)
driver.find_element(By.XPATH,'//*[@id="L2AGLb"]/div').click()
time.sleep(6)
web_element =driver.find_element(By.NAME, 'q')
web_element.send_keys("Selenium Webdriver" + Keys.ENTER)

time.sleep(10)
driver.quit()