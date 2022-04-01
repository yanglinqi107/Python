"""
小试牛刀-微信公众平台js算法逆向
· js调试工具
	· 发条js调试工具
· PyExecJs
	· 实现使用python执行js代码
	· 环境安装：
		1.nodejs开发环境
		2.pip install PyExecJs
· js算法改写初探
	· 打断点
	· 代码调试时，如果发现了相关变量的缺失，一般给其定义成空字典即可。
"""
# url = 'https://mp.weixin.qq.com/'

import execjs 
# 1.实例化一个node对象
node = execjs.get()

# 2.js源文件编译
ctx = node.compile(open('.\\JS\\weixin.js',encoding='utf-8').read())

# 3.执行js函数
funcName = 'getPwd("{0}")'.format('123456')
pwd = ctx.eval(funcName)
print(pwd)


