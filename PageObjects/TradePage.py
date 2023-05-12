from selenium.webdriver.common.by import By


class TradePage:
    def __init__(self, driver):
        self.driver = driver

    symbol = (By.CSS_SELECTOR, "#navigation-symbol-search")
    buy = (By.CSS_SELECTOR, "button[aria-label='Buy A M Z N']")
    qty = (By.CSS_SELECTOR, "input[value='100']")
    order_dropdown = (By.CSS_SELECTOR, "button[aria-label='Order Type']")
    market_order = (By.XPATH, "(//li[normalize-space()='MARKET'])")
    tif = (By.XPATH, "//button[@aria-label='Time in Force']")
    day_order = (By.XPATH, "//li[@data-testid='tif-dropdown:DAY']")
    review_button = (By.XPATH, "//button[@id='review-order-button']")

    def get_symbol(self):
        return self.driver.find_element(*TradePage.symbol)

    def get_buy_button(self):
        return self.driver.find_element(*TradePage.buy)

    def get_qty(self):
        return self.driver.find_element(*TradePage.qty)

    def get_order_dropdown(self):
        return self.driver.find_element(*TradePage.order_dropdown)

    def get_market_order(self):
        return TradePage.market_order

    def get_tif(self):
        return self.driver.find_element(*TradePage.tif)

    def get_day_order(self):
        return TradePage.day_order

    def get_review_button(self):
        return self.driver.find_element(*TradePage.review_button)
