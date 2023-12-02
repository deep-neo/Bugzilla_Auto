# login_page.py
from selenium.webdriver.common.by import By

class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def login(self, username, password):
        self.driver.find_element(By.ID, "Bugzilla_login").send_keys(username)
        self.driver.find_element(By.ID, "Bugzilla_password").send_keys(password)
        self.driver.find_element(By.ID, "log_in").click()
