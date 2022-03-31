import os


def main(path):
    os.chdir(path)
    files = os.listdir()
    # print(files)
    for f in files:
        if ".md" not in f:
            continue
        with open(f, 'r', encoding='utf-8') as fr:
            content = fr.read()
        # if (content.find("assets") == -1):
        #     continue
        if "assets" not in content:
            continue
        content = content.replace("assets", f.strip(".md"))
        with open(f, 'w+', encoding='utf-8') as fw:
            fw.write(content)
        print(f, "over!")


if __name__ == "__main__":
    path = input("请输入路径: ")
    main(path)