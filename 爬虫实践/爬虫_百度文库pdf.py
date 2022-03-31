import shutil
import requests
import re

import glob
import os
import fitz # pip install PyMuPDF
# from requests.api import get  

# 获取完整的网页源代码
def response(url):
    # url = 'https://wenku.baidu.com/view/e98449101b5f312b3169a45177232f60dccce70e.html'
    cookies = {
        'kunlunFlag': '1',
        'BAIDUID': '198DFC9FB9C70E6246854D4CA6A83752:FG=1',
        'BIDUPSID': '198DFC9FB9C70E6246854D4CA6A83752',
        'PSTM': '1637048358',
        '__yjs_duid': '1_04d90f15275790fe405ca0edda2e0a691637051147542',
        '_click_param_reader_query_ab': '-1',
        'layer_show_times_total_8_4f8ea67400e1780ab409be0d765e5aab': '2',
        'BDORZ': 'B490B5EBF6F3CD402E515D22BCDA1598',
        'Hm_lvt_f06186a102b11eb5f7bcfeeab8d86b34': '1637403048,1637415655,1637993654',
        'BDUSS': 'BkVEY0ZFJYfjkwNG9GdDdxYmVvaXl0eEliam9Wa2tQSGxCR3lua1hBYndhOGxoRVFBQUFBJCQAAAAAAAAAAAEAAAC8P2F4TUxax6fRsAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAPDeoWHw3qFhM1',
        'BDUSS_BFESS': 'BkVEY0ZFJYfjkwNG9GdDdxYmVvaXl0eEliam9Wa2tQSGxCR3lua1hBYndhOGxoRVFBQUFBJCQAAAAAAAAAAAEAAAC8P2F4TUxax6fRsAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAPDeoWHw3qFhM1',
        'BAIDUID_BFESS': '198DFC9FB9C70E6246854D4CA6A83752:FG=1',
        'delPer': '0',
        'PSINO': '3',
        'ZD_ENTRY': 'baidu',
        '__wk_view_topbar_20211029': '1',
        'Hm_lvt_d8bfb560f8d03bbefc9bdecafc4a4bf6': '1637669843,1637986431,1637986595,1638177445',
        'Hm_lpvt_d8bfb560f8d03bbefc9bdecafc4a4bf6': '1638179481',
        'bcat': '918eadd92e787b0db58a73c5c9c5915359d4ec2460753b44fa8fde55ad0028f367f10e0262c03edd8baa11ab1aa68f8baf2da1cb2546a48890f1c8c989081ae30e198d9f3c39fc3eb815cc156673a6ddd0bcd23540a76a4b37a869177edbe38d5bbe7cf4b85ae47171137c3cdaf12e3429305bc08e3b2bd253c5310eaf1a038b',
        'H_PS_PSSID': '35261_35105_35240_35048_34584_34518_34578_35317_26350_35144_35301',
    }

    headers = {
        'Connection': 'keep-alive',
        'Pragma': 'no-cache',
        'Cache-Control': 'no-cache',
        'sec-ch-ua': '"Microsoft Edge";v="95", "Chromium";v="95", ";Not A Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36 Edg/95.0.1020.53',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Sec-Fetch-Site': 'none',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-User': '?1',
        'Sec-Fetch-Dest': 'document',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    }
    response = requests.get(url=url, cookies=cookies, headers=headers)
    # print(response.text)
    return response.text

# 获取标题
def get_title(page_text):
    # 获取标题作为文件名
    title = re.findall(r'<title>(.*?)</title>',page_text,re.S)[0].strip(" - 百度文库")
    # print(title)
    return title
    # 存储网页源代码，直接在网页看容易出错，最好存储之后在文件中看，正则不容易错
    # with open('E:\\text.html', mode='w', encoding='utf-8') as f:
    #     f.write(response.text)
    # with open('E:\\text.html',mode='r', encoding='utf-8') as f:
    #     text = f.read()

    # "png":[{(.*?)}]正则出错，似乎是括号的原因，改成"png":(.*?)}]正确
    # pdf有23页，但pageLoadUrl一共有46个，前23个是没用的链接，需获取png后面的23个链接
    # 先将后面23个链接整体提出来

