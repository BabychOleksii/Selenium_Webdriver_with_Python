from selenium import webdriver
from selenium.webdriver.chrome.service import Service

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("headless")
chrome_options.add_argument("--ignore-certificate-errors")
chrome_options.add_argument("--start-maximized")

service_obj = Service('D:\\Projects\\Webdriver\\chromedriver.exe')
driver = webdriver.Chrome(service=service_obj, options=chrome_options)
driver.implicitly_wait(3)

driver.get("https://www.rahulshettyacademy.com/AutomationPractice/")

driver.execute_script("window.scrollBy(0,document.body.scrollHeight);")
driver.get_screenshot_as_file("screen.png")
