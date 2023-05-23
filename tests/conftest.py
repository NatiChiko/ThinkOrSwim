import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service


def pytest_addoption(parser):
    parser.addoption(
        "--browser-name", action="store", default="chrome"
    )


@pytest.fixture(scope='class')
def setup(request):
    global driver
    options = Options()
    options.add_argument("--start-maximized")
    options.add_argument("--ignore-certificate-errors")
    options.add_experimental_option("detach", True)
    browser_name = request.config.getoption("--browser-name")
    if browser_name == "chrome":
        service_obj = Service("C:\\Users\\nchik\\chromedriver_win32 (2)\\chromedriver.exe")
        driver = webdriver.Chrome(service=service_obj, options=options)
    elif browser_name == "firefox":
        service_obj = Service("C:\\ProgramData\\chocolatey\\bin\\geckodriver.exe")
        driver = webdriver.Firefox(service=service_obj)
    driver.implicitly_wait(15)
    driver.get("http://shopping.beeyor.com/")
    request.cls.driver = driver
    yield
    driver.quit()
