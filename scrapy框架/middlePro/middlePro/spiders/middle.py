import scrapy


class MiddleSpider(scrapy.Spider):
    name = 'middle'
    # allowed_domains = ['xx.c']
    start_urls = ['https://www.baidu.com/s?wd=IP']

    def parse(self, response):
        page_text = response.text()
        with open('ip.html',mode='w',encoding='utf-8') as f:
            f.write(page_text)
        print("over!")
