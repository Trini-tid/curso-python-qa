import time
from pytest import mark # type: ignore
from selenium import webdriver # type: ignore
from selenium.webdriver.common.by import By # type: ignore

@mark.selenium
def test_element_by_id():
    driver = webdriver.Chrome()
    driver.get("https://testautomationpractice.blogspot.com")
    
    web_element = driver.find_element(By.ID, "field2").send_keys("Juan")
    
    time.sleep(10)
    driver.close()

@mark.selenium
def test_element_by_name():
    driver = webdriver.Chrome()
    driver.get("https://testautomationpractice.blogspot.com")
    
    driver.find_element(By.CLASS_NAME, 'form-control').send_keys("MyName")
        
    time.sleep(10)
    driver.close()

@mark.selenium
def test_elements_list():
    driver = webdriver.Chrome()
    driver.get("https://testautomationpractice.blogspot.com")
    
    web_element=driver.find_elements(By.CLASS_NAME, 'form-control')
    print ("Numero de veces que aparece ese elemento: ", len(web_element))
    web_element[2].send_keys("699123456")
        
    time.sleep(10)
    driver.close()

@mark.selenium
def test_element_by_xpath():
    driver = webdriver.Chrome()
    driver.get("https://testautomationpractice.blogspot.com")    
        
    #full xpath  for phone
    driver.find_element(By.XPATH, '/html/body/div[4]/div[2]/div[2]/div[2]/div[2]/div[2]/div[2]/div/div[4]/div[1]/div/div/div[1]/div[1]/div/div/div/div/div[2]/div[1]/input[2]').send_keys("699123456")
    print("full xpath")
    time.sleep(5)
    
    #xpath for address
    driver.find_element(By.XPATH, '//*[@id="textarea"]').send_keys("My address 8, 1-A")
    print("xpath")
    time.sleep(5)
    
    driver.close()

