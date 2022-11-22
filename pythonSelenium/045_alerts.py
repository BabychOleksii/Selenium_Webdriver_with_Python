from selenium import webdriver

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service('D:\\Projects\\Webdriver\\chromedriver.exe')
driver = webdriver.Chrome(service=service_obj)

driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()

name = "Alex"

driver.find_element(By.CSS_SELECTOR, value="#name").send_keys(name)
driver.find_element(By.ID, value="alertbtn").click()
alert = driver.switch_to.alert
alertText = alert.text
assert name in alertText
alert.accept()
# alert.dismiss()
