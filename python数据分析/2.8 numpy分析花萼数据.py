import numpy as np

arr = np.loadtxt('iris_sepal_length.csv')
arr = np.unique(arr)

print('花萼长度的最大值是：{:.2f}'.format(np.max(arr)))
print('花萼长度的最小值是：{:.2f}'.format(np.min(arr)))
print('花萼长度的均值是：{:.2f}'.format(np.mean(arr)))
print('花萼长度的方差是：{:.2f}'.format(np.var(arr)))
print('花萼长度的标准差是：{:.2f}'.format(np.std(arr, ddof=1)))