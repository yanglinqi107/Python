# import requests


# url = 'https://wenku.baidu.com/view/e98449101b5f312b3169a45177232f60dccce70e.html'
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36 Edg/95.0.1020.53'
# }
# response = requests.get(url=url, headers=headers)
# print(response.content)


from fpdf import FPDF

pdf = FPDF()

#加一页
pdf.add_page()

#设置字体的大小和字体
pdf.set_font('Arial', size=15)

#加一个单元
pdf.cell(200, 10, txt='hello world', ln=1, align='C')

#加一个新的单元格
pdf.cell(200, 10, txt='this is a article.', ln=2, align='C')

pdf.output('test.pdf')
