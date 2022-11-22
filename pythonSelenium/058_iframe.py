from selenium import webdriver

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service('D:\\Projects\\Webdriver\\chromedriver.exe')
driver = webdriver.Chrome(service=service_obj)

driver.get("https://the-internet.herokuapp.com/iframe")
driver.maximize_window()

driver.switch_to.frame("mce_0_ifr")
driver.find_element(By.ID, "tinymce").clear()
driver.find_element(By.ID, "tinymce").send_keys("I am able to automate")
driver.switch_to.default_content()
print(driver.find_element(By.TAG_NAME, "h3").text)

