from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from urllib3.packages.six import b

from page.jobs_page import JobsPages



driver = webdriver.Chrome('C:/Users/Adam/Main/The Comlete Python course/12_browser_automation/chromedriver_win32/chromedriver.exe')
driver.get("https://www.drushim.co.il/")
driver.maximize_window()

driver.find_element_by_class_name("selectBox-label").click()
# driver.find_element_by_xpath("//*[@id=\"body\"]/ul[3]/li[6]").click()
x = len(driver.find_elements_by_xpath("//*[@id=\"body\"]/ul[3]/li"))
print(x)
print(type(x))
input = "אבטחת מידע"

for el in range(1, x):
    str_el = str(el)
    option = driver.find_element_by_xpath(f"//*[@id=\"body\"]/ul[3]/li[{str_el}]/a").text
    if option == input:
        driver.find_element_by_xpath(f"//*[@id=\"body\"]/ul[3]/li[{str_el}]").click()
        break



a = driver.find_elements_by_class_name("selectBox-label")
a[1].click()
x = len(driver.find_elements_by_xpath("//*[@id=\"body\"]/ul[4]/li"))
input = "מרכז"

for el in range(1, x):
    str_el = str(el)
    option = driver.find_element_by_xpath(f"//*[@id=\"body\"]/ul[4]/li[{str_el}]/a").text
    print(option)
    if option == input:
        driver.find_element_by_xpath(f"//*[@id=\"body\"]/ul[4]/li[{str_el}]").click()
        break


# Teamname = driver.find_element_by_xpath("//*[@id=\"body\"]/ul[3]/li[1]/a").text
# print(Teamname)



# a = []
# a = driver.find_elements_by_class_name("selectBox-label")
# a[1].click()
# print(driver.find_element_by_xpath("//*[@id=\"body\"]/ul[4]/li[3]/a").text)
