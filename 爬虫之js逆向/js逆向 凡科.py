# - url = https://i.fkw.com/

# - 注意：如果需要逆向的js函数时出现在一个闭包中，那么直接将闭包的整个代码块拷贝出进行调试即可。

import execjs
node = execjs.get()
ctx = node.compile(open(r'.\JS\fanke.js',encoding='utf-8').read())
funcName = "md5('{0}')".format('123456')
pwd = ctx.eval(funcName)
print(pwd)

