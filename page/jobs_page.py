from typing import List

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from locator.search_locators import SearchLocators
from locator.jobs_locators import JobsLocators
from parsers.jobs_parser import JobsParser
import time


class JobsPages:
    def __init__(self, browser):
        self.browser = browser
        self.dropdowns = []

    @property
    def jobs(self) -> List[JobsParser]:
        return [
            JobsParser(e)
            for e in self.browser.find_elements_by_css_selector(
                JobsLocators.JOB
            )
        ]

    @property
    def get_main_field(self):
        return self.browser.find_element_by_css_selector(SearchLocators.MAIN_CONTENT)

    @property
    def get_category_field(self):
        dropdowns = self.browser.find_elements_by_class_name(SearchLocators.CATEGORY)
        dropdowns[0].click()

    @property
    def get_area_field(self):
        dropdowns = self.browser.find_elements_by_class_name(SearchLocators.CATEGORY)
        dropdowns[1].click()

    @property
    def get_search_bottun(self):
        self.browser.find_element_by_id(SearchLocators.SEARCH).click()

    def insert_main_field(self, main_keyword: str):
        self.get_main_field.send_keys(main_keyword)

    def insert_category_field(self, category: str):
        self.get_category_field
        category_len = len(self.browser.find_elements_by_xpath("//*[@id=\"body\"]/ul[3]/li"))
        for el in range(1, category_len):
            str_el = str(el)
            option = self.browser.find_element_by_xpath(f"//*[@id=\"body\"]/ul[3]/li[{str_el}]/a").text
            if option == category:
                self.browser.find_element_by_xpath(f"//*[@id=\"body\"]/ul[3]/li[{str_el}]").click()
                break

    def insert_area_field(self, area: str):
        self.get_area_field
        area_len = len(self.browser.find_elements_by_xpath("//*[@id=\"body\"]/ul[4]/li"))
        for el in range(1, area_len):
            str_el = str(el)
            option = self.browser.find_element_by_xpath(f"//*[@id=\"body\"]/ul[4]/li[{str_el}]/a").text
            if option == area:
                self.browser.find_element_by_xpath(f"//*[@id=\"body\"]/ul[4]/li[{str_el}]").click()
                break


    def orchestrator(self, main_keyword: str, category: str, area: str) -> List[JobsParser]:
        self.insert_main_field(main_keyword)
        self.insert_category_field(category)
        self.insert_area_field(area)
        self.get_search_bottun
        time.sleep(5)
        return self.jobs