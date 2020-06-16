from selenium import webdriver
from page.jobs_page import JobsPages
import logging
from csv.csv_creator import CsvCreator
from global1.global_var import GlobalVar


logging.basicConfig(format='%(asctime)s %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s',
                    datefmt='%d-%m-%Y %H:%M:%S',
                    level=logging.INFO,
                    filename='logs.txt')
logger = logging.getLogger('scraping')


def start():
    driver = webdriver.Chrome(
        'C:/Users/Adam/Main/The Comlete Python course/12_browser_automation/chromedriver_win32/chromedriver.exe')
    driver.get("https://www.drushim.co.il/")
    driver.maximize_window()
    page = JobsPages(driver)
    status = page.orchestrator(GlobalVar.KEY_WORD.get(), GlobalVar.CATEGORY.get(), GlobalVar.AREA.get())
    return status



def app_retry():
    content = None
    retry = 3
    while content is None and retry != 0:
        content = start()
        retry = retry - 1
    print(content)
    CsvCreator(GlobalVar.GLOBAL_LIST).concatinate_json