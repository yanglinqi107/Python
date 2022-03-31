# import numpy as np

# 矩阵转换
'''
# 生成一个包含整数0-11的向量
x= np.arange(12)
print(x)
# 结果输出：
# [0 1 2 3 4 5 6 6 8 9 10 11]
# 查看数组大小
print(x.shape)
# 结果输出：
# (12,)
# 将x转换成二维矩阵，其中矩阵的第一个维度为1
x=x.reshape(1,12)
print(x)
# 结果输出：
# (12,)
# 查看数组大小
print(x.shape)
# 结果输出：
# （1,12）
# 将x转换为3x4的矩阵
x = x.reshape(3,4)
print(x)
# 结果输出：
# [[ 0  1  2  3]
#  [ 4  5  6  7]
#  [ 8  9 10 11]]
'''

# 转置实现
'''
# 生成3x4的矩阵并转置
A = np.arange(12).reshape(3,4)
print(A)
# 结果输出
# [[ 0  1  2  3]
#  [ 4  5  6  7]
#  [ 8  9 10 11]]

print(A.T)
# 结果输出：
# [[ 0  4  8]
#  [ 1  5  9]
#  [ 2  6 10]
#  [ 3  7 11]]
'''

# 矩阵乘法
'''
A = np.arange(6).reshape(3,2)
B = np.arange(6).reshape(2,3)
print(A)
# 结果输出：
# [[0 1]
#  [2 3]
#  [4 5]]
print(B)
# 结果输出：
# [[0 1 2]
#  [3 4 5]]
# 矩阵相乘
C = np.matmul(A,B)
print(C)
# 结果输出：
# [[ 3  4  5]
#  [ 9 14 19]
#  [15 24 33]]
'''

# 矩阵对应运算
'''
# 创建矩阵
A = np.arange(6).reshape(3,2)
B = np.arange(6,12).reshape(3,2)

# 矩阵相乘
print(A*B)
# 结果输出：
# [[ 0  7]
#  [16 27]
#  [40 55]]

# 矩阵相加
print(A+A)
# 结果输出
# [[ 0  2]
#  [ 4  6]
#  [ 8 10]]
'''

# 逆矩阵实现
'''
A = np.arange(4).reshape(2,2)
print(A)
# 结果输出：
# [[0 1]
#  [2 3]]

# 求逆矩阵
B = np.linalg.inv(A)
print(B)
# 结果输出：
# [[-1.5  0.5]
#  [ 1.   0. ]]
# 验证AB=I_n
print(np.matmul(A,B))
# 结果输出：
# [[1. 0.]
#  [0. 1.]]
'''

# 特征值与特征向量
'''
# 导入相应的库
from scipy.linalg import eig
import numpy as np
import matplotlib.pyplot as plt

# 生成一个2x2的矩阵
A = [[1, 2], [2, 1]]

# 求A的特征值(evals)和特征向量(evecs)
evals, evecs = eig(A)
evecs = evecs[:, 0], evecs[:, 1]
# print(evals, evecs)

# plt.subplots() 返回一个Figure实例flg 和一个AxesSubplot实例ax。
# flg代表整个图像，ax代表坐标轴和画的图，作图：
fig, ax = plt.subplots()
# 让坐标轴经过原点：
for spine in ['left', 'bottom']:  # 让在左下角的坐标轴经过原点
    ax.spines[spine].set_position('zero')
# 画出网格：
ax.grid(alpha=0.4)
# 设置坐标轴的范围
xmin, xmax = -3, 3
ymin, ymax = -3, 3
ax.set(xlim=(xmin, xmax), ylim=(ymin, ymax))
# 画出特征向量，用一个箭头指向要注释的地方，再写上一段画的行为，叫做annotate。
# text是输入内容；xy:箭头指向；xytext:文字所处的位置；arrowprops通过表明箭头的风格或种类：
for v in evecs:
    ax.annotate(text='',
                xy=v,
                xytext=(0, 0),
                arrowprops=dict(facecolor='blue',
                                shrink=0,
                                alpha=0.6,
                                width=0.5))

# 画出特征空间：
x = np.linspace(xmin, xmax, 3)  # 在指定的间隔内返回均匀间隔的数字
for v in evecs:
    a = v[1] / v[0]  # 沿特征向量方向的单位向量
    ax.plot(x, a * x, 'r-', lw=0.4)  # 参数lw表示图像的粗细
plt.show()
'''

