from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options

# 改变了谷歌浏览器的位置，需加上这几行
option = Options()
option.binary_location=r'D:\Program Files\Google\Chrome\Application\chrome.exe'

# 1.创建一个浏览器对象
driver = Chrome(options=option)

# 2.打开一个网址
driver.get("https://www.baidu.com")
print(driver.title)


# from selenium import webdriver
# from selenium.webdriver.chrome import options

# option=options.Options()
# option.binary_location='D:\Program Files\Google\Chrome\Application\chrome.exe'
# # 实例化一个浏览器对象，executable_path驱动的路径，若添加至环境变量无需
# bro = webdriver.Chrome(executable_path='E:\chromedriver.exe',options = option)
# bro.get('https://www.baidu.com')
# # 关闭浏览器
# bro.quit()

