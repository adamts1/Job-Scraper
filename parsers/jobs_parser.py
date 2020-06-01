from locator.jobs_locators import JobsLocators


class JobsParser:

    def __init__(self, parent):
        self.parent = parent
        self.result = {}


    def __repr__(self):
        return f'aa:  {self.top_section}'
        # return f'Job title:  {self.title} --  Job date:  {self.date} -- Content: {self.top_section}'

    @property
    def title(self):
        locator = JobsLocators.JOB_TITLE
        return self.parent.find_element_by_css_selector(locator).text

    @property
    def content(self):
        locator = JobsLocators.ALL_SECTION
        return self.parent.find_element_by_css_selector(locator).text

    @property
    def date(self):
        locator = JobsLocators.JOB_DATE
        return self.parent.find_element_by_css_selector(locator).text

    @property
    def top_section(self):
        locator = JobsLocators.TOP_SECTION
        return self.parent.find_element_by_css_selector(locator).text

    @property
    def top_section(self):
        locator = JobsLocators.ADDITIONAL_DETAILS
        element_list = self.parent.find_elements_by_css_selector(locator)
        content_list = []
        labels_list = []
        for outer_elemet in element_list:
             inner_elemet = outer_elemet.find_elements_by_css_selector('span.fieldText')
             labels = outer_elemet.find_elements_by_css_selector('span.fieldTitle')
             for content in inner_elemet:
                content_list.append(content.get_attribute("innerHTML"))
             for label in labels:
                labels_list.append(label.get_attribute("innerHTML"))

        result = dict(zip(labels_list, content_list))

        return result


