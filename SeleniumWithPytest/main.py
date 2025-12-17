import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

options = Options()
# Puedes añadir opciones si lo necesitas, por ejemplo:
# options.add_argument('--headless')

service = Service(executable_path='C:/workspace/python_projects/curso-python-qa/SeleniumWithPytest/drivers/chromedriver.exe')
driver = webdriver.Chrome(service=service, options=options)
driver.get('https://testpages.herokuapp.com/pages/forms/text-inputs/')
time.sleep(5) # Let the user actually see something!
web_element = driver.find_element(By.NAME, "text")
web_element.send_keys('ChromeDriver' + Keys.ENTER)
web_element = driver.find_element(By.__type_params__, "submit").click()
time.sleep(5) # Let the user actually see something!
driver.quit()