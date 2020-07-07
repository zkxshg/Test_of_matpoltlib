# 1 引入工具包
import matplotlib.pyplot as plt
import matplotlib.finance as mpf
import numpy as np
import pandas as pd
from matplotlib.pylab import date2num

# 2 删除空行
data=pd.read_csv('Stock.csv',usecols=['date','open','close','high','low','volume'])
data[data['volume']==0]=np.nan
data=data.dropna()

# 3 按时间升序排列并转换日期格式
data.sort_values(by='date',ascending=True,inplace=True)
data.date=pd.to_datetime(data.date)
data.date=data.date.apply(lambda x:date2num(x))

# 4 重新排列变量并转为矩阵
data=data[['date','open','close','high','low','volume']]
data_mat=data.as_matrix()

# 5 绘制K线图
fig,ax=plt.subplots(figsize=(1200/72,480/72))
fig.subplots_adjust(bottom=0.1)
mpf.candlestick_ochl(ax,data_mat,colordown='#53c156',
colorup='#ff1717',width=0.3,alpha=1)
ax.grid(True)
ax.xaxis_date()
plt.show()
