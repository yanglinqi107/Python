import requests
# import json
import pymysql

headers = {
    'User_Agent':
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36 Edg/95.0.1020.53'
}


def requests_data(url):
    response = requests.get(url=url, headers=headers)
    # print(response.json())
    # print(type(response.json()))

    dict1 = response.json()  # 类型居然是字典，而不是json
    list1 = dict1.get("data", "不存在")
    # print(type(list1))
    # print(list1)
    # dict1 = json.dumps(response.json(),ensure_ascii=False) # 这步就导致变成了字符串
    # print(type(dict1))
    # print(dict1)
    return list1

# 将数据存入Cards
def save_to_mysql_cards(hex_dic):
    connect = pymysql.connect(host='127.0.0.1',
                              user='root',
                              passwd='yanglinqi',
                              database='tft',
                              charset='utf8')
    cursor = connect.cursor()
    try:
        sql = "insert into cards values(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        args = (hex_dic["name"], hex_dic["img"], hex_dic["icon"],
                hex_dic["skill_name"], hex_dic["skill_img"],
                hex_dic["skill_type"], hex_dic["skill_desc"], hex_dic["price"],
                hex_dic["id"])
        cursor.execute(sql, args)
        connect.commit()
    except Exception as e:
        print(hex_dic)
        print(e)
    cursor.close()
    connect.close()

# 将数据存入Fetters
def save_to_mysql_fetters(id, fet):
    connect = pymysql.connect(host='127.0.0.1',
                              user='root',
                              passwd='yanglinqi',
                              database='tft',
                              charset='utf8')
    cursor = connect.cursor()
    sql = "insert into fetters values(%s,%s)"
    for fe in fet:
        args = (id, fe)
        cursor.execute(sql, args)
        connect.commit()
    cursor.close()
    connect.close()

# 将数据存入Fetter
def save_to_mysql_fetter(fet_dic):
    connect = pymysql.connect(host='127.0.0.1',
                              user='root',
                              passwd='yanglinqi',
                              database='tft',
                              charset='utf8')
    cursor = connect.cursor()
    try:
        sql = "insert into fetter values(%s,%s,%s,%s)"
        args = (fet_dic["fname"], fet_dic["icon"], fet_dic["descr"],
                fet_dic["level"])
        cursor.execute(sql, args)
        connect.commit()
    except Exception as e:
        print(e)
    cursor.close()
    connect.close()

# 将数据存入Properties
def save_to_mysql_properties(hex_dic):
    connect = pymysql.connect(host='127.0.0.1',
                              user='root',
                              passwd='yanglinqi',
                              database='tft',
                              charset='utf8')
    cursor = connect.cursor()
    try:
        sql = "insert into properties values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        args = (hex_dic["id"], hex_dic["health"], hex_dic["armor"],
                hex_dic["magic_resist"], hex_dic["material_attack"],
                hex_dic["attack_speed"], hex_dic["critical_strike_rate"],
                hex_dic["attack_distance"], hex_dic["initial_mana"],
                hex_dic["mana"])
        cursor.execute(sql, args)
        connect.commit()
    except Exception as e:
        print(e)
    cursor.close()
    connect.close()


def get_img_bytes(url):
    resp = requests.get(url=url, headers=headers)
    return resp.content


