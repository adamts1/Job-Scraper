from locator.jobs_locators import JobsLocators
from helper.clean_values import CleanValues
from global1.global_var import GlobalVar


class JobsParser:

    def __init__(self, parent):
        self.parent = parent
        self.result = {}
        self.data_page = {}
        self.all_data = {}

    def __repr__(self):
        return f'{self.join_data_single_page}'

    @property
    def join_data_single_page(self):
        title = self.title
        date = self.date
        description = self.description
        job_requirements = self.job_requirements
        bottom_section = self.bottom_section
        self.data_page = {**title, **date, **description, **job_requirements, **bottom_section}
        GlobalVar.GLOBAL_LIST.append(self.data_page)
        return self.data_page

    @property
    def title(self):
        locator = JobsLocators.JOB_TITLE
        self.result["Title"] = CleanValues(self.parent.find_element_by_css_selector(locator).text).replace_cahrs
        return self.result

    @property
    def date(self):
        locator = JobsLocators.JOB_DATE
        self.result["Date"] = CleanValues(self.parent.find_element_by_css_selector(locator).text).replace_cahrs
        return self.result

    @property
    def description(self):
        locator = JobsLocators.TOP_SECTION
        self.result["Description"] = CleanValues(self.parent.find_element_by_css_selector(locator).text).replace_cahrs
        return self.result

    @property
    def job_requirements(self):
        try:
            locator = JobsLocators.JOB_REQUIREMENTS
            requirements = self.parent.find_element_by_css_selector(locator)
            requirements = requirements.get_attribute("innerHTML")
            self.result["Requirements"] = CleanValues(requirements).replace_cahrs
        except:
            self.result = {}
        return self.result

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
                content_list.append(CleanValues(content.get_attribute("innerHTML")).replace_cahrs)
             for label in labels:
                labels_list.append(label.get_attribute("innerHTML"))
        result = dict(zip(labels_list, content_list))
        return result