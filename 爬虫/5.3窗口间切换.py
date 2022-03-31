# from selenium.webdriver import Chrome
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

web = webdriver.Chrome()
web.get("http://lagou.com")
web.find_element_by_xpath('//*[@id="cboxClose"]').click()
time.sleep(1)
web.find_element_by_xpath('//*[@id="search_input"]').send_keys("python", Keys.ENTER)
time.sleep(1)

# web.find_element_by_xpath('//*[@id="s_position_list"]/ul/li[1]/div[1]/div[1]/div[1]/a/h3').click()
# 发生异常: ElementClickInterceptedException
# Message: element click intercepted: Element <h3>...</h3> is not clickable at point (83, 605). Other element would receive the click:
element1 = web.find_element_by_xpath('//*[@id="s_position_list"]/ul/li[1]/div[1]/div[1]/div[1]/a/h3')
web.execute_script("arguments[0].click();",element1)
# 切换窗口
web.switch_to.window(web.window_handles[-1])
time.sleep(1)
# print(web.title)
# print(web.find_element_by_xpath('//*[@id="s_position_list"]/ul/li[1]/div[1]/div[1]/div[1]/a/h3').text)
job_detail = web.find_element_by_xpath('//*[@id="job_detail"]/dd[2]/div').text
print(job_detail)
web.close()
web.switch_to.window(web.window_handles[0])
print(web.find_element_by_xpath('//*[@id="s_position_list"]/ul/li[1]/div[1]/div[1]/div[1]/a/h3').text)
time.sleep(5)

# #云播TV，处理iframe，必须先拿到iframe，切换视角到iframe，然后才拿到数据
# web.get("https://www.yunb.tv/vodplay/nishiwoderongyao45533-1-1.html")

# iframe = web.find_element_by_xpath('//*[@id="playleft"]/iframe')
# web.switch_to.frame(iframe)
# # web.switch_to.default_content()   #切回原窗口
# tx = web.find_element_by_xpath('/html/head/title').text
# print(tx)

