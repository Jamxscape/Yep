# 导入相关的库
from PIL import Image

def image_crop(path, left, top, right, bottom, save_image_name):
    # 打开一张图
    img = Image.open(path)
    # print(img.size)
    # 开始截取
    region = img.crop((left, top, right, bottom,))
    # 保存图片
    region.save(save_image_name)

# left = 414
# top = 1358
# right = 414
# bottom = 2141
# path = "../testImg/test7.png"
# image_crop(path, left, top, right, bottom, "saveImg/123.png")
