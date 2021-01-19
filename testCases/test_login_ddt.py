import pytest
from selenium import webdriver
from pageObjects.LoginPage import Login
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from utilities import XLUtils
import time


class Test_002_Login:
    baseURL = ReadConfig.getApplicationURL()
    path = ".//TestData/LoginData.xlsx"
    logger = LogGen.loggen()


    @pytest.mark.regression
    def test_login_ddt(self, setup):
        self.logger.info(("**********************Test_002_Login***************"))
        self.logger.info("*****************verify login DDt test*********************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = Login(self.driver)

        self.rows=XLUtils.getRowCount(self.path,'Sheet1')
        print("no.of rows in Excelsheet:",self.rows)
        list_status = []

        for r in range(2,self.rows+1):
            self.user=XLUtils.readData(self.path,'Sheet1',r,1)
            self.password=XLUtils.readData(self.path,'Sheet1',r,2)
            self.exp=XLUtils.readData(self.path,'Sheet1',r,3)
            self.lp.setUserName(self.user)
            self.lp.setPassword(self.password)
            self.lp.clickLogin()
            time.sleep(5)
            act_title = self.driver.title
            exp_title = "Dashboard / nopCommerce administration"

            if act_title == exp_title:
                if self.exp == "Pass":
                    self.logger.info("**************************Passed to login****************")
                    self.lp.clickLogout()
                    list_status.append("pass")

                elif self.exp =="Fail":
                    self.logger.info("******************failed to login***********************")
                    self.lp.clickLogout()
                    list_status.append("Fail")

            elif act_title != exp_title:

                if self.exp == "Pass":
                    self.logger.info("*****************failed*********************")

                    list_status.append("Fail")

                elif self.exp =="Fail":
                    self.logger.info("**************Passed*******************")

                    list_status.append("Pass")

        if "Fail" not in list_status:
            self.logger.info("*******************LoginDDT test Passed************")
            self.driver.close()
            assert True

        else:
            self.logger.info("****************LoginDDt Test failed********************")
            self.driver.close()
            assert False

        self.logger.info("***************End of Login DDT Test****************")
        self.logger.info("*************completed TC_Test_002_Login******************")









