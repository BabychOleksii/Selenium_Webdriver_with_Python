import pytest

from PythonSelFramework.pageObject.HomePage import HomePage
from PythonSelFramework.utilities.BaseClass import BaseClass


class TestHomePage(BaseClass):

    def test_formSubmission(self, getData):

        homepage = HomePage(self.driver)
        homepage.getName().send_keys(getData[0])
        homepage.getEmail().send_keys(getData[1])
        homepage.getCheckBox().click()
        self.selectOptionByText(homepage.getGender(), getData[2])
        homepage.submitForm().click()

        alertText = homepage.getSuccessMessage().text

        assert ("Success" in alertText)

        self.driver.refresh()

    @pytest.fixture(params=[("Alex", "alexbaum@mail.net", "Male"), ("Helen", "helen@gmail.com", "Female")])
    def getData(self, request):
        return request.param
