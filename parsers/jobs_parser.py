from locator.jobs_locators import JobsLocators


class JobsParser:

    def __init__(self, parent):
        self.parent = parent

    def __repr__(self):
        return f'Job title is {self.title}'

    @property
    def title(self):
        locator = JobsLocators.JOB_TITLE
        return self.parent.find_element_by_css_selector(locator).text

