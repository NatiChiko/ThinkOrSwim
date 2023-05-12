from selenium.webdriver.common.by import By


class LinkPage:
    def __init__(self, driver):
        self.driver = driver

    link = (By.LINK_TEXT, "Log in to thinkorswim Web")

    def get_link(self):
        return self.driver.find_element(*LinkPage.link)
