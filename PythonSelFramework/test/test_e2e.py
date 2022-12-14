from selenium.webdriver.common.by import By

from PythonSelFramework.utilities.BaseClass import BaseClass
from PythonSelFramework.pageObject.HomePage import HomePage


class TestOne(BaseClass):

    def test_e2e(self):
        log = self.getLogger()
        homePage = HomePage(self.driver)
        checkoutPage = homePage.shopItems()
        # rewrite this - self.driver.find_element(By.CSS_SELECTOR, "a[href*='shop']").click()
        # rewrite this - checkoutPage = CheckoutPage(self.driver)
        log.info("getting all the card titles")
        products = checkoutPage.getCardTitle()
        # rewrite this -  products = self.driver.find_elements(By.XPATH, "//div[@class='card h-100']")

        for product in products:
            productName = product.find_element(By.XPATH, "div/h4/a").text
            log.info(productName)
            if productName == "Blackberry":
                checkoutPage.getCardFooter().click()
                # rewrite this - product.find_element(By.XPATH, "div/button").click()

        self.driver.find_element(By.CSS_SELECTOR, "a[class*='btn-primary']").click()
        confirmpage = checkoutPage.checkoutItems()
        # rewrite this - self.driver.find_element(By.XPATH, "//button[@class='btn btn-success']").click()
        log.info("Entering a country name as ind")
        self.driver.find_element(By.ID, "country").send_keys("ind")
        self.verifyLinkPresence("India")
        # rewrite this - wait = WebDriverWait(self.driver, 10)
        # rewrite this - wait.until(EC.presence_of_element_located((By.LINK_TEXT, "India")))
        self.driver.find_element(By.LINK_TEXT, "India").click()
        self.driver.find_element(By.XPATH, "//div[@class='checkbox checkbox-primary']").click()
        self.driver.find_element(By.CSS_SELECTOR, "[type='submit']").click()
        success_text = self.driver.find_element(By.CLASS_NAME, "alert-success").text
        log.info("text received from application is " + success_text)

        assert "Success! Thank you!" in success_text

