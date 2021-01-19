import pytest
from selenium import webdriver


@pytest.fixture()
# def setup():
#     driver = webdriver.Chrome("C:\\Divya\\PythonProject\\NopCommerceApp\\driver\chromedriver.exe")
#     return driver
# #
def setup(browser):
    if browser == 'chrome':
        driver = webdriver.Chrome("C:\\Divya\\PythonProject\\NopCommerceApp\\driver\\chromedriver.exe")
        print("launching chrome browser")
    elif browser == 'firefox':
        driver = webdriver.Firefox("C:\\Divya\\PythonProject\\NopCommerceApp\\driver\\geckodriver.exe")
        print("launching firefox browser")

    return driver


 # this will  get value from the commandprompt

def pytest_addoption(parser):
    parser.addoption("--browser")

#  this will return browser value to setup method
@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")


#######################Pytest Html reports##########################
#it is a hook for adding environment info to the html
def pytest_configure(config):
    config._metadata['Project Name'] = 'Nop Commerce'
    config._metadata['Module Name'] = 'Customers'
    config._metadata['Tester'] = 'Divya'

#it is hook for delete/Modify Environment info to HTML Report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("java_Home",None)
    metadata.pop("plugins",None)


