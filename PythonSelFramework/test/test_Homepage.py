from PythonSelFramework.pageObject.HomePage import HomePage
from PythonSelFramework.utilities.BaseClass import BaseClass


class TestHomePage(BaseClass):

    def test_formSubmission(self):

        homepage = HomePage(self.driver)
        homepage.getName().send_keys("Alex")
        homepage.getEmail().send_keys("alexbaum@mail.net")
        homepage.getCheckBox().click()
        # sel = Select(homepage.getGender())
        # sel.select_by_visible_text("Male")
        self.selectOptionByText(homepage.getGender(), "Male")
        homepage.submitForm().click()

        alertText = homepage.getSuccessMessage().text

        assert ("Success" in alertText)

