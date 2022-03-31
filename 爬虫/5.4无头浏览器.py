from selenium.webdriver import Chrome
from selenium.webdriver import ChromeOptions
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.select import Select
import time
#准备好参数配置
# 实现无可视化界面的操作
opt = Options()
# opt.add_argument('--headless')
# opt.add_argument('--disable-gpu')
opt.binary_location='D:\Program Files\Google\Chrome\Application\chrome.exe'
# 实现规避检测
option = ChromeOptions()
option.add_experimental_option('excludeSwitches',['enable-automation'])
web = Chrome(options = option, chrome_options=opt)
web.get("https://www.endata.com.cn/BoxOffice/BO/Year/index.html")

time.sleep(2)

# sel_el = web.find_element_by_xpath('//*[@id="OptionDate"]')
# sel = Select(sel_el)
# for i in range(len(sel.options)):
#     sel.select_by_index(i)
#     time.sleep(2)
#     table = web.find_element_by_xpath('//*[@id="TableList"]')
#     print(table.text)
#     print("=================================================")
# print("运行完毕！")

# 拿到页面代码
print(web.page_source)