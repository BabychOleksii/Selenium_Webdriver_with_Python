from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--start-maximized")

service_obj = Service('D:\\Projects\\Webdriver\\chromedriver.exe')
driver = webdriver.Chrome(service=service_obj, options=chrome_options)

driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")

browserSortVeggies = []

# click on column header
driver.find_element(By.XPATH, "//span[text()='Veg/fruit name']").click()

# collect all veggie names into Browser sorted list
veggieWebElements = driver.find_elements(By.XPATH, "//tr/td[1]")
for elem in veggieWebElements:
    browserSortVeggies.append(elem.text)

originalBrowserSortVeggies = browserSortVeggies.copy()

# Sort this browserSortVeggies list into a new sorted list
browserSortVeggies.sort()

assert browserSortVeggies == originalBrowserSortVeggies

