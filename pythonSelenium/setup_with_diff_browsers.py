from selenium import webdriver

# ----- Using downloaded webdriver -----
# =======================================

# This line is common for all 3 browsers
from selenium.webdriver.chrome.service import Service

# ----- Chrome browser -----
service_obj = Service('D:\\Projects\\Webdriver\\chromedriver.exe')
driver = webdriver.Chrome(service=service_obj)

# ----- Firefox browser -----
# service_obj = Service('D:\\Projects\\Webdriver\\geckodriver.exe')
# driver = webdriver.Firefox(service=service_obj)

# ----- Edge browser -----
# service_obj = Service('D:\\Projects\\msedgedriver.exe')
# driver = webdriver.Edge(service=service_obj)

# ----- Using external downloading and webdriver-manager -----
# ============================================================

# ----- Chrome browser -----
# from selenium.webdriver.chrome.service import Service as ChromeService
# from webdriver_manager.chrome import ChromeDriverManager
#
# driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
#
# ----- Firefox browser -----
# from selenium.webdriver.firefox.service import Service as FirefoxService
# from webdriver_manager.firefox import GeckoDriverManager
#
# driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
#
# ----- Edge browser -----
# from selenium.webdriver.edge.service import Service as EdgeService
# from webdriver_manager.microsoft import EdgeChromiumDriverManager
#
# driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))

driver.get("https://www.python.org/")

print(driver.title)
print(driver.current_url)