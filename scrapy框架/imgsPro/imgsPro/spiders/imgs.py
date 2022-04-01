import scrapy
from imgsPro.items import ImgsproItem

class ImgsSpider(scrapy.Spider):
    name = 'imgs'
    # allowed_domains = ['xxx.c']
    start_urls = ['https://www.4kbizhi.com']

    def parse(self, response):
        li_list = response.xpath('/html/body/div[3]/div[1]/ul/li')
        for li in li_list:
            src = self.start_urls[0] + li.xpath('./a[2]/img/@src | ./a/img/@src').extract_first()
            print(src)
            item = ImgsproItem()
            item['src'] = src
            yield item
