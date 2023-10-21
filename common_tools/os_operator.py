import os


class OsOperator:
    def __init__(self, target_path=""):
        self.target_path = target_path

    def find_file(self, keyword, suffix=".txt"):
        files = os.listdir(self.target_path)

        res = []
        for item in files:
            if item.endswith(suffix) and keyword in item:
                res.append(item)

        return res
