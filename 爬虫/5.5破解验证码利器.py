# 1.手写图像识别
# 2.选择互联网上成熟的验证码破解工具    超级鹰  位置在D:\Program Files\Python38\Lib\site-packages
import time
from selenium.webdriver import Chrome
from chaojiying_Python.chaojiying import Chaojiying_Client
web = Chrome()
web.get('https://www.chaojiying.com/user/login/')
# 处理验证码
img = web.find_element_by_xpath('/html/body/div[3]/div/div[3]/div[1]/form/div/img').screenshot_as_png
chaojiying = Chaojiying_Client('', '', '')		
# print(chaojiying.PostPic(img, 1902))		
dic = chaojiying.PostPic(img, 1902)
verify_code = dic['pic_str']   

# 输入用户名，密码，验证码
web.find_element_by_xpath('/html/body/div[3]/div/div[3]/div[1]/form/p[1]/input').send_keys('')
web.find_element_by_xpath('/html/body/div[3]/div/div[3]/div[1]/form/p[2]/input').send_keys('')
web.find_element_by_xpath('/html/body/div[3]/div/div[3]/div[1]/form/p[3]/input').send_keys(verify_code)
time.sleep(5)
#点击登录
web.find_element_by_xpath('/html/body/div[3]/div/div[3]/div[1]/form/p[4]/input').click()