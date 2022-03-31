#!/usr/bin/env python
# coding: utf-8

import requests
import re
import aiohttp
import aiofiles
import asyncio
import os
import shutil
from Crypto.Cipher import AES

cookies = {
    'lang': 'en_US',
    'authmethod': 'authpwd',
    'ilxpub-user-info': '{\\"username\\": \\"\\"\\054 \\"version\\": 1\\054 \\"enrollmentStatusHash\\": null\\054 \\"header_urls\\": {\\"logout\\": \\"https://ilearningx.huawei.com/logout\\"\\054 \\"account_settings\\": \\"https://ilearningx.huawei.com/account/settings\\"}}',
    'ilxpub-logged-in': 'true',
    'csrftoken': '8UAvRWDBnNBvrY12QiYmy560wKWG9jKY',
    'a053502d57194777a2a8dd2bd6b96c90': 'WyI0MjE0OTI1NjEwIl0',
    'HWWAFSESTIME': '1643112454258',
    'HWWAFSESID': '7db697ccf75df78b3d',
    'lang_key': 'cn',
    'ilxpub_sessionid': '1|ralkrb2qebq9s94giutmdyj83luqg3ak|NtEWuXBLBpUO|IjM5MGM2ZGFiNjc2YzZmZDhmNjgwMWU5OTZjYmExOTgzMjA3MmJlYTk3MmU5NTUxMmQ3NjMwMTRhNDQyYTY1NzUi:1nCKdz:hw8ZiJTuzNWUbTkeMZrVnaDo22o',
}

headers = {
    'Connection': 'keep-alive',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="92"',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'X-CSRFToken': '8UAvRWDBnNBvrY12QiYmy560wKWG9jKY',
    'X-Requested-With': 'XMLHttpRequest',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36 HBPC/12.0.0.300',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Dest': 'empty',
    'Referer': 'https://ilearningx.huawei.com/courses/course-v1:HuaweiX+CBUCNXX158+Self-paced/courseware/ce8d614342bd44518acbb6f97020240a/f004e03933874538bbe63ae151f9292e/?activate_block_id=block-v1%3AHuaweiX%2BCBUCNXX158%2BSelf-paced%2Btype%40sequential%2Bblock%40f004e03933874538bbe63ae151f9292e',
    'Accept-Language': 'zh-CN,zh;q=0.9',
}


# 路径
path = r".\huawei\temp"

session = requests.Session()


# 获取该url页面的源代码，并存入文件，文件名为title
def save_source(url, title):

    response = session.get(url=url, headers=headers, cookies=cookies)

    # print(response)
    # print(response.text)

    with open(r'%s\%s.html' % (path, title), mode='w', encoding='utf-8') as f:
        f.write(response.text)
    print(url, '的网页源代码保存中...')
    print(f"{title}.html保存完毕")


# 从save_source保存的文件中读取所有子页面的链接，并保存页面源代码至文件
# 返回文件名
def get_page_url():
    with open('%s\orgin.html' % (path), mode='r', encoding='utf-8') as f:
        html = f.read()

    obj1 = re.compile(
        r'(<div class="menu-item  ">|<div class="menu-item active ">).*?<a class="accordion-nav" href="(.*?)">.*?<p class="accordion-display-name" title="(.*?)">',
        re.S)
    page_href_list = obj1.findall(html)

    # print(len(page_href_list))

    page_list = []

    for page in page_href_list:
        # print(page)
        page_href = 'https://ilearningx.huawei.com' + page[1]  # 获取链接并拼接
        # print(page_href)
        page_title = page[2]  # 获取子页面的名称
        # print(page_title)

        # 保存子页面的页面源代码
        save_source(page_href, page_title)

        # tuple1 = (page_href, page_title)    # 将网页链接和名称保存至元组
        page_list.append(page_title)  # 将元组添加到列表中

    # print(page_list)
    return page_list  # 返回存有文件名的列表


def get_video_id(title):
    with open('{0}\{1}.html'.format(path, title), mode='r',
              encoding='utf-8') as f:
        page = f.read()
    video_id_list = re.findall(r';video_id&#34;: &#34;(.*?)&#34;', page, re.S)
    # print(title)
    # if len(video_id_list)!=0:
    #     print(video_id_list)
    # else:
    #     print('无视频')

    return video_id_list


