from selenium.webdriver.common.by import By

from PythonSelFramework.pageObject.ConfirmPage import ConfirmPage


class CheckoutPage:

    def __init__(self, driver):
        self.driver = driver

    # rewrite this - products = self.driver.find_elements(By.XPATH, "//div[@class='card h-100']")
    cardTitle = (By.XPATH, "//div[@class='card h-100']")

    # rewrite this - product.find_element(By.CSS_SELECTOR, ".card-footer button")
    cardFooter = (By.CSS_SELECTOR, ".card-footer button")

    # rewrite this - driver.find_element(By.XPATH, "//button[@class='btn btn-success']")
    checkOut = (By.XPATH, "//button[@class='btn btn-success']")

    def getCardTitle(self):
        return self.driver.find_elements(*CheckoutPage.cardTitle)

    def getCardFooter(self):
        return self.driver.find_element(*CheckoutPage.cardFooter)

    def checkoutItems(self):
        self.driver.find_element(*CheckoutPage.checkOut).click()
        confirmPage = ConfirmPage(self.driver)
        return confirmPage


