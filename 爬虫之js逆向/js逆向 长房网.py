# url = 'http://eip.chanfine.com/login.jsp'

import execjs

node = execjs.get()
pwd = '123456'
filepath = '.\\JS\\长房网.js'
ctx = node.compile(open(filepath,encoding='utf-8').read())
funcName = 'getPwd("{0}")'.format(pwd)
password = ctx.eval(funcName)
print(password)
