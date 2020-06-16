from global1.global_var import GlobalVar
import app
import tkinter as tk
from tkinter import ttk


def combine_funcs(*funcs):
    def combined_func(*args, **kwargs):
        for f in funcs:
            f(*args, **kwargs)
    return combined_func

def quit():
    root.destroy()

root = tk.Tk()
root.title("Job Scraper")

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

greet_button = ttk.Button(root, text="Search", command=combine_funcs(app.app_retry, quit)).pack(side="bottom", fill="both", expand=True, padx=(10))
root.mainloop()


