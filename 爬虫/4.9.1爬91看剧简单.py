# 将ts文件合并，可以在终端输入copy/b E:\xxxxx\*.ts E:\new.ts

import requests
import re
import aiohttp
import aiofiles
import asyncio

# url = "https://www.91kanju2.com/vod-play/54812-1-1.html"
# resp = requests.get(url = url)
# resp.close()
# # print(resp.text)
# obj = re.compile(r"url: '(?P<m3u8>.*?)'",re.S)
# url_m3u8 = obj.findall(resp.text)[0]
# # print(url_m3u8)
# m3u8 = requests.get(url = url_m3u8)
# m3u8.close()
# # print(m3u8.text)
# with open("sources/哲仁王后.m3u8", mode="wb") as f:
#     f.write(m3u8.content)
# print("over!")

# with open('sources/哲仁王后.m3u8',mode='r',encoding="utf-8") as f:
#         num = 1
#         for line in f:
#             line = line.strip()     #去空格和换行符
#             if line.startswith("#"):
#                 continue
#             ts_resp = requests.get(line)
#             ts_resp.close()
#             n = str(num).rjust(4,'0')
#             fw = open(f'sources/video/{n}.ts',mode="wb")
#             fw.write(ts_resp.content)
#             fw.close()
#             ts_resp.close()
#             print(n,"完成！")
#             num += 1
# print("over!")

async def download():
    num = 1
    tasks = []
    async with aiohttp.ClientSession() as session:
        async with aiofiles.open('sources/哲仁王后.m3u8',mode='r',encoding="utf-8") as f:
            async for line in f:
                if line.startswith("#"):
                    continue
                line = line.strip()     #去空格和换行符
                n = str(num).rjust(4,'0')
                tasks.append(asyncio.create_task(downloadTs(line, n, session)))
                num = num + 1
            await asyncio.wait(tasks)
    print("over!")

async def downloadTs(line, n, session):
    async with session.get(url = line) as ts_resp:
        async with aiofiles.open(f'爬虫/video/{n}.ts',mode="wb") as fw:
            await fw.write(await ts_resp.content.read())    # 必须用ts_resp.content.read()
    print(n,"完成")

if __name__ == '__main__':
    asyncio.run(download())

