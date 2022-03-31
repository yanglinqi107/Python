import os
import re
import shutil


# 找md文件中的图片
def findPic(name):
    with open(name, 'r', encoding='utf-8') as fr:
        content = fr.read()
    pic_list = re.findall(r'assets/(.*?.png)', content)
    # # 测试是否找到所有图片
    # print("图片数量：", len(pic_list))
    # for pic in pic_list:
    #     if os.path.isfile(f"assets\\{pic}"):
    #         print(pic, "exist")
    #     else:
    #         print(f"\\assets\\{pic}")
    return pic_list


def movePic(pic_list, newPath):
    for pic in pic_list:
        if os.path.isfile(f"assets\\{pic}"):
            shutil.copyfile(f"assets\\{pic}", f"{newPath}\\{pic}")
            print(f"{pic} 移动完成")
        else:
            print(f"{pic} 不存在")


def main():
    path = input("请原文件夹输入路径：")
    blog = "E:\\yanglinqi_blog\\source\\_posts"

    try:
        os.chdir(path)
    except Exception as e:
        print(e)
        exit(0)

    while (True):
        name = input("输入文件名不要后缀（exit 退出）：")
        newPath = blog + "\\" + name  # 准备好在博客哪里要创建的文件夹的路径
        if name == "exit":
            break
        name += ".md"
        if os.path.isfile(f"{name}"):
            pic_list = findPic(name)    
            if (len(pic_list) != 0):
                # 创建文件夹
                if not os.path.exists(newPath):
                    os.mkdir(newPath)
                movePic(pic_list, newPath)
        else:
            print("该文件不存在！")


if __name__ == "__main__":
    main()