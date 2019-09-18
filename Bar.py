import matplotlib.pyplot as plt	# 导入工具包

# 可以在这里定义要绘制的数据
customers = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO']  # 设置数据名
customers_index = range(len(customers))
sale_amounts = [127, 90, 201, 111, 232]  # 设置数据的值

# 执行函数绘制条形图
fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)
# x表示x轴标签；y表示y轴赋值；a表示布局，这里为中心’center’；c为直方颜色，这里选择暗蓝色。
ax1.bar(customers_index, sale_amounts,align='center', color='darkblue')

# 在这里设置图像的元素
# 设置x轴和y轴刻度的位置
ax1.xaxis.set_ticks_position('bottom')
ax1.yaxis.set_ticks_position('left')
plt.xticks(customers_index, customers, rotation=0, fontsize='small')

# 为x轴和y轴加上标签
plt.xlabel('Customer Name')
plt.ylabel('Sale Amount')

# 为条形图添加标题
plt.title('Sale Amount per Customer')

plt.savefig('bar_plot.png', dpi=400, bbox_inches='tight')  # 保存图像
plt.show()  # 显示图像
