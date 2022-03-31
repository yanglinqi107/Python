import pymysql

class Item:
    def __init__(self, arg: tuple):   #(title, name, img, id, price)
        self.title = arg[0]
        self.name = arg[1]
        self.img = arg[2]
        self.id = arg[3]
        self.price = arg[4]
        
    def addFetters(self, arg: tuple):
        self.fetters = [t[0] for t in arg]
    
    def returnJson(self):
        return {'title':self.title, 'name':self.name, 'img':self.img, 'id':int(self.id), 'price':int(self.price), 'fetters':self.fetters}

class Db: 
    def __init__(self, database: str):
        self.db = pymysql.Connect(host='localhost', user='root', password='1234', database=database)
        self.cursor = self.db.cursor()
    
    def exit(self):
        self.db.close()
    
    def getItems(self, name: str):
        sql = f'select * from v_items where name like "%{name}%"'
        self.cursor.execute(sql)
        data = self.cursor.fetchall() #((title, name, img, id, price),)
        ret = []
        for arg in data:
            item = Item(arg)
            dql = f'select name from fetters where id={item.id}'
            self.cursor.execute(dql)  #(('辛迪加',), ('黑魔法师',))
            item.addFetters(self.cursor.fetchall())
            ret.append(item.returnJson())
        return ret

    def getUser(self, name: str):
        sql = f'select * from users where user_id="{name}"'
        self.cursor.execute(sql)
        data = self.cursor.fetchone()#(icon, desc, level)
        return data
    
    def addUser(self, name: str, pwd: str):
        if self.getUser(name) == None:
            sql = f'insert into users(user_id, pwd) values("{name}","{pwd}");'
            self.cursor.execute(sql)
            self.db.commit()
            return "用户添加成功!"
        else:
            return "error: 用户名已被使用."
    
    def getAll(self):
        sql = f'select * from v_items'
        self.cursor.execute(sql)
        data = self.cursor.fetchall() #((title, name, img, id, price),)
        ret = []
        for arg in data:
            item = Item(arg)
            dql = f'select name from fetters where id={item.id}'
            self.cursor.execute(dql)  #(('辛迪加',), ('黑魔法师',))
            item.addFetters(self.cursor.fetchall())
            ret.append(item.returnJson())
        return ret

if __name__ == '__main__':
    db = Db('tmp')
    ret = db.addUser('tom', '12345')
    print(ret)
    db.exit()