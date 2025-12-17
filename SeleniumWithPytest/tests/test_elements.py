import time
from pytest import mark # type: ignore
from selenium import webdriver # type: ignore
from selenium.webdriver.common.by import By # type: ignore
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from datetime import date 

@mark.selenium
def test_textareas():
    driver = webdriver.Chrome()
    driver.get("https://testautomationpractice.blogspot.com")
    driver.maximize_window()
    driver.set_window_size(1024, 768)
    
    textarea_elmt = driver.find_element(By.ID, "textarea")
    textarea_elmt.send_keys("Hola mundo")
    textarea_elmt.clear()
    textarea_elmt.send_keys("Hola de nuevo")
    time.sleep(3)
    
    actual_value = textarea_elmt.get_attribute('value')
    print(actual_value)
    
    time.sleep(3)
    driver.close()

@mark.selenium
def test_elemento_checkbox():
    driver = webdriver.Chrome()
    driver.get("https://testautomationpractice.blogspot.com")
    
    checkbox_elmt = driver.find_element(By.ID, "monday")
    checkbox_elmt.click()
    
    print("Tipo de elemento: ", checkbox_elmt.get_attribute('type'))
    print("Seleccionado: ", checkbox_elmt.is_selected())

    time.sleep(3)
    driver.close()

@mark.selenium
def test_elemento_calendar():
    driver = webdriver.Chrome()
    driver.get("https://testautomationpractice.blogspot.com")
    
    myfecha = date.today().strftime("%m/%d/%Y")
    
    calendar_elmt = driver.find_element(By.ID, "datepicker")
    calendar_elmt.click()    
    time.sleep(3)    
    driver.find_element(By.XPATH, "//*[@class = 'ui-state-default' and text() = '20']").click()
    time.sleep(3)
    print("fecha1: " , calendar_elmt.get_attribute('value'))
    calendar_elmt.clear()
    
    calendar_elmt.send_keys(myfecha)
    print("fecha2: " , calendar_elmt.get_attribute('value')) 
    
    #el segundo datapicker es readonly
    calendar_elmt2 = driver.find_element(By.ID, "txtDate")
    calendar_elmt2.send_keys(myfecha) #no debe de dejar escribir
    print("fecha: " , calendar_elmt2.get_attribute('value')) #expected vacío
    
    time.sleep(3)
    driver.close()

@mark.selenium
def test_elemento_combobox():
    driver = webdriver.Chrome()
    driver.get("https://testautomationpractice.blogspot.com")
    
    select_country = Select(driver.find_element(By.ID, "country"))
    select_country.select_by_value("japan")
    time.sleep(2)
    select_country.select_by_index(2) #United Kingdom
    time.sleep(3)
    driver.close()

@mark.selenium
def test_drag_and_drop():
    driver = webdriver.Chrome()
    driver.get("https://testautomationpractice.blogspot.com")

    drag_element = driver.find_element(By.ID, "draggable")
    drop_area = driver.find_element(By.ID, "droppable")
    
    action = ActionChains (driver)
    action.drag_and_drop(drag_element, drop_area).perform()

    time.sleep(3)
    driver.close()



