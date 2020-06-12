class CleanValues:

    def __init__(self, text_to_clean):
        self.text_to_clean = text_to_clean

    @property
    def replace_cahrs(self):
        result = self.text_to_clean.replace("\n"," -- ")
        result = result.replace(","," ")
        result = result.replace("<br>", " ---")
        return result


