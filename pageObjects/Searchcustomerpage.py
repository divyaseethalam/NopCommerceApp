from selenium import webdriver


class Searchcustomerpage:

    txtEmail_xpath = "//input[@id='SearchEmail']"
    txtFirstname_xpath = "//input[@id='SearchFirstName']"
    txtLastname_xpath ="//input[@id='SearchLastName']"
    btnSearch_xpath = "//button[@id='search-customers']"

    tblSearchResults_xpath = "//table[@role='grid']"
    table_xpath = "//table[@id='customers-grid']"
    tableRows_xpath = "//table[@id='customers-grid']//tbody/tr"
    tableColumns_xpath = "//table[@id='customers-grid']//tbody/tr/td"

    def __init__(self,driver):
        self.driver = driver

    def setEmail(self,email):
        self.driver.find_element_by_xpath(self.txtEmail_xpath).clear()
        self.driver.find_element_by_xpath(self.txtEmail_xpath).send_keys(email)

    def setFirstName(self,firstname):
        self.driver.find_element_by_xpath(self.txtFirstname_xpath).clear()
        self.driver.find_element_by_xpath(self.txtFirstname_xpath).send_keys(firstname)

    def setLastName(self,lastname):
        self.driver.find_element_by_xpath(self.txtLastname_xpath).clear()
        self.driver.find_element_by_xpath(self.txtLastname_xpath).send_keys(lastname)

    def clickSearch(self):
        self.driver.find_element_by_xpath(self.btnSearch_xpath).click()

    def getNoOfRows(self):
        return len(self.driver.find_elements_by_xpath(self.tableRows_xpath))

    def getNoOfColumns(self):
        return len(self.driver.find_elements_by_xpath(self.tableColumns_xpath))

    def searchCustomerByEmail(self,email):
        flag=False
        for r in range(1,self.getNoOfRows()+1):
            table=self.driver.find_element_by_xpath(self.table_xpath)
            emailid=table.find_element_by_xpath("//table[@id='customers-grid']/tbody/tr["+str(r)+"]/td[2]").text
            if emailid == email:
                flag = True
                break
        return flag

    def searhCustomerByName(self,Name):
        flag=False
        for r in range(1,self.getNoOfRows()+1):
            table = table=self.driver.find_element_by_xpath(self.table_xpath)
            name=table.find_element_by_xpath("//table[@id='customers-grid']/tbody/tr["+str(r)+"]/td[3]").text
            if name == Name:
                flag = True
                break
        return flag