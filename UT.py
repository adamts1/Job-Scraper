from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

desired_cap = {
'browserName': 'android',
'device': 'Samsung Galaxy Note 9',
'realMobile': 'true',
'os_version': '8.1',
'name': 'Bstack-[Python] Sample Test'
}

driver = webdriver.Remote(
command_executor='https://www.drushim.co.il/',
desired_capabilities=desired_cap)

driver.get("https://www.google.com")
if not "Google" in driver.title:
 raise Exception("Unable to load google page!")
elem = driver.find_element_by_name("q")
elem.send_keys("BrowserStack")
elem.submit()
print (driver.title)
driver.quit()