# 导入工具包 
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.legend import Legend

# 定义要绘制的数据
x = np.linspace(0, 10, 1000)

# 设置用作对比的子图
fig, ax = plt.subplots()

# 建立一个空列表用来储存之后建立的四种折线图实例
lines = []

# 建立了一个列表来存放四种折线图的不同线型
styles = ['-', '--', '-.', ':']

# 执行函数绘制四种不同线型的折线图
for i in range(4):
	lines += ax.plot(x, np.sin(x - i * np.pi / 2),styles[i], color='black')

# 使x轴和y轴的刻度相等	
ax.axis('equal')

# 设置第一个图例要显示的线条和标签
ax.legend(lines[:2], ['line A', 'line B'], loc='upper right', frameon=False)

# 设置第二个图例要显示的线条和标签
leg = Legend(ax, lines[2:], ['line C', 'line D'],loc='lower right', frameon=False)
ax.add_artist(leg)

plt.savefig('legend_plot.png', dpi=600, bbox_inches='tight')  # 保存图像
plt.show()  # 显示图像
