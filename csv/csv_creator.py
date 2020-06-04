from global1.global_var import GlobalVar


class CsvCreator:
    def __init__(self, job_content):
        self.job_content = job_content
        self.job_content_list = []

    @property
    def concatinate_json(self):
        self.job_content_list.append(self.job_content)
        GlobalVar.GLOBAL_LIST.append(self.job_content_list)
        # print(GlobalVar.GLOBAL_LIST)
        return GlobalVar.GLOBAL_LIST







