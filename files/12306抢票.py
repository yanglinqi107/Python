# encoding: utf-8
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
'''
想要学习Python？Python学习交流群：973783996满足你的需求，资料都已经上传群文件，可以自行下载！
'''
class Qiangpiao(object):
  def __init__(self):
    driver_path = "E:\py_pachong\chromedriver.exe"
    # 浏览器驱动
    self.drive = webdriver.Chrome(executable_path=driver_path)
    # 登陆链接
    self.login_url = "https://kyfw.12306.cn/otn/login/init"
    # 登陆后的链接
    self.initmy_url = "https://kyfw.12306.cn/otn/index/initMy12306"
    # 查询页面
    self.search_url = "https://kyfw.12306.cn/otn/leftTicket/init"
    # 乘车人页面
    self.passenger_url = "https://kyfw.12306.cn/otn/confirmPassenger/initDc"
  def wait_input(self):
    """
    主要用于页面审核；
    当输入出发地，目的地，乘车时间后，会自动出发查询submit
    :return:
    """
    self.from_station = input("出发地：")
    self.to_station = input("目的地：")
    self.depart_time = input("出发时间：")
    self.passengers = input("乘客姓名：").split(",")
    self.trains = input("车次：").split(",")
  def _login(self):
    """
    登陆验证，登陆成功后会跳转到 self.initmy_url
    :return:
    """
    self.drive.get(self.login_url)
    WebDriverWait(self.drive, 1000).until(
      EC.url_to_be(self.initmy_url)
    )
    print('登录成功')
  def _order_ticket(self):
    """
    只实现了在无票的情况下去刷票
    最关键的是等待验证 WebDriverWait
    :return:
    """
    self.drive.get(self.search_url)
    WebDriverWait(self.drive, 1000).until(
      EC.text_to_be_present_in_element_value((By.ID, "fromStationText"), self.from_station)
    )
    WebDriverWait(self.drive, 1000).until(
      EC.text_to_be_present_in_element_value((By.ID, "toStationText"), self.to_station)
    )
    WebDriverWait(self.drive, 1000).until(
      EC.text_to_be_present_in_element_value((By.ID, "train_date"), self.depart_time)
    )
    WebDriverWait(self.drive, 10000).until(
      EC.element_to_be_clickable((By.ID, "query_ticket"))
    )
    searchBtn = self.drive.find_element_by_id("query_ticket")
    searchBtn.click()
    WebDriverWait(self.drive, 1000).until(
      EC.presence_of_element_located((By.XPATH, ".//tbody[@id='queryLeftTable']/tr"))
    )
    # find_elements_by_xpath 返回的是一个列表
    # find_element_by_xpath 返回的是一个元素
    tr_list = self.drive.find_elements_by_xpath(".//tbody[@id='queryLeftTable']/tr[not(@datatran)]")
    for tr in tr_list:
      train_num = tr.find_element_by_class_name("number").text
      # print(train_num)
      if train_num in self.trains:
        left_ticket_td = tr.find_element_by_xpath(".//td[4]").text
        num = 1
        while left_ticket_td == "无":
          print("暂时无票，正在刷新")
          time.sleep(2)
          searchBtn.click()
          num += 1
          print("抢票%s次" % num)
          if left_ticket_td != "无":
            print(train_num + "有票")
            oderBtn = tr.find_element_by_xpath(".//td[13]/a")
            oderBtn.click()
            WebDriverWait(self.drive, 1000).until(
              EC.url_to_be(self.passenger_url)
            )
            WebDriverWait(self.drive, 1000).until(
              EC.presence_of_element_located((By.XPATH, ".//ul[@id='normal_passenger_id']/li"))
            )
            passenger_labels = self.drive.find_elements_by_xpath(
              ".//ul[@id='normal_passenger_id']/li/label")
            for passenger_label in passenger_labels:
              name = passenger_label.text
              if name in self.passengers:
                passenger_label.click()
            submitBtn = self.drive.find_element_by_id("submitOrder_id")
            submitBtn.click()
            WebDriverWait(self.drive, 1000).until(
              EC.presence_of_element_located((By.CLASS_NAME, "dhtmlx_wins_body_outer"))
            )
            WebDriverWait(self.drive, 1000).until(
              EC.presence_of_element_located((By.ID, "qr_submit_id"))
            )
            qr_submit = self.drive.find_element_by_id("qr_submit_id")
            qr_submit.click()
  def run(self):
    self.wait_input()
    self._login()
    self._order_ticket()
if __name__ == '__main__':
    spider = Qiangpiao()
    spider.run()