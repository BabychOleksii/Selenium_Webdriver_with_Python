import pytest
from selenium import webdriver

from selenium.webdriver.chrome.service import Service


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )


@pytest.fixture(scope="class")
def setup(request):
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        driver = webdriver.Chrome(service=Service(executable_path="D:\\Projects\\Webdriver\\chromedriver.exe"))
    elif browser_name == "firefox":
        driver = webdriver.Firefox(service=Service(executable_path="D:\\Projects\\Webdriver\\geckodriver.exe"))
    elif browser_name == "edge":
        driver = webdriver.Firefox(service=Service(executable_path="D:\\Projects\\Webdriver\\msedgedriver.exe"))
        print("edge driver")
    driver.get("https://rahulshettyacademy.com/angularpractice/")
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()

