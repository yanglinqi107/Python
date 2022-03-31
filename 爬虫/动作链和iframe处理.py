from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import ActionChains
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains

option = Options()
option.binary_location = r'D:\Program Files\Google\Chrome\Application\chrome.exe'
bro = webdriver.Chrome(options=option)
bro.get('https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable')
# 如果定位的标签是在iframe中，则必须通过如下操作进行标签定位
bro.switch_to.frame('iframeResult') # 切换浏览器标签定位的作用域
div = bro.find_element_by_id('draggable')

# 动作链
action = ActionChains(bro)
# 点击长按指定的标签
action.click_and_hold(div)
for i in range(5):
    action.move_by_offset(17, 0).perform()
    sleep(0.3)
# 释放动作链
action.release()

print(div)
bro.quit()