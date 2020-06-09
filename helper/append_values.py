from global1.global_var import GlobalVar


class AppendValues:

    def __init__(self, single_page):
        self.single_page = single_page
        # self.all_result = {}

    def __repr__(self):
        return f'{self.add_values}'
        # return self.__str__()

    @property
    def add_values(self):
        GlobalVar.GLOBAL_LIST.append(self.single_page)
        print("GlobalVar.GLOBAL_LIST")
        return GlobalVar.GLOBAL_LIST


