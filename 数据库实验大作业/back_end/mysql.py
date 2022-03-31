import os
import pymysql


############################## 搜索后的小卡片，item
class Item:
    def __init__(self, arg: tuple):  #(name, img, id, price)
        self.name = arg[0]
        self.img = arg[1]
        self.id = arg[2]
        self.price = arg[3]

    def addFetters(self, fnames: list, icons: list):
        self.fetters = []
        for i in range(len(fnames)):
            d = {'fname': fnames[i], 'img': icons[i]}
            self.fetters.append(d)

    def returnJson(self):
        return {
            'name': self.name,
            'img': self.img,
            'id': int(self.id),
            'price': int(self.price),
            'fetters': self.fetters
        }


############################# 点开小卡片后的详细信息，card
class Card():
    desc = []  #[('icon', 'descr', 'level'),]
    synerge = {}  #{icon:}

    def __init__(self, arg: tuple
                 ):  #(name,img,icon,skill_name,s_img,s_type,s_desc,price,id)
        self.name = arg[0]
        self.img = arg[1]
        self.icon = arg[2]
        self.skill_name = arg[3]
        self.skill_img = arg[4]
        self.skill_type = arg[5]
        self.skill_desc = arg[6]
        self.price = arg[7]
        self.id = arg[8]

    def addFetters(self, arg: tuple):
        self.fetters = [t[0] for t in arg]

    def addDesc(self, desc: tuple):
        self.desc.append(list(desc))

    def addProperties(
        self, arg: tuple
    ):  #(id,health,armor,magic_resist,material_attack,attack_speed,critical_strike_rate,attack_distance,initial_mana,mana)
        self.property = list(arg[1:])

    def addSynerge(self, fetter: str, arg: tuple):
        tup = [[ls[0], ls[1]] for ls in arg]
        self.synerge[fetter] = tup

    def returnJson(self):
        self.data = []
        for i in range(len(self.fetters)):
            d = {
                'icon': self.desc[i][0],
                "fname": self.fetters[i],
                "desc": self.desc[i][1],
                "level": self.desc[i][2]
            }
            self.data.append(d)
        return {
            'name': self.name,
            'img': self.img,
            'icon': self.icon,
            'id': int(self.id),
            'skill_name': self.skill_name,
            'skill_img': self.skill_img,
            'skill_type': self.skill_type,
            'skill_desc': self.skill_desc,
            'price': int(self.price),
            'fetters': self.data,
            'property': self.property,
            'synerge': self.synerge
        }


