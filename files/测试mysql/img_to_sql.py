import pymysql

# D:\MLZ107\Pictures\wallpaper\5kxcvrtjlqk.jpg
conn = pymysql.connect(host="127.0.0.1", user="root", password="yanglinqi", database="savePic", charset="utf8")

cursor = conn.cursor()

with open(r"E:\Python\5kxcvrtjlqk.jpg", mode='rb') as f:
    img = f.read()

sql = 'insert into picture values (%s,%s);' # 使用%  或者 format或报错，最好还是使用args
# print(sql)
args = ("图片", img)

cursor.execute(sql, args)

conn.commit()
cursor.close()
conn.close()