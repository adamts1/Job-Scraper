from selenium import webdriver
from page.jobs_page import JobsPages
import logging

logging.basicConfig(format='%(asctime)s %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s',
                    datefmt='%d-%m-%Y %H:%M:%S',
                    level=logging.INFO,
                    filename='logs.txt')
logger = logging.getLogger('scraping')


driver = webdriver.Chrome('C:/Users/Adam/Main/The Comlete Python course/12_browser_automation/chromedriver_win32/chromedriver.exe')
driver.get("https://www.drushim.co.il/")
driver.maximize_window()



###########################
category_input = "אינטרנט"
area_input = "מרכז"

page = JobsPages(driver)
# logger.info(page)

print(page.orchestrator("Python", category_input, area_input))







