from lxml import etree

tree = etree.parse('a.html')
# result = tree.xpath('/html')
# result = tree.xpath('/html/body/ul/li/a/text()')
# result = tree.xpath('/html/body/ul/li[1]/a/text()')     # xpath从1开始数
# result = tree.xpath("/html/body/ol/li/a[@href='dapao']/text()")     # xpath从1开始数
# print(result)

# ol_li_list = tree.xpath('/html/body/ol/li')
# for li in ol_li_list:
#     #从每一个li中提取到文字信息
#     result = li.xpath('./a/text()')  #在当前节点去查找，相对查找 
#     print(result)
#     result2 = li.xpath('./a/@href')
#     print(result2)
print(tree.xpath('/html/body/ul/li/a/@href'))