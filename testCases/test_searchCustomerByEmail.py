import pytest
import time
from pageObjects.LoginPage import Login
from pageObjects.AddCustomerPage import AddCustomer
from pageObjects.Searchcustomerpage import Searchcustomerpage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen

class Test_004_SearchCustomerByEmail:

    baseURL=ReadConfig.getApplicationURL()
    username=ReadConfig.getUseremail()
    password=ReadConfig.getPassword()
    logger = LogGen.loggen()


    @pytest.mark.regression
    def test_searchCustomerByEmail(self,setup):
        self.logger.info("***************Test_004_SearchCustomerByEmail********")
        self.driver=setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = Login(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("*************Login successful************")

        self.logger.info("*******starting search customer by email************")

        self.addcust=AddCustomer(self.driver)
        self.addcust.clickOnCustomerMenu()
        self.addcust.clickOnCustomerMenuItem()

        self.logger.info("***********searching customer by emailid***********")
        searchcust = Searchcustomerpage(self.driver)
        searchcust.setEmail("victoria_victoria@nopCommerce.com")
        searchcust.clickSearch()
        time.sleep(5)
        status=searchcust.searchCustomerByEmail("victoria_victoria@nopCommerce.com")
        assert True == status
        self.logger.info("**************Tc_SearchCustomerByEmail_004 Finished***********")

        self.driver.close()
