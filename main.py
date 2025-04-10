# python pdf电子相册
# 图像操作 PIL
# reportlab
# 目录文件的遍历
# 图像嵌入pdf的坐标计算
# os

import PIL
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import landscape
import os


def genpdf(filename,pagesizes):
    pdf = canvas.Canvas(filename)
    pdf.setPageSize(pagesizes)
    return pdf


def save_img_to_pdf(pdf, image, x, y, w, h):
    pdf.drawImage(image, x, y, w, h)
    pdf.showPage()


if __name__ == '__main__':
    pdf_size = (1920,1080)
    my_pdf = genpdf("my_album.pdf",pdf_size)

# 遍历文件夹 读取文件夹下的照片
    folder = "imgs"
    filelist = os.listdir(folder)
    for filename in filelist:
        img = PIL.Image.open(os.path.join(folder,filename))   #folder+"/"+filename
        img_w,img_h = img.size
        img_x = (landscape(pdf_size)[0] - img_w) / 2
        img_y = (landscape(pdf_size)[1] - img_h) / 2

        save_img_to_pdf(my_pdf,os.path.join(folder,filename),x = img_x,y = img_y,w = img_w,h = img_h)
        print("image"+ str(filename)+" saved")

    my_pdf.save()