# 通过video_id获取m3u8文件地址，并保存至文件中，单个页面的
def get_m3u8_url(title, video_id_list):
    domain = 'https://ilearningx.huawei.com/vod/videos/'
    # print(title)
    m3u8_url_list = []
    for video_id in video_id_list:
        video_id_url = domain + video_id  # 拼接网址
        # print(video_id_url)
        response = session.get(url=video_id_url,
                               headers=headers,
                               cookies=cookies)

        # print(response.text)
        # with open(f".\huawei\{video_id}.txt", "w", encoding="utf8") as f:
        #     f.write(response.text)

        # "720P"},{"video_url":"(.*?)","quality":"1080P"}
        # ;720P&quot;.*?&quot;video_url&quot;: &quot;<a href="(.*?)"
        m3u8_url = re.findall(
            r'"720P"},{"video_url":"(.*?)","quality":"1080P"}', response.text,
            re.S)[0]
        m3u8_url_list.append(m3u8_url)
        # print(m3u8_list)

    # 将所有页面的视频m3u8的文件保存至一个文件，已追加的形式保存，
    with open(f'{path}\m3u8.txt', mode='a+', encoding='utf-8') as f:
        # 视频可能多个
        i = 0
        for m3u8_url in m3u8_url_list:
            i += 1
            f.write(title)
            f.write(str(i))
            f.write('\n')
            f.write(m3u8_url)
            f.write('\n')
    print(title, '页面的视频的m3u8链接保存至文件！')


# 读取m3u8.txt文件，请求里面的链接将所有的m3u8文件下载下来
def download_m3u8():
    title_list = []
    domain_list = []
    with open(f'{path}\m3u8.txt', mode='r', encoding='utf-8') as f:
        lines = f.readlines()
        # print(lines)
    title = ''
    for line in lines:
        if not line.startswith('http'):
            title = line.strip()
            # print(title,'是文件名')
        else:
            url = line.strip()
            # print(url,'是链接')
            domain_list.append(url.rsplit('/', 1)[0])
            response = session.get(url=url)
            # print(response.text)
            with open(r'{0}\{1}.m3u8'.format(path, title), mode='wb') as f:
                f.write(response.content)
            title_list.append(title)
            print(f'{title_list[-1]}.m3u8文件保存完毕！')
    return title_list, domain_list


