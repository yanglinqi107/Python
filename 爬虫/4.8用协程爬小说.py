import requests
import aiohttp
import asyncio
import json
import aiofiles


# title_url = 'http://dushu.baidu.com/api/pc/getCatalog?data={"book_id":"4306063500"}'  #章节名称，cid
# content_url = 'http://dushu.baidu.com/api/pc/getChapterContent?data={"book_id":"4306063500","cid":"4306063500|11348571","need_bookinfo":1}'

async def getCatalog(b_id):
    url = 'http://dushu.baidu.com/api/pc/getCatalog?data={"book_id":"'+b_id+'"}'
    resp = requests.get(url = url)
    resp.close()
    # print(resp.text)
    tasks = []
    dic = resp.json()
    for item in dic['data']['novel']['items']:   #item对应每个章节的名称和cid
        title = item['title']
        cid = item['cid']
        # print(cid,title)
        tasks.append(asyncio.create_task(aiodownload(cid, b_id, title)))
    await asyncio.wait(tasks)

async def aiodownload(cid, book_id, title):
    data = {
        "book_id":book_id,
        "cid":f'{book_id}|{cid}',
        "need_bookinfo":1
    }
    data = json.dumps(data)
    url = f'http://dushu.baidu.com/api/pc/getChapterContent?data={data}'
    async with aiohttp.ClientSession() as session:
        async with session.get(url = url) as resp:
            dic = await resp.json()
            async with aiofiles.open(f"sources/{title}.txt",mode = 'w',encoding = 'utf-8') as f:
                await f.write(dic['data']['novel']['content'])        #把内容写进去

if __name__ == '__main__':
    b_id = "4306063500"
    asyncio.run(getCatalog(b_id))