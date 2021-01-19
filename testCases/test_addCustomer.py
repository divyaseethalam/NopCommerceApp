import pytest
import time
from pageObjects.LoginPage import Login
from pageObjects.AddCustomerPage import AddCustomer
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
import string
import random

class Test_003_AddCustomer:

    baseURL=ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    @pytest.mark.sanity
    def test_addcustomer(self,setup):
        self.logger.info("**************Test_003_AddCustomer*******************")
        self.driver=setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp=Login(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("**************login successfull**********")

        self.logger.info("****************starting add customer test**********")

        self.addcust = AddCustomer(self.driver)
        self.addcust.clickOnCustomerMenu()
        self.addcust.clickOnCustomerMenuItem()
        self.addcust.clickOnAddNew()
        self.logger.info("**********providing customer info**********")

        self.email = random_generator() + "@gmail.com"
        self.addcust.setEmail(self.email)
        self.addcust.setPassword("test123")
        self.addcust.setFirstname("Teja")
        self.addcust.setLastName("Pavan")
        self.addcust.setDateOfBirth("5/24/1995")#mm-dd-yy
        self.addcust.setCompanyName("busyQA")
        self.addcust.setAdmincomment("this is teting")
        self.addcust.clickOnSave()

        self.logger.info("***********saving cutomer info*******")
        self.logger.info("*****************Add customer validation started********")

        self.msg = self.driver.find_element_by_tag_name("body").text

        print(self.msg)
        if 'customer has been added successfully.' in self.msg:
            assert True == True
            self.logger.info("*************Add customer test passed*********")
        else:
            #Screenshot
            self.driver.save_screenshot(".\\Screenshots\\"+"test_addCustomer_scr.png")
            self.logger.error("********Add Customer Test Failed*****")
            assert True == False

        self.driver.close()
        self.logger.info("*************Add Customer test  ******************")


        #its a user defined function,to generate random data
def random_generator(size=8, chars=string.ascii_lowercase + string.digits):
    #its a loopig stm every time it will generate new haracter
    return ''.join(random.choice(chars) for x in range(size))













