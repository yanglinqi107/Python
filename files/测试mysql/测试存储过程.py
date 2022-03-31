import pymysql

connect = pymysql.connect(host='127.0.0.1',
                          user='root',
                          passwd='yanglinqi',
                          database='tft',
                          charset='utf8')
cursor = connect.cursor()

# sql ="call adduser('0003','13234',1,@result);"
# cursor.execute(sql)
# sql = "select @result;"
# cursor.execute(sql)
# connect.commit()
# res = cursor.fetchone()[0]
# print(res)

sql = 'source D:/Program Files/mysql-8.0.27-winx64/data_backup/backup_tft.sql'
cursor.execute(sql)
connect.commit()

cursor.close()

connect.close()