from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from time import sleep
option = Options()
option.binary_location='D:\Program Files\Google\Chrome\Application\chrome.exe'
bro = webdriver.Chrome(options=option)
bro.get('https://www.taobao.com/')
# 标签定位
search_input = bro.find_element_by_id('q')
# 标签交互
search_input.send_keys('Iphone')
btn = bro.find_element_by_css_selector('.btn-search')
# 执行一组js程序，滚动窗口
bro.execute_script('window.scrollTo(1,document.body.scrollHeight)')
sleep(2)
# 点击按钮
btn.click()

bro.get('https://www.baidu.com')
sleep(2)
# 窗口回退
bro.back()
sleep(2)
# 窗口前进
bro.forward()

sleep(5)
bro.quit()