from selenium import webdriver
from page.jobs_page import JobsPages
import logging
from global1.global_var import GlobalVar
from csv.csv_creator import CsvCreator


logging.basicConfig(format='%(asctime)s %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s',
                    datefmt='%d-%m-%Y %H:%M:%S',
                    level=logging.INFO,
                    filename='logs.txt')
logger = logging.getLogger('scraping')
###########################
category_input = "כל הקטגוריות"
area_input = "מרכז"


def start():
    driver = webdriver.Chrome(
        'C:/Users/Adam/Main/The Comlete Python course/12_browser_automation/chromedriver_win32/chromedriver.exe')
    driver.get("https://www.drushim.co.il/")
    driver.maximize_window()
    page = JobsPages(driver)
    status = page.orchestrator("Python", category_input, area_input)
    return status


if __name__ == '__main__':
    content = None
    retry = 3
    while content is None and retry != 0:
        content = start()
        retry = retry - 1
    print(content)

CsvCreator(GlobalVar.GLOBAL_LIST).concatinate_json