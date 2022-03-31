import pymysql

# 连接数据库
conn = pymysql.connect(host='localhost', user='root', passwd='yanglinqi', database='savePic',charset='utf8')
# 创建游标
cursor = conn.cursor()
# sql语句
sql = "select img from picture where imgName='图片';"

cursor.execute(sql)
conn.commit()
img = cursor.fetchone()[0]

with open('./pic.jpg', mode='wb') as f:
    f.write(img)
print("pic保存成功！")
cursor.close()
conn.close()