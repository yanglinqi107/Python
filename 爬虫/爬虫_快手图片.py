import requests
import time
# from lxml import etree
# url = "https://live.kuaishou.com/u/3xdx9gthpdguqxg/3x6tsw2m8twzi8k?did=web_eba95d7c7b07743262acd89b354329a7"
# headers = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36 HBPC/11.0.7.301"
# }
# resp = requests.get(url = url, headers = headers)
# resp.close()
# # print(resp.text)

# html = etree.HTML(resp.text)
# result = html.xpath('//*[@id="app"]/div[1]/div/div[2]/div[1]/div[1]/div[2]/img/@src')
# print(result)

for i in range(0, 15):
    url = "https://tx2.a.kwimgs.com/ufile/atlas/NTIzOTM3NTI3OTg1MjczMjIxNF8xNjM2MzQ1MDM4MDQw_" + str(i) + ".webp"
    print(url)
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36 HBPC/11.0.7.301"
    }
    img_resp = requests.get(url = url, headers = headers)
    img_resp.close()
    img_name = url.split('/')[-1]
    with open('img/' + img_name, mode='wb') as f:
        f.write(img_resp.content)
    print("over!")
    time.sleep(1)

print('over!!!')