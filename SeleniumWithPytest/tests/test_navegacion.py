import time
from pytest import mark 
from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert

@mark.selenium
def test_links_navg():
    driver = webdriver.Chrome()
    driver.get("https://testautomationpractice.blogspot.com")
    print("URL actual: ", driver.current_url)
    
    driver.find_element(By.LINK_TEXT, "Udemy Courses").click()
    print("URL actual: ", driver.current_url)
    time.sleep(3)
    
    driver.back()
    print("URL actual: ", driver.current_url)
    time.sleep(3)
    
    driver.forward()
    print("URL actual: ", driver.current_url)
    
    driver.refresh()    
    print("URL actual: ", driver.current_url)
    
    time.sleep(3)
    driver.close()


@mark.selenium
def test_alerts_windows():
    driver = webdriver.Chrome()
    driver.get("https://testautomationpractice.blogspot.com")
    
    driver.find_element(By.ID, "alertBtn").click()
    time.sleep(3)
    alert_window = Alert(driver)
    texto_alert = alert_window.text
    print(texto_alert)
    assert texto_alert == "I am an alert box!"
    
    alert_window.accept()
    
    driver.find_element(By.ID, "confirmBtn").click()
    time.sleep(3)
    alert_window = Alert(driver)
    alert_window.dismiss()
          
    time.sleep(35)
    driver.close()
    

@mark.ui
def test_alerts_windows():
    driver = webdriver.Chrome()
    driver.get("https://testautomationpractice.blogspot.com")
    driver.maximize_window()
    driver.save_screenshot("./img1.png")
