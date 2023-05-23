from time import sleep
from selenium.webdriver import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from BaseClass import BaseClass
from PageObjects.LinkPage import LinkPage
from PageObjects.LoginPage import LoginPage
from PageObjects.TradePage import TradePage


class TestEnd2End(BaseClass):
    def test_e2e(self):
        link = LinkPage(self.driver)
        link.get_link().click()
        login = LoginPage(self.driver)
        login.get_username().send_keys("natichiko")
        login.get_password().send_keys("Naqerala00.")
        login.get_login_button().click()
        tradePage = TradePage(self.driver)
        tradePage.get_symbol().send_keys("AMZN")
        tradePage.get_symbol().send_keys(Keys.ENTER)
        tradePage.get_buy_button().click()
        tradePage.get_qty().send_keys(Keys.BACKSPACE * 3)
        tradePage.get_qty().send_keys("500")
        tradePage.get_order_dropdown().click()
        market_order = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(tradePage.get_market_order()))
        sleep(4)
        market_order.click()
        tradePage.get_tif().click()
        time_in_force = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(tradePage.day_order))
        sleep(3)
        time_in_force.click()
        tradePage.get_review_button().click()
        logger = self.get_logger()
        logger.info(tradePage)
        print("hello")
        print("hallo")
        print("hola")
