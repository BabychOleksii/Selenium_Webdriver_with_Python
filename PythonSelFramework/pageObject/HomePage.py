from selenium.webdriver.common.by import By

from PythonSelFramework.pageObject.CheckoutPage import CheckoutPage


class HomePage:
    def __init__(self, driver):
        self.driver = driver

    shop = (By.CSS_SELECTOR, "a[href*='shop']")

    def shopItems(self):
        self.driver.find_element(*HomePage.shop).click()
        checkoutPage = CheckoutPage(self.driver)
        return checkoutPage
        # the same as - driver.find_element(By.CSS_SELECTOR, "a[href*='shop']").click()

