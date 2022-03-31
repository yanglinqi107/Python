import requests

# proxies={"http":"http://118.135.217.7:80"}
proxies={"http":"http://183.247.199.215"}

try:
    result = requests.get('https://blog.csdn.net/tingfenyijiu/article/details/77937481', proxies=proxies)
    print(result)
    print(result.text)
except:
    print('connect failed')
else:
    print('success')


# # 修改事件循环的策略，不能放在协程函数内部，这条语句要先执行
# import asyncio

# import aiohttp


# async def func():
#     # 添加trust_env=True
#     async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(ssl=False), trust_env=True) as session:
#         try:
#             async with session.get("https://httpbin.org/ip", proxy='http://183.220.145.3:80', timeout=10) as response:
#                 page_text = await response.text()
#                 print(page_text)
#                 print('success')
#         except Exception as e:
#             print(e)
#             print('error')
# if __name__ == '__main__':
#     asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
#     asyncio.get_event_loop().run_until_complete(func())


import aiohttp
import asyncio
import threading
# from tools import auto
asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy()) # 加上这一行
# proxy=auto.proxies, proxy_auth=auto.proxy_auth 这里的代理需要换成自己的
async def quest(url,  headers):
    con = aiohttp.TCPConnector(ssl=False)
    async with aiohttp.ClientSession(connector=con, trust_env=True) as sess: # 加上trust_env=True
        async with sess.get(url=url, headers=headers, proxy='http://183.247.199.215') as res:
            return await res.read()


def forever(loop):
    asyncio.set_event_loop(loop)
    loop.run_forever()


if __name__ == '__main__':
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:79.0) Gecko/20100101 Firefox/79.0'}
    url = 'http://baidu.com'

    loop = asyncio.new_event_loop()
    t = threading.Thread(target=forever, args=(loop,))
    t.setDaemon(True)
    t.start()
    ret = asyncio.run_coroutine_threadsafe(quest(url, headers), loop)
    print(ret.result())
