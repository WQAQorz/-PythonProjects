import os
import shutil
import logging
from enum import Enum
import pandas as pd


class ParseMode(Enum):
    LOAD = 0
    REFRESH = 1


class DataManager:
    def __init__(self):
        self.target_path = ""
        self.data_list = []
        self.df = pd.DataFrame()
        self.df_selected = pd.DataFrame()
        self.configs = {
            "save_filename": "data_manager_attrs.xlsx",
            "selected_filename": "data_selected.xlsx"
        }
        self._read_config()
        log_format = "%(asctime)s %(levelname)s - %(message)s"
        date_format = "%Y-%m-%d %H:%M:%S"
        logging.basicConfig(
            filemode="data_manager.log",
            level=logging.INFO,
            format=log_format,
            datefmt=date_format
        )

    def set_target_path(self, path) -> bool:
        """"添加一个文件夹，自动解析里面的所有数据"""
        if not os.path.exists(path):
            logging.info("target_path不存在")
            return False

        self.target_path = path

    def select_by_attr(self, attrs) -> bool:
        pass

    def add_attr(self, attr):
        pass

    def del_attr(self, attr: str) -> bool:
        pass

    def confirm_recreate_data(self, new_path: str) -> bool:
        pass

    def _read_config(self):
        filename = os.path.join(self.target_path, self.configs["save_filename"])
        if not os.path.exists(filename):
            return False

        self.df = pd.read_excel(filename, sheet_name=0, index_col=0)
        self._parse_path(mode=ParseMode.REFRESH)
        return True

    def _write_config(self) -> bool:
        pass

    def _parse_path(self, mode=ParseMode.LOAD) -> bool:
        pass


if __name__ == "__main__":
    dm = DataManager()
    dm.set_target_path("")

    dm.add_attr("xxx")
    pass
