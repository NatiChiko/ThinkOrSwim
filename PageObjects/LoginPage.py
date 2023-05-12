from selenium.webdriver.common.by import By


class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    username = (By.CSS_SELECTOR, "#username0")
    password = (By.CSS_SELECTOR, "#password1")
    loginButton = (By.CSS_SELECTOR, "#accept")


    def get_username(self):
        return self.driver.find_element(*LoginPage.username)

    def get_password(self):
        return self.driver.find_element(*LoginPage.password)

    def get_login_button(self):
        return self.driver.find_element(*LoginPage.loginButton)