def save_data_to_cards(list1):
    # print(len(list1)) # 59
    hex_dic = {}
    jpg_domain = 'https://game.gtimg.cn/images/lol/tft/cham-icons/624x318/'
    png_domain = 'https://game.gtimg.cn/images/lol/act/img/tft/champions/'

    # print(list1)

    # 保存cards表的数据
    for hex in list1:
        # print(hex)
        # print(hex["chessId"])
        jpg_id = hex["name"].split('.')[0]  # 英雄图片的id，类型是jpg
        # hex_dic["title"] = hex["title"]
        hex_dic["name"] = hex["title"] + " " + hex["displayName"]
        hex_dic["img"] = jpg_domain + jpg_id + ".jpg"
        hex_dic["icon"] = png_domain + hex["name"]
        hex_dic["skill_name"] = hex["skillName"]
        hex_dic["skill_img"] = hex["skillImage"]
        hex_dic["skill_type"] = hex["skillType"]
        hex_dic["skill_desc"] = hex["skillDetail"].replace('\xa0', "")
        hex_dic["price"] = int(hex["price"])  # 将英雄加个转化为int型
        hex_dic["id"] = int(hex["chessId"])  # 要把英雄Id转化为int型
        # 将字典中保存的图片链接改成图片的字节流
        # hex_dic["img"] = get_img_bytes(hex_dic["img"])
        # hex_dic["icon"] = get_img_bytes(hex_dic["icon"])
        # hex_dic["skill_img"] = get_img_bytes(hex_dic["skill_img"])
        save_to_mysql_cards(hex_dic)
        print(hex_dic["id"], "成功存入数据库！")
        # print(hex_dic)


def save_data_to_fetters(list1):
    for hex in list1:
        id = int(hex["chessId"])
        races = hex["races"].split(',')
        jobs = hex["jobs"].split(',')
        fet = races + jobs
        # print(id, fet)
        # print(type(id))
        save_to_mysql_fetters(id, fet)
        print(id, '的羁绊保存至数据库')


def save_data_to_fetter(job_list, race_list):
    fet_dic = {}
    fet_list = job_list + race_list
    for fet in fet_list:
        fet_dic['fname'] = fet['name']
        fet_dic['icon'] = fet['imagePath']
        # fet_dic['icon'] = get_img_bytes(fet['imagePath'])
        fet_dic['descr'] = fet['introduce']
        level = list(fet['level'].keys())
        content = list(fet['level'].values())
        for i in range(len(level)):
            level[i] = level[i] + ':' + content[i]
        fet_dic['level'] = '$'.join(level)
        # print(fet_dic)
        save_to_mysql_fetter(fet_dic)
        print(fet_dic['fname'], '的详细信息存入数据库')


def save_data_to_properties(list1):
    # print(len(list1)) # 59
    hex_dic = {}

    for hex in list1:
        #     print(hex)
        #     print(hex["chessId"])
        hex_dic["id"] = int(hex["chessId"])  # 要把英雄Id转化为int型
        hex_dic["health"] = hex["lifeData"]
        hex_dic["armor"] = f'{hex["armor"]}/{hex["armor"]}/{hex["armor"]}'
        hex_dic[
            "magic_resist"] = f'{hex["spellBlock"]}/{hex["spellBlock"]}/{hex["spellBlock"]}'
        hex_dic["material_attack"] = hex["attackData"]
        hex_dic[
            "attack_speed"] = f'{hex["attackSpeed"]}/{hex["attackSpeed"]}/{hex["attackSpeed"]}'
        hex_dic[
            "critical_strike_rate"] = f'{hex["crit"]}%/{hex["crit"]}%/{hex["crit"]}%'
        hex_dic[
            "attack_distance"] = f'{hex["attackRange"]}/{hex["attackRange"]}/{hex["attackRange"]}'
        hex_dic[
            "initial_mana"] = f'{hex["startMagic"]}/{hex["startMagic"]}/{hex["startMagic"]}'
        hex_dic["mana"] = f'{hex["magic"]}/{hex["magic"]}/{hex["magic"]}'
        # print(hex_dic)
        save_to_mysql_properties(hex_dic)
        print(hex_dic["id"], "的属性成功存入数据库！")


if __name__ == "__main__":

    chess_url = 'https://game.gtimg.cn/images/lol/act/img/tft/js/chess.js?v=2734431'
    job_url = 'https://game.gtimg.cn/images/lol/act/img/tft/js/job.js?v=2733645'
    race_url = 'https://game.gtimg.cn/images/lol/act/img/tft/js/race.js?v=2733645'

    list1 = requests_data(chess_url)
    # print(list1)
    # save_data_to_cards(list1)  # cards表
    # save_data_to_fetters(list1) # fetters羁绊表

    # job_list = requests_data(job_url)
    # race_list = requests_data(race_url)
    # save_data_to_fetter(job_list,race_list)

    save_data_to_properties(list1)