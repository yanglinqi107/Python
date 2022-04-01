import scrapy
import re 
from bianPro.items import BianproItem

class BianpicSpider(scrapy.Spider):
    name = 'bianpic'
    # allowed_domains = ['www.xxxx.com']
    start_urls = ['https://pic.netbian.com']
    # 生成一个通用的URL模板
    url = "https://pic.netbian.com/index_%d.html"
    page_num = 2

    def parse(self, response):
        li_list = response.xpath('//*[@id="main"]/div[3]/ul/li')
        for li in li_list:
            # img_name = li.xpath('./a/b/text()')[0].extract()
            img_url = self.start_urls[0] + li.xpath('./a/@href').extract_first()
            # print(img_name)
            # print(img_url)
            # print(response.url)显示当前请求的url
            img_name = re.findall(r'tupian/(.*?).html', img_url, re.S)[0]   # https://pic.netbian.com/tupian/28325.html 将数字作为文件名
            item = BianproItem()
            item['img_name'] = img_name
            # print(img_name)
            yield scrapy.Request(url=img_url,callback=self.parse_detail, meta={'item':item},)
        if self.page_num <= 162:
            new_url = format(self.url%self.page_num)
            self.page_num += 1
            # 手动请求发送,callback回调函数专门用于数据解析
            yield scrapy.Request(url=new_url,callback=self.parse)

    def parse_detail(self, response):
        src = self.start_urls[0] + response.xpath('//*[@id="img"]/img/@src').extract_first()
        # print(src)
        item = response.meta['item']
        item['img_src'] = src
        yield item