# 获取所有图片链接
def get_url_list(page_text):
    obj = re.compile(r'"png":(.*?)}]',re.S)
    all_urls = obj.findall(page_text)[0]
    # print(all_urls)

    # 获取一个个url链接
    obj2 = re.compile('"pageLoadUrl":"(.*?)"',re.S)
    url_list = obj2.findall(all_urls)
    # print(len(url_list))  # 打印链接个数，是否和页面数一致
    return url_list

# 下载所有图片
def down_pngs(path, url_list):
    # 一张张图片保存测试
    name = 1000
    for url in url_list:
        # print(url)
        page_content = requests.get(url=url).content
        with open(f'{path}\\{name}.png',mode='wb') as f:
            f.write(page_content)
            print(name,'图片完成')
            name += 1


def down_pdf(url_list, title):
    doc = fitz.open()
    for url in url_list:
        page_content = requests.get(url=url).content
        pdfbytes = fitz.convertToPDF(page_content)
        imgpdf = fitz.open('pdf',pdfbytes)
        doc.insertPDF(imgpdf)
        doc.save(f'E:\\Python\\爬虫_百度文库\\百度文库\\{title}.pdf')
        doc.close()

def pic_to_pdf(img_dir, title):
    doc = fitz.open()
    for img in sorted(glob.glob("{}/PngTemp/*".format(img_dir))):  # 读取图片，确保按文件名排序
        imgdoc = fitz.open(img)  # 打开图片
        pdfbytes = imgdoc.convertToPDF()  # 使用图片创建单页的 PDF
        imgpdf = fitz.open("pdf", pdfbytes)
        doc.insertPDF(imgpdf)  # 将当前页插入文档
    if os.path.exists(f"{img_dir}\\{title}.pdf"):
        os.remove(f"{img_dir}\\{title}.pdf")
    doc.save(f"{img_dir}\\{title}.pdf")  # 保存pdf文件
    doc.close()


if __name__ == '__main__':
    url = input('输入网址：')
    page_text = response(url)
    title = get_title(page_text)
    url_list = get_url_list(page_text)
    # down_pdf(url_list, title)
    # 创建临时文件夹保存图片
    path = "E:\\Python\\爬虫_百度文库\\百度文库\\PngTemp"
    if not os.path.exists(path = path):
        os.mkdir(path = path)
    down_pngs(path, url_list)
    img_dir = "E:\\Python\\爬虫_百度文库\\百度文库"
    pic_to_pdf(img_dir, title)
    # 删除文件夹
    # shutil.rmtree(path)







# from selenium.webdriver import Chrome
# from selenium.webdriver.chrome.options import Options
# from time import sleep

# opt = Options()
# # opt.add_argument('--headless')
# opt.add_argument('--disable-blink-features=AutomationControlled')
# opt.binary_location = r'D:\Program Files\Google\Chrome\Application\chrome.exe'
# driver = Chrome(options=opt)
# url = 'https://wenku.baidu.com/view/e98449101b5f312b3169a45177232f60dccce70e.html'
# driver.get(url)

# print(driver.page_source)
# links = driver.find_element_by_xpath("//div[@class='reader-pic-item']/@style")
# print(links)
# # reader_container = driver.find_element_by_xpath('//*[@id="reader-container"]')
# # pages = driver.find_elements_by_xpath('//*[@id="reader-container"]/div')  

# login_pic = driver.find_element_by_class_name('user-icon')
# login_pic.click()
# # iframe = driver.find_element_by_xpath('/html/body/div[1]/iframe')
# # driver.switch_to.frame(iframe)
# sleep(1)
# login = driver.find_element_by_id('TANGRAM__PSP_11__footerULoginBtn')
# login.click()
# userName = driver.find_element_by_xpath('//*[@id="TANGRAM__PSP_11__userName"]')
# password = driver.find_element_by_xpath('//*[@id="TANGRAM__PSP_11__password"]')
# sleep(1)
# userName.send_keys('')
# password.send_keys('')
# submit = driver.find_element_by_xpath('//*[@id="TANGRAM__PSP_11__submit"]')
# submit.click()
# # pages = driver.find_elements_by_class_name('reader-pic-item')  
# # print(pages)
# # for page in pages:                          
# #     page_url = page.find_element_by_xpath('./div[1]')
# #     page_url = page_url.get_attribute('style')
# #     print(page_url)