# 求行列式
'''
import numpy as np

E = [[1, 2, 3], 
     [4, 5, 6],
     [7, 8, 9]]
print(np.linalg.det(E))
# 结果输出：
# 0.0
'''

# 奇异值分解

'''
import numpy as np
import matplotlib.pyplot as plt

title_1 = ['dad','dad','stock']
title_2 = ['books','books','value','estate']
title_3 = ['books','decomposition']
title_4 = ['stock']
title_5 = ['dad']
title_6 = ['value','singular','decomposition']
title_7 = ['dad',"singular"]
title_8 = ['singular','estate','decomposition']

words = ['books','dad','stock','value','singular','estate','decomposition']
# 设已知8个标题，7个关键字，记录每个关键字出现的次数，得矩阵X，
# X中每一行表示一个标题，每一列表示一个关键字，
# 矩阵中的每个元素表示一个关键字在一个标题中出现的次数
X=np.array([[0,2,1,0,0,0,0],[2,0,0,1,0,1,0],[1,0,0,0,0,0,1],[0,0,1,0,0,0,0],[0,1,0,0,0,0,0],[0,0,0,1,1,0,1],[0,1,0,0,1,0,0],[0,0,0,0,1,1,1]])
# 进行奇异值分解
U,s,Vh = np.linalg.svd(X)
# 输出左奇异矩阵U及其shape:
print('U=',U)
print('U.shape',U.shape)
# 输出结果：
# U= [[-1.87135757e-01 -7.93624528e-01  2.45011855e-01 -2.05404352e-01
#   -7.77156117e-16 -4.95330978e-15 -2.57394431e-01 -4.08248290e-01]
#  [-6.92896814e-01  2.88368077e-01  5.67788037e-01  2.22142537e-01
#    2.54000254e-01  5.20956571e-15 -2.21623012e-02  0.00000000e+00]
#  [-3.53233681e-01  1.22606651e-01  3.49203461e-02 -4.51735990e-01
#   -7.62000762e-01 -1.04191314e-14  2.72513448e-01  5.55111512e-17]
#  [-2.61369658e-02 -1.33189110e-01  7.51079037e-02 -6.44727454e-01
#    5.08000508e-01 -1.58761893e-14  3.68146235e-01  4.08248290e-01]
#  [-8.04993957e-02 -3.30217709e-01  8.49519758e-02  2.19661551e-01
#   -2.54000254e-01  5.29989065e-15 -3.12770333e-01  8.16496581e-01]
#  [-3.95029694e-01  1.56123876e-02 -5.28290830e-01 -6.82340484e-02
#    1.27000127e-01 -7.07106781e-01 -2.09360158e-01  1.38777878e-16]
#  [-2.02089013e-01 -3.80395849e-01 -2.12899198e-01  4.80790894e-01
#    8.88178420e-16  1.15928216e-14  7.33466480e-01  1.66533454e-16]
#  [-3.95029694e-01  1.56123876e-02 -5.28290830e-01 -6.82340484e-02
#    1.27000127e-01  7.07106781e-01 -2.09360158e-01 -2.49800181e-16]]
# U.shape (8, 8)

# 输出奇异矩阵及其shape:
print('s=',s)
print('s.shape',s.shape)
# 结果结果：
# 按每个奇异值——对应一个左奇异向量和一个右奇异向量从大到小排列
# s= [2.85653844 2.63792139 2.06449303 1.14829917 1.         1.
#  0.54848559]
# s.shape (7,)

# 输出右奇异矩阵Vh及其shape:
print('Vh=',Vh)
print('Vh.shape',Vh.shape)
# 输出结果：
# Vh= [[-6.08788345e-01 -2.29949618e-01 -7.46612474e-02 -3.80854846e-01
#   -3.47325416e-01 -3.80854846e-01 -4.00237243e-01]
#  [ 2.65111314e-01 -8.71088358e-01 -3.51342402e-01  1.15234846e-01
#   -1.32365989e-01  1.15234846e-01  5.83153945e-02]
#  [ 5.66965547e-01  1.75382762e-01  1.55059743e-01  1.91316736e-02
#   -6.14911671e-01  1.91316736e-02 -4.94872736e-01]
#  [-6.48865369e-03  2.52237176e-01 -7.40339999e-01  1.34031699e-01
#    2.99854608e-01  1.34031699e-01 -5.12239408e-01]
#  [-2.54000254e-01 -2.54000254e-01  5.08000508e-01  3.81000381e-01
#    2.54000254e-01  3.81000381e-01 -5.08000508e-01]
#  [ 0.00000000e+00  7.25520445e-15 -2.07821168e-14 -7.07106781e-01
#    8.03741866e-15  7.07106781e-01 -1.37929454e-14]
#  [ 4.16034348e-01 -1.71550021e-01  2.01922906e-01 -4.22112199e-01
#    5.73845817e-01 -4.22112199e-01 -2.66564648e-01]]
# Vh.shape (7, 7)

# 规定坐标轴的范围
plt.axis([-0.8,0.8,-0.8,0.8])
# 原每个关键字由1*8的向量表示，先降维成1*2的向量以便进行可视化
for i in range(len(words)):
    plt.text(U[i,0],U[i,1],words[i])
plt.show()
# 图解：将到2维可视化后，我们可以将关键词聚类，如 singular, value和 decomposition
# 三个词距离比较近可以被划分为一组，而 stock和 estate经常同时出现。
# 在得到了词的向量表示后，我们就可以根据选取一种向量距离（例如：欧式距离、曼哈顿距离
# 等）计算的方式来计算词间的相似度从而可以再根据一些策略（例如：词对相似度的和、均值
# 等）得到文章标题之间的相似度；之后我们就可以通过文章标题的相似度来近似表示文章内容
# 的相似度从而完成对文章的聚类。
'''

