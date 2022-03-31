from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select



opt = Options()
opt.binary_location=r'D:\Program Files\Google\Chrome\Application\chrome.exe'
opt.add_argument('--disable-blink-features=AutomationControlled')
opt.add_experimental_option('excludeSwitches', ['enable-automation'])
web = Chrome(options=opt)

url = "https://kyfw.12306.cn/otn/leftTicket/init?linktypeid=dc&fs=%E6%AD%A6%E6%B1%89,WHN&ts=%E5%8D%97%E6%98%8C,NCG&date=2022-01-08&flag=N,N,Y"
web.maximize_window()
EC.url_to_be(
    web.get(url)
)

# web.find_element_by_xpath('//*[@id="J-userName"]').send_keys("")
# web.find_element_by_xpath('//*[@id="J-password"]').send_keys('')
# web.find_element_by_id('J-login').click()

wait = WebDriverWait(web,5,0.2)

# web.switch_to.frame(iframe_label)
clock = wait.until(
    EC.element_to_be_clickable(web.find_element_by_id('gb_closeDefaultWarningWindowDialog_id'))
)
clock.click()


# unfind = False
# while not unfind:
#     unfind = WebDriverWait(web,1000,0.3).until_not(
#         EC.text_to_be_present_in_element((By.XPATH,'//*[@id="ticket_4e000G203509_01_05"]/td[13]'),"预订")
#     )
#     print(unfind)
#     web.find_element_by_xpath('//*[@id="query_ticket"]').click()
#     sleep(2)

js = "window.scrollTo(0,600)"
web.execute_script(js)

# print(result15)
# web.find_element_by_xpath('//*[@id="ticket_850000Z12821_10_11"]/td[13]/a').click()
web.find_element_by_xpath('//*[@id="ticket_390000K7990S_01_05"]/td[13]/a').click()

sleep(0.5)
web.find_element_by_xpath('//*[@id="J-userName"]').send_keys('')
web.find_element_by_xpath('//*[@id="J-password"]').send_keys('')
web.find_element_by_id('J-login').click()
sleep(1)
btn = web.find_element_by_id('nc_1_n1z')
ActionChains(web).drag_and_drop_by_offset(btn, 300, 0).perform()
sleep(2)
web.find_element_by_xpath('//*[@id="normalPassenger_0"]').click()
web.find_element_by_xpath('//*[@id="dialog_xsertcj_ok"]').click()
sleep(1)
# web.find_elements_by_xpath('/html/body/div[1]/div[9]/div[3]/div[2]/table/tbody[2]/tr[1]/td[3]/select').click()
select = Select(web.find_element_by_css_selector('select[id=seatType_1]'))
select.select_by_value('1')
# web.find_element_by_css_selector('value="1"')
web.find_element_by_xpath('//*[@id="submitOrder_id"]').click()
sleep(20)

sleep(1)



sleep(1000000)