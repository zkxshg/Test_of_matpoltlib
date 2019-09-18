import matplotlib.pyplot as plt	# 导入工具包 
import numpy as np

x = np.linspace(0, 10, 100)
plt.plot(x, np.sin(x - 0), color='blue')  # 标准颜色名称
plt.plot(x, np.sin(x - 1), color='g')  # 缩写颜色代码（rgbcmyk)
plt.plot(x, np.sin(x - 2), color='0.75')  # 范围在0~1的灰度值
plt.plot(x, np.sin(x - 3), color='#FFDD44')  # 十六进制（RRGGBB，00~FF）
plt.plot(x, np.sin(x - 4), color=(1.0,0.2,0.3))  # RGB元组，范围在0~1
plt.plot(x, np.sin(x - 5), color='chartreuse')  # HTML颜色名称
# 修改线型
plt.plot(x, x + 0, linestyle='solid')
plt.plot(x, x + 1, linestyle='dashed')
plt.plot(x, x + 2, linestyle='dashdot')
plt.plot(x, x + 3, linestyle='dotted')
# 简写形式
plt.plot(x, x + 4, linestyle='-')  # 实线
plt.plot(x, x + 5, linestyle='--')  # 虚线
plt.plot(x, x + 6, linestyle='-.')  # 点划线
plt.plot(x, x + 7, linestyle=':')  # 实点线
plt.plot(x, x + 0, '-g')  # 绿色实线
plt.plot(x, x + 1, '--c')  # 青色虚线
plt.plot(x, x + 2, '-.k')  # 黑色点划线
plt.plot(x, x + 3, ':r')  # 红色实点线
plt.show()
