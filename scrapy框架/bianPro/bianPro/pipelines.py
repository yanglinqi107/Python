# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface


from scrapy.pipelines.images import ImagesPipeline
import scrapy

class BianproPipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        # return super().get_media_requests(item, info)
        # print(item['img_src'])
        yield scrapy.Request(item['img_src'])
    
    # # 指定图片存储的路径
    # def file_path(self, request, response=None, info=None):
    #     imgName = request.url.split('/')[-1]
    #     return imgName

    def file_path(self, request, response=None, info=None, item=None):
        imgName = item['img_name'] + '.jpg'
        # print(imgName)
        return imgName

    def item_completed(self, results, item, info):
        # return super().item_completed(results, item, info)
        return item

    