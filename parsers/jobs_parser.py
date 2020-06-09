from locator.jobs_locators import JobsLocators
from helper.append_values import AppendValues
from global1.global_var import GlobalVar
import json


class JobsParser:

    def __init__(self, parent):
        self.parent = parent
        self.result = {}
        self.data_page = {}
        self.all_data = {}

    # def __str__(self):
    #     string = self.join_data_single_page
    #     string1 = json.dumps(string)
    #     return string1

    def __repr__(self):
        return f'{self.join_data_single_page}'
        # return self.__str__()


    @property
    def join_data_single_page(self):
        title = self.title
        date = self.date
        description = self.description
        bottom_section = self.bottom_section
        # job_requirements = self.job_requirements
        # data_page = {**title, **date, **description, **job_requirements, **bottom_section}
        self.data_page = {**title, **date, **description, **bottom_section}
        # data_page = json.dumps(data_page, ensure_ascii=False).encode('utf8')
        GlobalVar.GLOBAL_LIST.append(self.data_page)
        # print(test)
        return self.data_page

    @property
    def title(self):
        locator = JobsLocators.JOB_TITLE
        self.result["Title"] = self.parent.find_element_by_css_selector(locator).text
        return self.result

    @property
    def content(self):
        locator = JobsLocators.ALL_SECTION
        self.result["Content"] = self.parent.find_element_by_css_selector(locator).text
        return self.result

    @property
    def date(self):
        locator = JobsLocators.JOB_DATE
        self.result["Date"] = self.parent.find_element_by_css_selector(locator).text
        return self.result

    @property
    def description(self):
        locator = JobsLocators.TOP_SECTION
        self.result["Description"] = self.parent.find_element_by_css_selector(locator).text
        return self.result

    # @property
    # def job_requirements(self):
    #     locator = JobsLocators.JOB_REQUIREMENTS
    #     requirements = self.parent.find_element_by_css_selector(locator)
    #     requirements = requirements.get_attribute("innerHTML")
    #     requirements = requirements.replace("<br>", " ---")
    #     self.result["Requirements"] = requirements
    #     return self.result

    @property
    def bottom_section(self):
        locator = JobsLocators.ADDITIONAL_DETAILS
        element_list = self.parent.find_elements_by_css_selector(locator)
        content_list = []
        labels_list = []
        for outer_element in element_list:
             inner_element = outer_element.find_elements_by_css_selector('span.fieldText')
             labels = outer_element.find_elements_by_css_selector('span.fieldTitle')
             for content in inner_element:
                content_list.append(content.get_attribute("innerHTML"))
             for label in labels:
                labels_list.append(label.get_attribute("innerHTML"))
        result = dict(zip(labels_list, content_list))
        return result