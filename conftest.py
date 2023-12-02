# conftest.py
import pytest
from selenium import webdriver
from utils.config import CHROME_DRIVER_PATH

@pytest.fixture
def driver(request):
    driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)
    request.addfinalizer(driver.quit)
    return driver
