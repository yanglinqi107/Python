import re

# #findall：匹配字符串中所有符合正则的内容，返回列表
# lst = re.findall(r'\d+', '我的电话号码是：10086，我女朋友的电话号码是：10010')
# print(lst)

# #finditer：匹配字符串中所有內容返回迭代器，迭代器中拿到內容要用.group()
# iter = re.finditer(r'\d+', '我的电话号码是：10086，我女朋友的电话号码是：10010')
# print(iter)
# for i in iter:
#     print(i.group())

# #search：找到一个结果就返回，返回对象是match，拿到內容要用.group()
# s = re.search(r'\d+', '我的电话号码是：10086，我女朋友的电话号码是：10010')
# print(s)
# print(s.group())

# #match：从头开始匹配
# m = re.match(r'\d+', '10086，我女朋友的电话号码是：10010')
# print(m)
# print(m.group())

# #预加载正则表达式
# obj = re.compile(r'\d+')
# result = obj.finditer('我的电话号码是：10086，我女朋友的电话号码是：10010')
# for i in result:
#     print(i.group( ))

s = """
<div class='a'><span id='1'>杨洋</span></div>
<div class='c'><span id='2'>端口i</span></div>
<div class='w'><span id='3'>地</span></div>
<div class='d'><span id='4'>肯德基覅哦</span></div>
<div class='v'><span id='5'>点击</span></div>
"""

# obj = re.compile(r"<div class='.*?'><span id='\d+'>.*?</span></div>",re.S)  #re.S让.能匹配换行符
# result = obj.finditer(s)
# for i in result:
#     print(i.group())
"""结果如下
<div class='a'><span id='1'>杨洋</span></div>
<div class='c'><span id='2'>端口i</span></div>
<div class='w'><span id='3'>地</span></div>
<div class='d'><span id='4'>肯德基覅哦</span></div>
<div class='v'><span id='5'>点击</span></div>
"""
#(?P<名字>正则)单独从正则匹配的内容中进一步提取内容
obj = re.compile(r"<div class='.*?'><span id='(?P<id>\d+)'>(?P<text>.*?)</span></div>",re.S)  #获取想要的精确内容
result = obj.finditer(s)
for i in result:
    print(i.group("id"))
    print(i.group("text"))

# 注意注意
str = '"pageLoadUrl:":"kdsfjodfoaoifjksl","pageLoadUrl:":"dklsfdoiefk","pageLoadUrl:":"dkfodfl0.pngdksof","pageLoadUrl:":"dkfodfl0.pngdksof"'
result = re.findall(r'"pageLoadUrl:":"(.*?0.png.*?)"', str, re.S)
print(result)