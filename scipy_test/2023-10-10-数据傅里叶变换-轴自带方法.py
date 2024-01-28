import numpy as np
from common_tools.matplot_tools import *


# 生成白噪声
num_samples = 100  # 采样点数
samples = np.random.normal(0, 1, size=num_samples)

# 画出时域和频域图像
mt = FigureDecoratorReel()
paras = FigParameters(slices=2)
mt.set_config(paras)
ax_group = mt.use_basic_format()

ax1 = ax_group[0]
ax2 = ax_group[1]
ax1.plot(samples)
ax1.set_title('时域图像')
ax2.magnitude_spectrum(samples, Fs=1, scale='dB')
ax2.set_title('频域图像')
plt.show()
