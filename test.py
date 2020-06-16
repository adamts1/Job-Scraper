from selenium import webdriver
from page.jobs_page import JobsPages
import logging
from csv.csv_creator import CsvCreator
from global1.global_var import GlobalVar


import tkinter as tk
from tkinter import ttk


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
    CsvCreator(GlobalVar.GLOBAL_LIST).concatinate_json
    return status


if __name__ == '__main__':
    root = tk.Tk()
    root.title("Job Scraper")

    # Here we create an instances of the StringVar() class, which is to track the content of widgets
    GlobalVar.AREA = tk.StringVar()
    GlobalVar.CATEGORY = tk.StringVar()
    GlobalVar.KEY_WORD = tk.StringVar()

    search_label = ttk.Label(root, text="Key Word: ").pack(side="left", padx=(0, 10))
    search_entry = ttk.Entry(root, width=15, textvariable=GlobalVar.KEY_WORD).pack(side="left", padx=(0, 10))

    category_label = ttk.Label(root, text="Category: ", width=4).pack(side="left")
    category_entry = ttk.Combobox(root, width=14, values=["כל הקטגוריות", "אבטחת מידע", "אדמיניסטרציה", "אופנה", "אינטרנט", "ביטוח",
                                      "בכירים / ניהול", "בעלי מקצוע", "הדרכה / הוראה", "הייטק-QA", "הייטק-חומרה",
                                      "הייטק-כללי", "הייטק-תוכנה", "הנדסה", "כללי", "כספים", "לוגיסטיקה / שילוח",
                                      "מדעים / ביוטק", "מכירות", "מלונאות / מסעדנות", "משאבי אנוש", "עבודה מהבית",
                                      "עיצוב", "עריכת דין", "פרסום / מדיה", "קמעונאות", "רכב / תחבורה",
                                      "רפואה / בריאות", "שיווק", "שירות לקוחות", "שמירה / אבטחה", "תיירות/ תעופה",
                                      "תעשיה / ייצור"], textvariable=GlobalVar.CATEGORY).pack(side="left")

    area_entry_label = ttk.Label(root, text="Area: ").pack(side="left", padx=(0, 10))
    area_entry = ttk.Combobox(root, width=15, values=["כל האיזורים", "מרכז", "תל אביב", "רמת גן / גבעתיים", "חולון / בת ים",
                                          "ראשון לציון", "פתח תקווה", "אור יהודה / יהוד", "לוד / רמלה", "מודיעין",
                                          "ראש העין", "שרון", "נתניה / אבן יהודה", "רעננה / כפר סבא",
                                          "הרצליה / רמת השרון", "הוד השרון", "חדרה", "שפלה", "אשדוד / גן יבנה",
                                          "רחובות / נס ציונה/ גדרה", "יבנה", "ירושלים", "ירושלים", "בית שמש",
                                          "מעלה אדומים", "צפון", "חיפה", "קריות", "עכו / נהריה", "גליל / גולן", "טבריה",
                                          "עפולה / נצרת", "יוקנעם / רמת ישי"], textvariable=GlobalVar.AREA).pack(side="left")

    greet_button = ttk.Button(root, text="Search", command=start).pack(side="bottom", fill="both", expand=True, padx=(10))

    root.mainloop()
    content = None
    retry = 3
    while content is None and retry != 0:
        content = start()
        retry = retry - 1
    print(content)

CsvCreator(GlobalVar.GLOBAL_LIST).concatinate_json