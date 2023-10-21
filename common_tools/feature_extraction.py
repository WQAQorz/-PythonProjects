import os
import logging

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import scipy.signal as signal
from scipy.fftpack import fft

import matplot_tools


class FeatureExtractor:
    @staticmethod
    def set_log_format():
        pass

    def __init__(self):
        self.target_path = ""
        self.data = np.array([])
        self.data_processed = np.array([])
        self.set_log_format()

    def set_target_file(self, file: str, attr: str) -> bool:
        df = pd.read_csv(file)
        self.data = df[attr]
        return True

    def set_target_path(self, path) -> bool:
        """"添加一个文件夹，自动解析里面的所有数据"""
        if not os.path.exists(path):
            logging.info("target_path不存在")
            return False

        self.target_path = path

    def median_filter(self, win_size: int, ax1):
        self.data_processed = signal.medfilt(self.data, win_size)
        ax1.plot(self.data_processed)


if __name__ == "__main__":
    pass
