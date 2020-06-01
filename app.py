from selenium import webdriver
from page.jobs_page import JobsPages



driver = webdriver.Chrome('C:/Users/Adam/Main/The Comlete Python course/12_browser_automation/chromedriver_win32/chromedriver.exe')
driver.get("https://www.drushim.co.il/")
driver.maximize_window()


###########################
category_input = "אינטרנט"
area_input = "מרכז"

page = JobsPages(driver)

print(page.orchestrator("Python", category_input, area_input))







