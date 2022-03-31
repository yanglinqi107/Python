from lxml import etree

xml = """
<book>
    <id>1</id>
    <name>野花遍地香</name>
    <price>1.23</price>
    <nick>臭豆腐</nick>
    <author>
        <nick id="10086">周东强</nick>
        <nick id="10010">周芷若</nick>
        <nick class="joy">周杰伦</nick>
        <nick class="jolin">蔡依林</nick>
        <div>
            <nick>都叫我佛教飞机</nick>
        </div>
        <span>
            <nick>都叫我佛教飞机2</nick>
            <div>
                <nick>都叫我佛教飞机3</nick>
            </div>
        </span>
    </author>
    <partner>
        <nick id="ppc">胖胖陈</nick>
        <nick id="ppbc">胖胖不陈</nick>
    </partner>
</book>
"""

tree = etree.XML(xml)
#result = tree.xpath('/book')
# result = tree.xpath('/book/name')
# result = tree.xpath('/book/name/text()')    #text()是拿文本
# result = tree.xpath('/book/author/nick/text()') 
# result = tree.xpath('/book/author//nick/text()')  # // author后代所有nick节点的文本
result = tree.xpath('/book/author/*/nick/text()')   # *通配符 author子节点*的子节点nick的文本

print(result)

