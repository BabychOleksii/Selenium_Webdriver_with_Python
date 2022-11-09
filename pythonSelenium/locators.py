from selenium import webdriver

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service('D:\\Projects\\Webdriver\\chromedriver.exe')
driver = webdriver.Chrome(service=service_obj)

driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.maximize_window()

driver.find_element(By.CSS_SELECTOR, value="input[name='name']").send_keys("Alex")
driver.find_element(By.NAME, value="email").send_keys("alexbaum@mail.net")
driver.find_element(By.ID, value="exampleCheck1").click()
driver.find_element(By.XPATH, value="//input[@type='submit']").click()
