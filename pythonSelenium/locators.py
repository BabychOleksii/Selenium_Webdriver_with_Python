from selenium import webdriver

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service('D:\\Projects\\Webdriver\\chromedriver.exe')
driver = webdriver.Chrome(service=service_obj)

driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.maximize_window()

# ID, Xpath, CSSSelector, classname, name, linkText
driver.find_element(By.NAME, value="email").send_keys("alexbaum@mail.net")
driver.find_element(By.ID, "exampleInputPassword1").send_keys('123456')
driver.find_element(By.ID, value="exampleCheck1").click()

driver.find_element(By.CSS_SELECTOR, value="input[name='name']").send_keys("Alex")
driver.find_element(By.CSS_SELECTOR, "#inlineRadio1").click()
driver.find_element(By.XPATH, "//input[@type='submit']").click()

message = driver.find_element(By.CLASS_NAME, 'alert-success').text
print(message)
assert "Success" in message
# assert "Fail" in message

driver.find_element(By.XPATH, "(//input[@type='text'])[3]").send_keys("HelloAgain")
driver.find_element(By.XPATH, "(//input[@type='text'])[3]").clear()