# 从title_domain.txt文件中提取所有.m3u8文件名和各自下载ts需要的链接，形成完成链接
def download_all_ts():
    with open(f'{path}\\title_domain.txt', mode='r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            title, domain = line.split('//', 1)
            # print(title,domain)
            if not os.path.exists(r'{0}\{1}'.format(path, title)):
                os.mkdir(r'{0}\{1}'.format(path, title))
            loop = asyncio.get_event_loop()
            loop.run_until_complete(download_m3u8_ts(title, domain))


# 读取单个m3u8文件中的所有视频链接，
async def download_m3u8_ts(title, domain):
    tasks = []
    print(title, '开始下载：')
    async with aiohttp.ClientSession() as session:
        async with aiofiles.open(r'{0}\{1}.m3u8'.format(path, title),
                                 mode='r',
                                 encoding='utf-8') as f:
            async for line in f:
                if line.startswith('#'):
                    continue
                line = line.strip()
                url = domain + '/' + line
                # print(url)
                task = asyncio.create_task(download_ts(url, session, title))
                tasks.append(task)
            await asyncio.wait(tasks)
    print(title, '全部下载over!')


# 下载单个ts文件
async def download_ts(url, session, title):
    name = url.rsplit('/', 1)[-1]
    async with session.get(url=url) as response:
        async with aiofiles.open(r'{0}\{1}\{2}'.format(path, title, name),
                                 mode='wb') as f:
            await f.write(await response.content.read())
    print(name, '下载完成！')


# 将key和IV和title(文件夹名)放到元组里，将所有元组组成列表
def get_list_of_keyIV():
    keyIV_list = []
    with open(f'{path}\\title_domain.txt', mode='r',
              encoding='utf-8') as f:
        for line in f:
            title = line.strip().split('//', 1)[0]
            # print(title)
            key, IV = get_key_IV(title)
            tuple1 = (title, key, IV)
            keyIV_list.append(tuple1)
    print(keyIV_list)
    return keyIV_list


# 解密
async def dec_all_file():
    tasks = []
    keyIV_list = get_list_of_keyIV()
    # 获取协程返回的key和IV
    for tup in keyIV_list:
        async with aiofiles.open(r'%s\%s.m3u8' % (path, tup[0]),
                                 mode='r',
                                 encoding='utf-8') as f:
            async for line in f:
                if line.startswith('#'):
                    continue
                line = line.strip()
                # 开始创建异步任务
                task = asyncio.create_task(dec_ts(tup[0], line, tup[1],
                                                  tup[2]))
                tasks.append(task)
            await asyncio.wait(tasks)
    print('全部解密完成！')


# 获取密钥和偏移量
def get_key_IV(title):
    with open(r'%s\%s.m3u8' % (path, title),
              mode='r',
              encoding='utf-8') as f:
        for line in f:
            list1 = re.findall(r'URI="(.*?)",IV=(.*?)\n', line)
            if len(list1) != 0:
                break
    # print(list1)
    IV = list1[0][1]
    with requests.get(url=list1[0][0]) as response:
        key = response.content
    # print(key,IV)
    return key, IV


# 对单个ts读取并解密，存入新文件
async def dec_ts(title, line, key, IV):
    aes = AES.new(key=key,
                  IV=bytes(IV, encoding='utf-8')[:16],
                  mode=AES.MODE_CBC)  # IV偏移量需要是16位，跟key的位数相同
    title2 = title + str(2)
    if not os.path.exists(r'%s\%s' % (path, title2)):
        os.mkdir(r'%s\%s' % (path, title2))
    async with aiofiles.open(r'%s\%s\%s'%(path, title, line),mode='rb') as f1,\
        aiofiles.open(r'%s\%s\%s'%(path, title2, line), mode='wb') as f2:
        bs = await f1.read()
        await f2.write(aes.decrypt(bs))
    print(title, line, '解密完毕！')


def merge_ts_by_title():
    if not os.path.exists('.\\huawei\\video'):
        os.mkdir('.\\huawei\\video')
    with open(f'{path}\\title_domain.txt', mode='r',
              encoding='utf-8') as f:
        for line in f:
            title = line.split('//', 1)[0]
            # print(title)
            merge_ts(title)


# 合并ts文件
def merge_ts(title):
    # ts_list = []  # 去掉列表，换一种方法

    # 先创建一个空文件，再逐一合并
    target = f'{title}.ts'
    with open(f'{path}\\{title}2\\{title}.ts', mode='wb') as f:
        print(f'{path}\\{title}2\\{title}.ts空文件创建成功')

    with open(r'%s\%s.m3u8' % (path, title),
              mode='r',
              encoding='utf-8') as f:
        for line in f:
            if line.startswith('#'):
                continue
            line = line.strip()
            print(line)
            # print(os.getcwd())
            os.system(f'copy/b "{path}\\{title}2\\{target}"+"{path}\\{title}2\\{line}" "{path}\\{title}2\\{target}"')
    print(f'{target}文件合并成功！')

    # 将合成的文件移动到video文件夹下
    shutil.move(f"{path}\\{title}2\\{target}", r".\huawei\video\%s" % (target))
    print(target, r'已移至E:\Python\huawei\video')

    # with open(r'E:\Python\huawei\%s.m3u8'%(title),mode='r',encoding='utf-8') as f:
    #     for line in f:
    #         if line.startswith('#'):
    #             continue
    #         line = line.strip()
    #         ts_list.append(line)
    # ts_str = '+'.join(ts_list)

    # print(ts_str)
    # 更改系统路径，防止命令行太长
    # os.chdir('E:\\Python\\huawei\\%s2'%(title))
    # 命令行还是太长，此路不通，可以使用迭代器，但我不太会
    # os.system(f'copy/b {ts_str} E:\\Python\\huawei\\video\\{title}.mp4')
    # print(f'E:\\Python\\huawei\\video\\{title}.mp4合成成功！')


def main():
    # 创建临时文件夹暂时保存文件，下载完后删除
    if not os.path.exists(path):
        os.makedirs(path)

    # url = 'https://ilearningx.huawei.com/courses/course-v1:HuaweiX+20ESHZCLC038+21ZNJZ050/courseware/3a0cc426426c4b7487dab1811b370878/a46fbbfc834549e7bc5be8bf13b9fcaa/'
    url = input('输入网址：')
    # # 获取目录页的某个页面的源代码，源代码有所有子页面的网址链接
    save_source(url, "orgin")

    # 获取所有子页面的标题，并保存子页面的页面源代码到文件
    title_list = get_page_url()
    # 将所有子页面的文件名保存到文件中
    with open(f'{path}\\titles.txt', mode='w', encoding='utf-8') as f:
        for title in title_list:
            f.write(title + '\n')

    # 获取所有视频的m3u8文件的链接，存入m3u8.txt文件中
    with open(f'{path}\\titles.txt', mode='r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()  # 去除回车
            # 获取存有video_id的列表
            video_id_list = get_video_id(line)
            if len(video_id_list) == 0:  # 如果video_id_list为空，说明该页面没有视频，跳过
                continue
            # 通过video_id获取m3u8文件地址，并保存至文件中
            get_m3u8_url(line, video_id_list)

    # 读取m3u8.txt文件，请求里面的链接将所有的m3u8文件下载下来，返回m3u8的文件名列表
    title_list, domain_list = download_m3u8()
    # 将所有m3u8的文件名保存到title.txt文件中
    with open(f'{path}\\title_domain.txt', mode='w', encoding='utf-8') as f:
        i = 0
        for title in title_list:
            f.write(title)
            f.write('//')
            f.write(domain_list[i])
            f.write('\n')
            i += 1
    print('title_domain.txt保存完毕！')

    # 通过每个.m3u8把切片的ts视频下载下来
    download_all_ts()  # 漫长的等待

    # # 解密
    # loop = asyncio.get_event_loop()
    # loop.run_until_complete(dec_all_file())

    # # 合并ts文件，并移动至video文件夹
    # merge_ts_by_title()

    # # 删除temp临时文件夹
    # if os.path.exists(path):
    #     shutil.rmtree(path)


if __name__ == '__main__':
    main()