from selenium import webdriver

driver = webdriver.Chrome(
    'C:/Users/Adam/Main/The Comlete Python course/12_browser_automation/chromedriver_win32/chromedriver.exe')
driver.get("https://www.drushim.co.il/")
driver.maximize_window()
page = JobsPages(driver)
status = page.orchestrator("Python", category_input, area_input)
return status