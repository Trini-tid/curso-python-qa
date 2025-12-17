from selenium.webdriver.common.by import By

base_url = "https://testautomationpractice.blogspot.com/"


class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.name = "name"
        self.email = "email"

    def get_name(self):
        return self.driver.find_element(By.ID, self.name)

    def get_email(self):
        return self.driver.find_element(By.ID, self.email)