# 奇异值分解应用-图像压缩
'''
import numpy as np
from pylab import *
import matplotlib.pyplot as plt

# 读取并保存灰度图像
img = imread('res/lena.png')[:,:,0]
plt.gray()

# 画出灰度图
plt.figure(1)
plt.imshow(img) # 负责处理图片不会显示
plt.savefig('./lena_gray')
# plt.show()
# 输出结果


# 读取并打印图像的长宽
m,n = img.shape
print(np.shape(img))
# 输出结果：
# (457, 563)

# 对图像矩阵进行奇异值分解
U,sigma,V = np.linalg.svd(img)
# 打印奇异值大小
print(np.shape(sigma))
# 输出结果
# (457,)

# 将奇异值整理成一个对角矩阵
sigma = resize(sigma,[m,1])*eye(m,n)
# 取前K个奇异值及其奇异向量用于压缩图像
k = 100
# 用前K个奇异值及其奇异向量构造新图像
img1 = np.dot(U[:,0:k],np.dot(sigma[0:k,0:k],V[0:k,:]))
plt.figure(2)
# 打印压缩后的效果图
plt.imshow(img1)
plt.show()
'''

# 线性方程组求解

import numpy as np
from scipy.linalg import solve

a = np.array([[10,2,5],[4,4,2],[2,2,2]])
b = np.array([10,8,5])
x = solve(a,b)
print(x)

# 结果输出：
# [0.25 1.25 1.  ]