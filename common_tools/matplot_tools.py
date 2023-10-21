from dataclasses import dataclass

import matplotlib.pyplot as plt
from matplotlib.pyplot import MultipleLocator

plt.rcParams["font.sans-serif"] = ["Microsoft YaHei"]  # 微软雅黑显示中文
plt.rcParams["axes.unicode_minus"] = False  # 正常显示负号


@dataclass
class FigParameters:
    # 基础参数
    fig_size: list = ()
    fig_dpi: int = 100
    major_locator: list = ()
    lim_x: list = ()
    lim_y: list = ()
    axis_name: list = ()
    axis_type: str = "auto"
    is_grid: bool = True
    # 3d 图像参数
    lim_z: list = ()
    axis_view_angle: list = (15, 45)
    # 卷轴图像参数
    slices: int = 2  # 切片数量
    width: int = 6  # 单个图像高度
    height: int = 3  # 单个图像高度


class FigureDecorator:
    def __init__(self):
        self.fig_size = [8, 6]
        self.fig_dpi = 100
        self.major_locator = []
        self.lim_x = []
        self.lim_y = []
        self.axis_name = ["x轴", "y轴"]
        self.axis_type = "auto"
        self.is_grid = True

    def set_config(self, paras: FigParameters):
        if paras.fig_size:
            self.fig_size = paras.fig_size
        if paras.fig_dpi:
            self.fig_dpi = paras.fig_dpi
        if paras.major_locator:
            self.major_locator = paras.major_locator
        if paras.lim_x:
            self.lim_x = paras.lim_x
        if paras.lim_y:
            self.lim_y = paras.lim_y
        if paras.axis_name:
            self.axis_name = paras.axis_name
        if paras.is_grid is not None:
            self.is_grid = paras.is_grid
        if paras.axis_type is not None:
            self.axis_type = paras.axis_type


class FigureDecorator2D(FigureDecorator):
    def __init__(self):
        super().__init__()

    def use_basic_format(self):
        """设置二维图像的默认展示格式"""
        plt.figure(figsize=self.fig_size, dpi=self.fig_dpi)
        ax = plt.gca()
        if len(self.major_locator) == 2:  # x和 y 的等刻度间隔
            x_major_locator = MultipleLocator(self.major_locator[0])
            y_major_locator = MultipleLocator(self.major_locator[1])
            ax.xaxis.set_major_locator(x_major_locator)
            ax.yaxis.set_major_locator(y_major_locator)
        if self.lim_x:
            ax.set_xlim(xmin=self.lim_x[0], xmax=self.lim_x[1])
        if self.lim_y:
            ax.set_ylim(ymin=self.lim_y[0], ymax=self.lim_y[1])
        if len(self.axis_name) == 2:
            ax.set_xlabel(self.axis_name[0])
            ax.set_ylabel(self.axis_name[1])
        if self.axis_type and not (self.lim_x or self.lim_y):
            plt.axis(self.axis_type)
        if self.is_grid:
            plt.grid()
        return ax


class FigureDecorator3D(FigureDecorator):
    def __init__(self):
        super().__init__()
        self.lim_z = []
        self.axis_name = ["x轴", "y轴", "z轴"]
        self.axis_view_angle = [15, 45]

    def set_config(self, paras: FigParameters):
        super().set_config(paras)
        if paras.lim_z:
            self.lim_z = paras.lim_z
        if paras.axis_view_angle:
            self.axis_view_angle = paras.axis_view_angle

    def use_basic_format(self):
        """设置三维图像的默认展示格式"""
        plt.figure(figsize=self.fig_size, dpi=self.fig_dpi)
        ax = plt.axes(projection="3d")
        if len(self.major_locator) == 3:
            x_major_locator = MultipleLocator(self.major_locator[0])
            y_major_locator = MultipleLocator(self.major_locator[1])
            z_major_locator = MultipleLocator(self.major_locator[2])
            ax.xaxis.set_major_locator(x_major_locator)
            ax.yaxis.set_major_locator(y_major_locator)
            ax.zaxis.set_major_locator(z_major_locator)

        if len(self.major_locator) == 3:
            x_major_locator = MultipleLocator(self.major_locator[0])
            y_major_locator = MultipleLocator(self.major_locator[1])
            z_major_locator = MultipleLocator(self.major_locator[2])
            ax.xaxis.set_major_locator(x_major_locator)
            ax.yaxis.set_major_locator(y_major_locator)
            ax.zaxis.set_major_locator(z_major_locator)
        if self.lim_x:
            ax.set_xlim(xmin=self.lim_x[0], xmax=self.lim_x[1])
        if self.lim_y:
            ax.set_ylim(ymin=self.lim_y[0], ymax=self.lim_y[1])
        if self.lim_z:
            ax.set_zlim(zmin=self.lim_z[0], zmax=self.lim_z[1])
        if len(self.axis_name) == 3:
            ax.set_xlabel(self.axis_name[0])
            ax.set_ylabel(self.axis_name[1])
            ax.set_zlabel(self.axis_name[2])
        if self.axis_type and not (self.lim_x or self.lim_y or self.lim_z):
            plt.axis(self.axis_type)
        if self.is_grid:
            plt.grid()

        ax.view_init(self.axis_view_angle[0], self.axis_view_angle[1])
        ax.set_box_aspect((1, 1, 1))
        return ax


class FigureDecoratorReel(FigureDecorator):
    def __init__(self):
        super().__init__()
        self.slices = 2  # 切片数量
        self.width = 6  # 单个图像高度
        self.height = 3  # 单个图像高度

    def set_config(self, paras: FigParameters):
        super().set_config(paras)
        if paras.slices:
            self.slices = paras.slices
        if paras.width:
            self.width = paras.width
        if paras.height:
            self.height = paras.height

    def use_basic_format(self):
        """设置二维卷轴图像的默认展示格式"""
        plt.figure(figsize=(self.width, self.slices * self.height), dpi=self.fig_dpi)
        plt.subplots_adjust(wspace=self.width / 10, hspace=self.height / 8)  # 调整子图间距
        ax_group = []
        for i in range(self.slices):
            plt.subplot(self.slices, 1, i + 1)
            ax = plt.gca()

            if len(self.major_locator) == 2:  # x 和 y 的等刻度间隔
                x_major_locator = MultipleLocator(self.major_locator[0])
                y_major_locator = MultipleLocator(self.major_locator[1])
                ax.xaxis.set_major_locator(x_major_locator)
                ax.yaxis.set_major_locator(y_major_locator)
            if self.lim_x:
                ax.set_xlim(xmin=self.lim_x[0], xmax=self.lim_x[1])
            if self.lim_y:
                ax.set_ylim(ymin=self.lim_y[0], ymax=self.lim_y[1])
            if len(self.axis_name) == 2:
                ax.set_xlabel(self.axis_name[0])
                ax.set_ylabel(self.axis_name[1])
            if self.axis_type and not (self.lim_x or self.lim_y):
                plt.axis(self.axis_type)
            if self.is_grid:
                plt.grid()

            ax_group.append(ax)
        return ax_group
