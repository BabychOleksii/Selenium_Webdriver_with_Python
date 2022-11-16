import time

from selenium import webdriver

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

service_obj = Service('D:\\Projects\\Webdriver\\chromedriver.exe')
driver = webdriver.Chrome(service=service_obj)

# Static dropdown
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.maximize_window()

dropdown = Select(driver.find_element(By.ID, "exampleFormControlSelect1"))
dropdown.select_by_visible_text("Female")
time.sleep(2)
dropdown.select_by_index(0)

# AutoSuggestive dynamic dropdowns
driver.get("https://rahulshettyacademy.com/dropdownsPractise/")

driver.find_element(By.ID, "autosuggest").send_keys("ind")
time.sleep(2)
countries = driver.find_elements(By.CSS_SELECTOR, value="li[class='ui-menu-item'] a")
print(len(countries))
for country in countries:
    if country.text == "India":
        country.click()
        break

# the .text can't get the value of dynamic field. Use .get_attribute for this case.
# print(driver.find_element(By.ID, value="autosuggest").text)
print(driver.find_element(By.ID, value="autosuggest").get_attribute('value'))
assert driver.find_element(By.ID, value="autosuggest").get_attribute('value') == "India"