############################# 数据库类，封装数据库操作
class Db:
    def __init__(self, database: str):
        self.database = database
        self.db = pymysql.Connect(host='localhost',
                                  user='root',
                                  password='yanglinqi',
                                  database=database)
        self.cursor = self.db.cursor()

    def exit(self):
        self.db.close()

    def getAll(self):
        sql = f'select * from v_items'
        self.cursor.execute(sql)
        data = self.cursor.fetchall()  #((name, img, id, price),)
        ret = []
        for arg in data:
            item = Item(arg)
            dql = f'select fname from fetters where id={item.id}'
            self.cursor.execute(dql)  #(('辛迪加',), ('黑魔法师',))
            fetters_query = self.cursor.fetchall()
            fetters = [t[0] for t in fetters_query]
            icons = []
            for fetter in fetters:
                self.cursor.execute(
                    f'select icon from fetter where fname="{fetter}"')
                icon = self.cursor.fetchone()
                icons.append(icon[0])
            item.addFetters(fetters, icons)
            ret.append(item.returnJson())
        return ret

    ################################## 英雄界面进行搜索，返回一组Item数据<嵌套的元组>
    def getItems(self, name: str):
        sql = f'select * from v_items where name like "%{name}%"'
        self.cursor.execute(sql)
        data = self.cursor.fetchall()  #((name, img, id, price),)
        ret = []
        for arg in data:
            item = Item(arg)
            dql = f'select fname from fetters where id={item.id}'
            self.cursor.execute(dql)  #(('辛迪加',), ('黑魔法师',))
            fetters = [t[0] for t in self.cursor.fetchall()]
            icons = []
            for fetter in fetters:
                self.cursor.execute(
                    f'select icon from fetter where fname="{fetter}"')
                icon = self.cursor.fetchone()
                icons.append(icon[0])
            item.addFetters(fetters, icons)
            ret.append(item.returnJson())
        return ret

    def getItemsByPrice(self, price: int):
        sql = f'select * from v_items where price={price}'
        self.cursor.execute(sql)
        data = self.cursor.fetchall()  #((name, img, id, price),)
        ret = []
        for arg in data:
            item = Item(arg)
            dql = f'select fname from fetters where id={item.id}'
            self.cursor.execute(dql)  #(('辛迪加',), ('黑魔法师',))
            fetters = [t[0] for t in self.cursor.fetchall()]
            icons = []
            for fetter in fetters:
                self.cursor.execute(
                    f'select icon from fetter where fname="{fetter}"')
                icon = self.cursor.fetchone()
                icons.append(icon[0])
            item.addFetters(fetters, icons)
            ret.append(item.returnJson())
        return ret

    def getItemsByFetter(self, fetter: str):
        self.cursor.execute(f'select id from fetters where fname="{fetter}"')
        ids = self.cursor.fetchall()
        ret = []
        for id in ids:
            sql = f'select * from v_items where id={id[0]}'
            self.cursor.execute(sql)
            data = self.cursor.fetchone()  #((name, img, id, price),)
            item = Item(data)
            dql = f'select fname from fetters where id={item.id}'
            self.cursor.execute(dql)  #(('辛迪加',), ('黑魔法师',))
            fetters = [t[0] for t in self.cursor.fetchall()]
            icons = []
            for fetter in fetters:
                self.cursor.execute(
                    f'select icon from fetter where fname="{fetter}"')
                icon = self.cursor.fetchone()
                icons.append(icon[0])
            item.addFetters(fetters, icons)
            ret.append(item.returnJson())
        return ret

    ################################## 点开某个英雄卡片，返回该英雄详细信息Card
    def getCard(self, id: int):
        #(name,img,icon,skill_name,s_img,s_type,s_desc,price,id)
        sql = f'select * from cards where id={id}'
        self.cursor.execute(sql)
        data = self.cursor.fetchone()
        ret = Card(data)
        #(('辛迪加',), ('黑魔法师',), )
        sql = f'select fname from fetters where id={ret.id}'
        self.cursor.execute(sql)
        data = self.cursor.fetchall()
        ret.addFetters(data)
        #[(icon, descr, level), ]
        #[(id, icon), ]
        for fetter in ret.fetters:
            sql = f'select icon, descr, level from fetter where fname="{fetter}"'
            self.cursor.execute(sql)
            data = self.cursor.fetchone()  #(icon, descr, level)
            ret.addDesc(data)
            sql = f'select cards.id, icon from fetters join cards on fetters.id=cards.id where fname="{fetter}"'
            self.cursor.execute(sql)
            data = self.cursor.fetchall()
            ret.addSynerge(fetter, data)
        #(id,health,armor,magic_resist,material_attack,attack_speed,critical_strike_rate,attack_distance,initial_mana,mana)
        sql = f'select * from properties where id={id}'
        self.cursor.execute(sql)
        data = self.cursor.fetchone()
        ret.addProperties(data)

        return ret.returnJson()

    ###################################################### 删除一张card
    def delete(self, id: int):
        sql = f'delete from cards where id={id}'
        self.cursor.execute(sql)
        return '删除成功!'

    ###################################################### 用户操作
    def getUser(self, name: str, pwd: str):
        sql = f'select * from users where id="{name}"'
        self.cursor.execute(sql)
        data = self.cursor.fetchone()
        if data != None and data[1] == pwd:
            return data[2]
        elif data == None:
            return "用户不存在!"
        else:
            return "密码错误!"

    def addUser(self, name: str, pwd: str):
        sql = f'call adduser("{name}", "{pwd}", 1, @result);'
        self.cursor.execute(sql)
        self.cursor.execute('select @result')
        data = self.cursor.fetchone()
        if data[0] == 1:
            self.db.commit()
            return "1"
        else:
            return "error: 用户名已被使用."

    ######################################################## 恢复数据库
    def resume(self):
        self.exit()
        data = os.system('mysql -uroot -p1234 tft < D:/desktop/sql/tft.sql')
        if data == 0:
            self.__init__(self.database)
            data = self.getAll()
            return data
        else:
            return '恢复数据库失败...'


if __name__ == '__main__':
    db = Db('tft')
    data = db.getItemsByPrice(1)
    db.exit()
