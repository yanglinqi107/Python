import requests
import aiohttp
import aiofiles
import asyncio
from Crypto.Cipher import AES  
import os

def download_m3u8():
    url = "https://v7.dious.cc/20210926/TX2fGLGH/1000kb/hls/index.m3u8"
    resp = requests.get(url = url)
    resp.close()
    # print(resp.text)
    with open("sources/失控玩家.m3u8",mode="wb") as f:
        f.write(resp.content)
    print("over!")

"""
timeout = aiohttp.ClientTimeout(total=600)  # 将超时时间设置为600秒
connector = aiohttp.TCPConnector(limit=50)  # 将并发数量降低

async with aiohttp.ClientSession(connector=connector, timeout=timeout) as session:
    async with session.get(url[0], headers=headers) as response:
"""

async def download():
    name = 100001
    tasks = []
    timeout = aiohttp.ClientTimeout(total=600)  # 将超时时间设置为600秒
    connector = aiohttp.TCPConnector(limit=50)  # 将并发数量降低

    async with aiohttp.ClientSession(connector=connector, timeout=timeout) as session:
    # async with aiohttp.ClientSession() as session:
        async with aiofiles.open('sources/失控玩家.m3u8',mode='r',encoding="utf-8") as f:
            async for line in f:
                if line.startswith("#"):
                    continue
                line = line.strip()     #去空格和换行符
                tasks.append(asyncio.create_task(downloadTs(line, name, session)))
                name += 1
            await asyncio.wait(tasks)
    print("over!")

async def downloadTs(line, name, session):
    async with session.get(url = line) as ts_resp:
        async with aiofiles.open(f'爬虫/video/{name}.ts',mode="wb") as fw:
            await fw.write(await ts_resp.content.read())    # 必须用ts_resp.content.read()
    print(name,"完成")

# key:4cf800bdca8898b8

async def dec_ts(name, key):
    aes = AES.new(key=key, IV=b"0000000000000000", mode=AES.MODE_CBC)
    async with aiofiles.open(f"爬虫/video/{name}.ts", mode="rb") as f1,\
        aiofiles.open(f"sources/video/dec_{name}.ts", mode="wb") as f2:
    
        bs = await f1.read()  # 从源文件读取内容
        await f2.write(aes.decrypt(bs))  # 把解密好的内容写入文件
    print(f"{name}处理完毕")

async def aio_dec(key):
    # 解密
    tasks = []
    last = 101860
    for name in range(100001,last):
        # 开始创建异步任务
        task = asyncio.create_task(dec_ts(name, key))
        tasks.append(task)
        name += 1
    await asyncio.wait(tasks)

def merge_ts():
    # mac: cat 1.ts 2.ts 3.ts > xxx.mp4
    # windows: copy /b 1.ts+2.ts+3.ts xxx.mp4
    lst = []
    for name in range(100001,101860):
        lst.append(f"sources/video/dec_{name}.ts")
    s = "+".join(lst)  # 1.ts 2.ts 3.ts
    os.system(f"copy/b {s} movie.mp4")
    print("搞定!")

# 单步
def downloadTs_bystep():
    with open('sources/失控玩家.m3u8',mode='r',encoding="utf-8") as f:
            n = 100001
            for line in f:
                line = line.strip()     #去空格和换行符
                if line.startswith("#"):
                    continue
                ts_resp = requests.get(line)
                ts_resp.close()
                fw = open(f'爬虫/video2/{n}.ts',mode="wb")
                fw.write(ts_resp.content)
                fw.close()
                print(n,"完成！")
                n += 1
    print("over!")

if __name__ == '__main__':
    # asyncio.get_event_loop().run_until_complete(download())
    # key = "4cf800bdca8898b8"
    # asyncio.run(aio_dec(key))
    # merge_ts()
    # downloadTs_bystep()



    