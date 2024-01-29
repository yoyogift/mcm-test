#拉格朗日
import numpy as np
from scipy.interpolate import lagrange
import matplotlib.pyplot as plt
#设置字体支持中文
plt.rcParams['font.sans-serif']=['SimHei']
#随机生成6个x点，和对应的6个y值
x0 = np.arange(1,7);y0=np.array([16,18,21,17,15,12])
#现在有6个点
p=lagrange(x0,y0)

print('从高次幂到底次幂系数为：',np.round(p,4))#round四舍五入，保留四位小数
#给定输入的x值，1.5&2.6
yh=np.polyval(p,[1.5,2.6])
print('预测值为：',np.round(yh,4))
#散点图，圆滑的曲线，红色
plt.scatter(x0,y0,marker='o',color='r',label='原始数据')
#1~6之间等间距创建100个点
x=np.linspace(1,6,100)

y=np.polyval(p,x)#p是一个多项式，polyval计算多个x用这个多项式计算的y值

plt.plot(x,y,'r-',x0,y0,'bo',label='插值多项式')
plt.legend(loc='best')
plt.savefig('code1.png',dpi=600)
plt.show()
