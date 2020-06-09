import json

from selenium import webdriver
import time
import os, sys

# driver = webdriver.Chrome(
#     'C:/Users/Adam/Main/The Comlete Python course/12_browser_automation/chromedriver_win32/chromedriver.exe')
# driver.get("https://www.drushim.co.il/jobs/cat24/area/1-2-3-4-5-6-7-8-9/?searchterm=python")
# driver.maximize_window()
#
# driver.refresh()
#
# time.sleep(12)
# # while driver.find_elements_by_css_selector('.jobListPageNumberContainer.contentDivider > a')[-1].get_attribute('innerHTML') == "הבא »":
# #     driver.find_elements_by_css_selector('.jobListPageNumberContainer.contentDivider > a')[-1].click()
# #     time.sleep(1)
#
# driver.refresh()
#


json_string = json.dumps("ברי צקלה", ensure_ascii=False).encode('utf8')
print(json_string)
print(json_string.decode())
