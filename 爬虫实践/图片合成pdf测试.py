import glob
import os
import fitz  # pip install PyMuPDF


def pic2pdf(img_dir):
    doc = fitz.open()
    for img in sorted(glob.glob("{}/*".format(img_dir))):  # 读取图片，确保按文件名排序
        print(img)
        imgdoc = fitz.open(img)  # 打开图片
        pdfbytes = imgdoc.convertToPDF()  # 使用图片创建单页的 PDF
        imgpdf = fitz.open("pdf", pdfbytes)
        doc.insertPDF(imgpdf)  # 将当前页插入文档
    if os.path.exists(f"{img_dir}\\allimages.pdf"):
        os.remove(f"{img_dir}\\allimages.pdf")
    doc.save(f"{img_dir}\\allimages.pdf")  # 保存pdf文件
    doc.close()


if __name__ == '__main__':
    img_dir = "E:\\Python\\百度文库"
    pic2pdf(img_dir)

