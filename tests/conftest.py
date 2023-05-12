import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service


@pytest.fixture(scope='class')
def setup(request):
    options = Options()
    options.add_argument("__start-maximized")
    options.add_argument("__ignore-certificate-errors")
    options.add_experimental_option("detach", True)
    service_obj = Service("C:\\Users\\nchik\\chromedriver_win32 (2)\\chromedriver.exe")
    driver = webdriver.Chrome(service=service_obj, options=options)
    driver.implicitly_wait(10)
    driver.get("https://www.tdameritrade.com/tools-and-platforms/thinkorswim/web.html?TID=NA&ef_id=Cj0KCQjwpPKiBhDvARIsACn-gzB9LAhpQUIk4VQF-3QSSoBhaI0__SE3qC-thw5bdcUge5QbvAidXG4aArlREALw_wcB:G:s&s_kwcid=AL!2521!3!518660092256!e!!g!!thinkorswim%20paper%20money%20login&CID=PSTOS&gad=1&dclid=CjgKEAjwpPKiBhCd4ujAufCtg0kSJADS989r_r-KRpJPPb_fTQM2pQFjUkxgKp4EDM_3O75wS7AL7vD_BwE")
    request.cls.driver = driver
    yield
    driver.quit()
