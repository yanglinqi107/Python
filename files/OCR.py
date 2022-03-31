# # 导入easyocr
# import easyocr
# # 创建reader对象
# reader = easyocr.Reader(['ch_sim']) 
# # 读取图像
# result = reader.readtext('E:\\Python\\sources\\OCR.png')
# # 结果
# print(result)
# # import pytesseract

# import pytesseract
# from PIL import Image

# def image_handle():
#     # image = Image.open('E:\Python\sources\OCR.png')
#     image = Image.open('E:\\code.png')
#     image.convert("L")
#     text = pytesseract.image_to_string(image, lang='eng')
#     print(text)

# if __name__ == '__main__':
#     image_handle()

"""
超级鹰识别正常
"""
from chaojiying_Python.chaojiying import Chaojiying_Client
import requests
# img = Image.open('E:\\OCR.png')
# print(type(img))  
"""TypeError: a bytes-like object is required, not 'PngImageFile'"""

url = 'http://www.diyibanzhuvip9.xyz/toimg/data/4820521578.png'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36 HBPC/11.0.8.300'
}
response = requests.get(url, headers=headers)
response.close()
img = response.content
print(type(img))
# with open('E:\\OCR.png', mode='rb') as f:
#     img = f.read()
chaojiying = Chaojiying_Client('', '', '')		
dic = chaojiying.PostPic(img, 2001)
verify_code = dic['pic_str']   
print(verify_code)
