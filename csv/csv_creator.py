class CsvCreator:
    def __init__(self, list_of_jobs):
        self.list_of_jobs = list_of_jobs

    @property
    def concatinate_json(self):
        print(__name__)
        with open('csv.csv', 'w', encoding="utf8") as f:
            for dict in self.list_of_jobs:
                f.write(f'\n')
                for key in dict:
                    f.write(f'{dict[key]},')