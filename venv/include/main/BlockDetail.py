from PIL import Image
import pytesseract
import excel
import os
import io
import locale
locale.setlocale(locale.LC_ALL, 'C')
import tesserocr
from PIL import Image
# from tesserocr import PyTessBaseAPI, RIL, iterate_level

def block_detail(path, left, top, right, bottom):
    with tesserocr.PyTessBaseAPI(lang='chi_sim+eng') as api:
        api.SetImageFile(path)
        api.SetVariable("save_blob_choices", "T")
        # api.SetRectangle(left, top, right, bottom)
        api.SetRectangle(left, top, (right-left)*0.9, (bottom-top)*0.9)
        # print("执行过1")
        api.Recognize()
        # print("执行过2")
        iterator = api.GetIterator()
        # print("执行过3")
        # print(api.GetUTF8Text()) # 识别的具体文字，但是这个并不精准
        #vprint(iterator.RowAttributes()) # 每一行的具体信息 这个对结果无意义
        dic = iterator.WordFontAttributes()
        print(dic)
        if dic is None:
            return '/* 检测出错 */'
        else:
            new_dict = ''
            if not dic['serif']:
                new_dict = "font-family: " + dic["font_name"]
            else:
                serif = 'serif'
                new_dict = "font-family: " + dic["font_name"] + ',' + serif
            if not dic['monospace']:
                new_dict = new_dict + ";\n"
            else:
                new_dict = new_dict + "," + "monospace;\n"
            if not dic['bold']:
                new_dict = new_dict + "font-weight: " + "normal;\n"
            else:
                new_dict = new_dict + "font-weight: " + "bold;\n"
            if not dic['italic']:
                new_dict = new_dict + "font-style: " + "normal;\n"
            else:
                new_dict = new_dict + "font-style: " + "italic;\n"
            if not dic['smallcaps']:
                new_dict = new_dict + "font-variant: " + "normal;\n"
            else:
                new_dict = new_dict + "font-variant: " + "small-caps;\n"
            if not dic['underlined']:
                new_dict = new_dict + "text-decoration: " + 'none;\n'
            else:
                new_dict = new_dict + "text-decoration: " + "underline;\n"
            new_dict = new_dict + "font-size: " + str(dic['pointsize']/5) + ';'
            return  new_dict


"""
最后返回结果 是对每一个块的整合
{'font_name': 'Arial_Unicode_MS',  字体
'bold': False,  加粗
'italic': False,  斜体
'underlined': False,  下划线
'monospace': False,  等宽字体
'serif': False,  有衬线字体
'smallcaps': False,  
'pointsize': 16,  字号
'font_id': 351}  字体id
# """
# path = "../testImg/test5.png"
# # # path2 = "saveImg/page1blk1par1.png"
# print(block_detail(path, 527.0, 254.0, 1200, 1200.0))

# def get_font(image_path):
#     with PyTessBaseAPI() as api:
#         api.SetImageFile(image_path)
#         api.Recognize()
#         ri = api.GetIterator()
#         level = RIL.SYMBOL
#
#         for r in iterate_level(ri, level):
#             symbol = r.GetUTF8Text(level)
#             word_attributes = r.WordFontAttributes()
#
#             if symbol:
#                  print(u'symbol {}, font: {}'.format(symbol, word_attributes['font_name']))
#
# get_font('logo.jpg')
