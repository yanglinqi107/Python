'''

import numpy as np
import scipy as sp

# 均值实现

U = [[1, 2, 3, 4, 5, 6], [3, 4, 5, 6, 7, 8]]

# 全部元素求均值
print(np.mean(U))
# 结果输出：
# 4.5

# 按列求均值，0代表列向量
print(np.mean(U, 0))
# 结果输出：
# [2. 3. 4. 5. 6. 7.]

# 按行求均值，1代表行向量
print(np.mean(U, 1))
# 结果输出：
# [3.5 5.5]

'''

# 二项分布的实现
'''
from scipy.stats import binom, norm, beta, expon
import numpy as np
import matplotlib.pyplot as plt

# n,p对应二项式公式中的事件成功次数及其概率
binom_sim = binom.rvs(n=10, p=0.3, size=10000)
print('Data:', binom_sim)
print('Mean:%g' % np.mean(binom_sim))
print('SD:%g' % np.std(binom_sim, ddof=1))
# 生成直方图，x指定每个bin(箱子)分布的数据，对应x轴，bins是总共有几条条状图，
# normed值密度，也就是每个条状图的占比比例，默认为1
plt.hist(binom_sim, bins=10, density=True)
plt.xlabel('x')
plt.ylabel('density')
plt.show()
'''

# 图像加噪声
from numpy import *
from scipy import *
import numpy as np
import cv2

srcImage = cv2.imread(r'.\res\lena.png')
print(srcImage.shape)  # 打印图像size
cv2.namedWindow('Original image')  # 图像显示窗口命令
cv2.imshow('Original image', srcImage)  # 显示图像
k = cv2.waitKey(0)
# 灰度处理原始图片
grayImage = cv2.cvtColor(srcImage, cv2.COLOR_BGR2GRAY)  # 灰度变换
print(grayImage.shape)
cv2.imshow('grayimage', grayImage)
k = cv2.waitKey(0)
# 加入高斯噪声(均值mean,方差var,比例percent)
image = np.array(grayImage / 255, dtype=float)
percent = 0.01  # 图像加入噪声比例
num = int(percent * image.shape[0] * image.shape[1])

for i in range(num):
    temp1 = np.random.randint(image.shape[0])
    temp2 = np.random.randint(image.shape[1])

    mean = 0
    var = 0.04
    noise = np.random.normal(mean, var**0.5, 1)
    image[temp1][temp2] += noise
out = image

if out.min() < 0:
    low_clip = -1
else:
    low_clip = 0
out = np.clip(out, low_clip, 1)
gasuss_image = np.uint8(out * 255)
print(gasuss_image.shape)
cv2.imshow('gasuss_image', gasuss_image)
k = cv2.waitKey(0)

# 加入泊松噪声(泊松参数scale,比例percent)
from scipy.stats import expon

image = np.array(grayImage, dtype=float)
percent = 0.001  # 图像加入噪声比例
num = int(percent * image.shape[0] * image.shape[1])
for i in range(num):
    temp1 = np.random.randint(image.shape[0])
    temp2 = np.random.randint(image.shape[1])
    scale = 150
    noise = np.random.poisson(scale, 1)
    image[temp1][temp2] += noise

out = image
if out.min() < 0:
    low_clip = -1
else:
    low_clip = 0
out = np.clip(out, low_clip, 255)
expon_image = np.uint8(out)
print(expon_image.shape)
cv2.imshow('expon.image', expon_image)
k = cv2.waitKey(0)