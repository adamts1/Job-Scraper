import csv


csv_columns = ['No', 'Name', 'Country']
dict_data = [
    {'No': 1, 'Name': 'sss', 'Country': 'I\nndsia'},
    {'No': 2, 'Name': 'Ben', 'Country': 's'},
    {'No': 3, 'Name': 'Shri Ram', 'Country': 'ישראל'},
    {'No': 4, 'Name': 'Smith', 'Country': 'USA'},
    {'No': 5, 'Name': 'Yuva Raj', 'Country': 'India'},  
]

csv_file = 'csv.csv'


def output_to_file(output):
    with open(csv_file, 'w', encoding="utf8") as f:
        # f.write("sss,dd")
        for dict in output:
            f.write(f'\n')
            for key in dict:
                f.write(f'{dict[key]},')
            #f.write(f'{dict["Name"]}, {dict["Country"]}\n')



output_to_file(dict_data)
