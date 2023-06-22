import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service


<<<<<<< HEAD
def pytest_addoption(parser):cd
=======
def pytest_addoption(parser):
>>>>>>> ea16bfbaf62c3aaf7e70990966e04e9a00d5a441
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
<<<<<<< HEAD
        service_obj = Service("C:\\Users\\nchik\\Downloads\\chromedriver_win32\\chromedriver.exe")
=======
        service_obj = Service("C:\\Users\\nchik\\chromedriver_win32 (2)\\chromedriver.exe")
>>>>>>> ea16bfbaf62c3aaf7e70990966e04e9a00d5a441
        driver = webdriver.Chrome(service=service_obj, options=options)
    elif browser_name == "firefox":
        service_obj = Service("C:\\ProgramData\\chocolatey\\bin\\geckodriver.exe")
        driver = webdriver.Firefox(service=service_obj)
    driver.implicitly_wait(15)
    driver.get("https://www.tdameritrade.com/tools-and-platforms/thinkorswim.html?TID=NA&ef_id=Cj0KCQjwjryjBhD0ARIsAMLvnF_-lfstevKaaZSZ6AuokimdFFNZ8SMoYueo_Q75MAfMEJoGngyIyKQaAuHTEALw_wcB:G:s&s_kwcid=AL!2521!3!516515983854!e!!g!!think%20or%20swim&CID=PSTOS&gad=1&dclid=CjgKEAjwjryjBhCO6t3GjrXByzcSJADfpqL9qkXUMfA91kEbJVqsEhZRf8MpkSQrvUjXeixlCQKPJ_D_BwE")
    request.cls.driver = driver
    yield
    driver.quit()

