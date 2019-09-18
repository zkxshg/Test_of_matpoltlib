import matplotlib.pyplot as plt	# 导入工具包
import numpy as np

N=500
normal=np.random.normal(loc=0.0,scale=1.0,size=N)
lognormal=np.random.lognormal(mean=0.0,sigma=1.0,size=N)
index_value=np.random.random_integers(low=0,high=N-1,size=N)
normal_sample=normal[index_value]
lognormal_sample=lognormal[index_value]
box_plot_data=[normal,normal_sample,lognormal,lognormal_sample]
box_labels=['normal','normal_sample','lognormal','lognormal_sample']
plt.boxplot(box_plot_data,notch=False,sym='.',vert=True,whis=1.5,showmeans=True,labels=box_labels)
plt.show()  # 显示图像
