import asyncio

# async def func():
#     print("hello world!")

# if __name__ == '__main__':
#     g = func()
#     #  print(g)
#     asyncio.run(g)

async def request(url):
    print('正在请求的URL是',url)
    print('请求成功',url)
    return url
# async修饰的函数，调用之后返回一个协程对象
c = request('www.baidu.com')

# # 创建一个时间循环对象
# loop = asyncio.get_event_loop()
# # 将协程对象注册到loop中，启动loop
# loop.run_until_complete(c)

# # task的使用
# loop = asyncio.get_event_loop()
# # 基于loop创建了一个task对象
# task = loop.create_task(c)
# print(task)
# loop.run_until_complete(task)
# print(task)

# # future的使用
# loop = asyncio.get_event_loop()
# task = asyncio.ensure_future(c)
# print(task)
# loop.run_until_complete(task)
# print(task)

def callback_func(task):
    print(task.result())
# 绑定毁掉
loop = asyncio.get_event_loop()
task = asyncio.ensure_future(c)
# 将回调函数绑定到任务对象中
task.add_done_callback(callback_func)
loop.run_until_complete(task)



