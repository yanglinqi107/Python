import requests

url = "https://www.pearvideo.com/video_1744481"

contId = url.split('_')[1]

video_url = f"https://www.pearvideo.com/videoStatus.jsp?contId={contId}&mrd=0.6819059715349529"   #  mrd是个随机数，无所谓

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36 Edg/95.0.1020.44",
    #防盗链 溯源 本次请求的上一级是谁
    "Referer": url  #"https://www.pearvideo.com/video_1744481"
}

resp = requests.get(url = video_url, headers = headers)
resp.close()
#print(resp.json())
dic = resp.json()
srcUrl = dic['videoInfo']['videos']["srcUrl"]
systemTime = dic["systemTime"]

srcUrl = srcUrl.replace(systemTime, f'cont-{contId}')
# print(srcUrl)
resp = requests.get(url = srcUrl)
resp.close()
# 下载视频
with open('爬虫/video/a.mp4',mode='wb') as f:
    f.write(resp.content)
print("over!!!")