# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import pymysql

class QiubaiproPipeline:
    fp = None
    # 重写父类的一个方法：该方法只在开始爬虫的时候调用一次
    def open_spider(self,spider):
        print('开始爬虫……')
        self.fp = open('./qiubai.txt','w',encoding='utf-8') 
    # 专门用来处理item对象
    # 该方法可以接收爬虫文件提交过来的item的对象
    # 该方法每接收一个item就会被调用一次
    def process_item(self, item, spider):
        author = item['author']
        content = item['content']

        self.fp.write(author+':'+content+'\n')

        return item #传递给下一个即将被执行的管道类（根据优先级）

    def close_spider(self,spider):
        print("结束爬虫！")
        self.fp.close()

class mysqlPipeline():
    conn = None
    cursor = None
    def open_spider(self,spider):
        self.conn = pymysql.Connect(host='127.0.0.1',port=3306,user='root',password='yanglinqi',db='qiubai',charset='utf8')
    def process_item(self,item,spider):
        self.cursor = self.conn.cursor()
        try:
            self.cursor.execute('insert into qiubai values("%s","%s")'%(item["author"],item["content"]))
            self.conn.commit()
        except Exception as e:
            print(e)
            self.conn.rollback()
        return item #传递给下一个即将被执行的管道类

    def close_spider(self,spider):
        self.cursor.close()
        self.conn.close()