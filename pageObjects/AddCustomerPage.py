import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select

class AddCustomer:
#locators for that page
    lnkCustomers_menu_xpath = "//a[@href='#']//span[contains(text(),'Customers')]"
    lnkCustomers_menuitem_xpath = "//span[@class='menu-item-title'][contains(text(),'Customers')]"
    btnAddnew_xpath = "//a[@class='btn bg-blue']"

    txtEmail_xpath = "//input[@id='Email']"
    txtPasword_xpath = "//input[@id='Password']"
    txtFirstname_xpath = "//input[@id='FirstName']"
    txtLasttime_xpath = "//input[@id='LastName']"
    rdFemaleGender_xpath = "//input[@id='Gender_Female']"
    rdMaleGender_xpath = "//input[@id='Gender_Male']"
    txtDOB_xpath = "//input[@id='DateOfBirth']"
    txtCmpname_xpath = "//input[@id = 'Company']"

    txtCustomerRoles_xpath = "//body/div[3]/div[3]/div[1]/form[1]/div[3]/div[1]/nop-panels[1]/nop-panel[1]/div[1]/div[2]/div[1]/div[10]/div[2]/div[1]/div[1]/div[1]"
    lstitemRegistered_xpath = "//li[contains(text(),'Registered')]"
    lstitemAdministration_xpath = "//li[contains(text(),'Administrators')]"
    lstitemGuests_xpath = "//li[contains(text(),'Guests')]"
    lstitemVendor_xpath = "//li[contains(text(),'Vendors')]"

    drpManagerOfVendor_xpath = "//select[@id='VendorId']"

    chkIsTaxExempt_xpath="//input[@id='IsTaxExempt']"

    chkActive_xpath="//input[@checked='checked']"
    txtAdminComment_xpath="//textarea[@class='form-control']"
    btnSave_xpath = "//button[@name='save']"

#action methods
    def __init__(self,driver):
        self.driver=driver

    def clickOnCustomerMenu(self):
        self.driver.find_element_by_xpath(self.lnkCustomers_menu_xpath).click()

    def clickOnCustomerMenuItem(self):
        self.driver.find_element_by_xpath(self.lnkCustomers_menuitem_xpath).click()

    def clickOnAddNew(self):
        self.driver.find_element_by_xpath(self.btnAddnew_xpath).click()

    def setEmail(self,email):
        self.driver.find_element_by_xpath(self.txtEmail_xpath).send_keys(email)


    def setPassword(self,password):
        self.driver.find_element_by_xpath(self.txtPasword_xpath).send_keys(password)

    def setFirstname(self,firstname):
        self.driver.find_element_by_xpath(self.txtFirstname_xpath).send_keys(firstname)

    def setLastName(self,lastname):
        self.driver.find_element_by_xpath(self.txtLasttime_xpath).send_keys(lastname)

    def setDateOfBirth(self,dateofbirth):
        self.driver.find_element_by_xpath(self.txtDOB_xpath).send_keys(dateofbirth)

    def setCompanyName(self,companyname):
        self.driver.find_element_by_xpath(self.txtCmpname_xpath).send_keys(companyname)

    def setCustomerRoles(self,role):
        self.driver.find_element_by_xpath(self.txtCustomerRoles_xpath).click()
        time.sleep(3)
        if role == 'Registered':
            self.listitem=self.driver.find_element_by_xpath(self.lstitemRegistered_xpath)
        elif role == 'Administrators':
            self.listitem=self.driver.find_element_by_xpath(self.lstitemAdministration_xpath)
        elif role=='Guests':
            #here user can be either guest (or) registered but not both
            time.sleep(3)
            self.driver.find_element_by_xpath("//*[@id='SelectedCustomerRoleIds_taglist']/li/span[2]").click()
            self.listitem=self.driver.find_element_by_xpath(self.lstitemGuests_xpath)
        elif role=='Vendors':
            self.listitem=self.driver.find_element_by_xpath(self.lstitemVendor_xpath)
        else:
            self.driver.find_element_by_xpath(self.lstitemGuests_xpath)
            #self.listitem.click()(if click is not executed then use execute_script)
            self.driver.execute_script("arguments[0].click();",self.listitem)

    def setManagerOfVendor(self,value):
        drp = Select(self.driver.find_element_by_xpath(self.drpManagerOfVendor_xpath))
        drp.select_by_visible_text(value)

    def setGender(self,gender):
        if gender=='Male':
            self.driver.find_element_by_xpath(self.rdMaleGender_xpath).click()
        elif gender=='Female':
            self.driver.find_element_by_xpath(self.rdFemaleGender_xpath).click()
        else:
            self.driver.find_element_by_xpath(self.rdMaleGender_xpath).click()

    def setAdmincomment(self,content):
        self.driver.find_element_by_xpath(self.txtAdminComment_xpath).send_keys(content)

    def clickOnSave(self):
        self.driver.find_element_by_xpath(self.btnSave_xpath).click()
















