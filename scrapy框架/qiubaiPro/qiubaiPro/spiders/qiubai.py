import scrapy
from qiubaiPro.items import QiubaiproItem

class QiubaiSpider(scrapy.Spider):
    name = 'qiubai'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['https://www.qiushibaike.com/text/']

    # def parse(self, response):
    #     # 解析：作者的名称+段子的内容
    #     divs = response.xpath('//div[@class="col1 old-style-col1"]/div')
    #     all_data = []
    #     for div in divs: 
    #         # xpath返回的是列表，但是列表元素一定是Selector类型的对象
    #         # extract()可以将Selector对象中data参数存储的字符创提取出来
    #         author = div.xpath('./div/a[2]/h2/text()')[0].extract().strip()
    #         # 列表调用了extract之后，表示将列表中每一个Selector对象中data对应的字符串提取出来
    #         content = div.xpath('./a[1]/div/span//text()').extract()
    #         content = ''.join(content)
    #         print(author, content)
            
    #         dic = {
    #             'author':author,
    #             'content':content
    #         }

    #         all_data.append(dic)
    #     return all_data

    def parse(self, response):
        # 解析：作者的名称+段子的内容
        divs = response.xpath('//div[@class="col1 old-style-col1"]/div')
        for div in divs: 
            # xpath返回的是列表，但是列表元素一定是Selector类型的对象
            # extract()可以将Selector对象中data参数存储的字符创提取出来
            author = div.xpath('./div/a[2]/h2/text()')[0].extract().strip()
            # 列表调用了extract之后，表示将列表中每一个Selector对象中data对应的字符串提取出来
            content = div.xpath('./a[1]/div/span//text()').extract()
            content = ''.join(content)

            item = QiubaiproItem()
            item['author'] = author
            item['content'] = content
            # 将item提交给管道
            yield item
            