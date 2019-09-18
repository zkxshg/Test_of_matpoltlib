# 导入工具包 
import numpy as np
import matplotlib.pyplot as plt

# 设置绘图风格
plt.style.use('ggplot')

# 导入要绘制的数据
x1 = np.loadtxt("NBA.csv",delimiter=",", skiprows=1, usecols=4)
x2 = np.loadtxt("NBA.csv",delimiter=",", skiprows=1, usecols=7)
fig = plt.figure()

# 执行函数绘制直方图
ax1 = fig.add_subplot(1,1,1)
ax1.hist(x1, bins=50, normed=False, color='darkgreen')
ax1.hist(x2, bins=50, normed=False, color='orange', alpha=0.5)

# 设置x轴和y轴刻度的位置
ax1.xaxis.set_ticks_position('bottom')
ax1.yaxis.set_ticks_position('left')

# 为x轴和y轴加上标签
plt.xlabel('Team`s points/FGA')
plt.ylabel('Number of Values in Bin')

# 添加标题
fig.suptitle('NBA team`s PTS vs FGA', fontsize=14, fontweight='bold')

plt.savefig('NBA_hist.png', dpi=200, bbox_inches='tight')  # 保存图像
plt.show()  # 显示图像
