from global1.global_var import GlobalVar
import tkinter as tk
from tkinter import ttk


def greet():
    # The get() method is used to fetch the value of a StringVar() instance.
    # If user_name is empty, print Hello, World!
    print(f"Hello, {GlobalVar.CATEGORY.get()}, {GlobalVar.AREA.get()} == {GlobalVar.KEY_WORD.get()}")


root = tk.Tk()
root.title("Job Scraper")

# Here we create an instances of the StringVar() class, which is to track the content of widgets
GlobalVar.AREA = tk.StringVar()
GlobalVar.CATEGORY = tk.StringVar()
GlobalVar.KEY_WORD = tk.StringVar()




search_label = ttk.Label(root, text="Key Word: ").pack(side="left", padx=(0, 10))
search_entry = ttk.Entry(root, width=15, textvariable=GlobalVar.KEY_WORD).pack(side="left", padx=(0, 10))

area_label = ttk.Label(root, text="Area: ", width=4).pack(side="left")
area_entry = ttk.Combobox(root, width=14, values= ["כל הקטגוריות", "אבטחת מידע", "אדמיניסטרציה", "אופנה", "אינטרנט", "ביטוח", "בכירים / ניהול", "בעלי מקצוע", "הדרכה / הוראה", "הייטק-QA", "הייטק-חומרה", "הייטק-כללי", "הייטק-תוכנה", "הנדסה", "כללי", "כספים", "לוגיסטיקה / שילוח", "מדעים / ביוטק", "מכירות", "מלונאות / מסעדנות", "משאבי אנוש", "עבודה מהבית", "עיצוב", "עריכת דין", "פרסום / מדיה", "קמעונאות", "רכב / תחבורה", "רפואה / בריאות", "שיווק", "שירות לקוחות", "שמירה / אבטחה", "תיירות/ תעופה", "תעשיה / ייצור"], textvariable=GlobalVar.AREA ).pack(side="left")
# area_entry.focus()

category_label = ttk.Label(root, text="Category: ").pack(side="left", padx=(0, 10))
category_entry = ttk.Combobox(root, width=15, values=["כל האיזורים", "מרכז", "תל אביב", "רמת גן / גבעתיים", "חולון / בת ים", "ראשון לציון", "פתח תקווה", "אור יהודה / יהוד", "לוד / רמלה", "מודיעין", "ראש העין", "שרון", "נתניה / אבן יהודה", "רעננה / כפר סבא", "הרצליה / רמת השרון", "הוד השרון", "חדרה", "שפלה", "אשדוד / גן יבנה", "רחובות / נס ציונה/ גדרה", "יבנה", "ירושלים", "ירושלים", "בית שמש", "מעלה אדומים", "צפון", "חיפה", "קריות", "עכו / נהריה", "גליל / גולן", "טבריה", "עפולה / נצרת", "יוקנעם / רמת ישי"], textvariable=GlobalVar.CATEGORY ).pack(side="left")




greet_button = ttk.Button(root, text="Search", command=greet).pack(side="bottom", fill="both", expand=True, padx=(10))

root.mainloop()