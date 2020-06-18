import os
import stat
from CSS.CSS_Position import *
import excel
import ImageToData
import ImageCrop
import BlockDetail
import shutil
from PIL import Image

def get_data(path_image):
    path = "../excel/"
    book_name_xls = "ImageToData.xls"  # 文件名
    open(path + book_name_xls)
    line_count = 2  # 从第二行有数字的开始
    page_num = 1
    block_num = 1
    par_num = 1
    left = ImageToData.left(line_count)
    top = ImageToData.top(line_count)
    width = ImageToData.width(line_count)
    height = ImageToData.height(line_count)
    text = ImageToData.text(line_count)
    # class_name = 'page' + str(page_num) + 'blk' + str(block_num) + 'par' + str(par_num)  # 要在这儿重新加一个命名系统
    result_book_name_xls = "result.xls"  # 文件名
    result_sheet_name_xls = "sheet1"  # 表格名
    value_title = ["class_name", "position", "left", "top", "font", "text"]
    excel.write_excel_xls(path + result_book_name_xls, result_sheet_name_xls)  # 创建文件成功
    result_row = 1  # 书写文字的行
    result_col = 0  # 列
    for i in range(0, 6):
        excel.write_excel_xls_row_append(path + result_book_name_xls, 0, result_col, value_title[i])
        result_col = result_col + 1
    image_to_data_rows = excel.get_excel_rows(path + book_name_xls)  # 获取ImageTOData最大行数
    result_left = left # 左边最小值
    result_top = top # 上边最大值
    result_right = left # 左边最大值
    result_bottom = top # 上边最大值
    result_text = ""
    while line_count <= image_to_data_rows:  # level值为空时，获取结束
        result_col = 0  # 列置0，重新每行写入
        if ImageToData.page_num(line_count) == page_num:  # 检查同一页面内文字
            if ImageToData.block_num(line_count) == block_num:  # 检查同一块的文字
                if ImageToData.par_num(line_count) == par_num:  # 检查同一段落的文字
                    text = ImageToData.text(line_count)
                    if text.encode( 'UTF-8' ).isalpha():  # 如果字符串是英文，则应该加空格
                        text += " "
                    result_text = result_text + text
                    left = ImageToData.left(line_count) # 取最小的左边
                    top = ImageToData.top(line_count) # 取最小的上边
                    if result_left > left:
                        result_left = left
                    if result_right < left:
                        result_right = left
                        width = ImageToData.width(line_count)
                    if result_top > top:
                        result_top = top
                    if result_bottom < top:
                        result_bottom = top
                        height = ImageToData.height(line_count)
                    line_count = line_count + 1
                else:
                    if width == 0: # 当这一部分为一行时，width获取会为零，因此要重新定位width的值
                        width = ImageToData.width(line_count - 1)
                    if height == 0:
                        height = ImageToData.height(line_count - 1)
                    write_data(path_image, page_num, block_num, par_num, path +
                                result_book_name_xls, result_row, result_col,
                                result_left, result_top, width + result_right, height + result_bottom, result_text)
                    result_row = result_row + 1
                    result_left = ImageToData.left(line_count)
                    result_top = ImageToData.top(line_count)
                    result_right = result_left
                    result_bottom = result_top
                    par_num = ImageToData.par_num(line_count)
                    width, height,result_text = reset()
            else:
                if width == 0:
                    width = ImageToData.width(line_count - 1)
                if height == 0:
                    height = ImageToData.height(line_count - 1)
                write_data(path_image, page_num, block_num, par_num, path + result_book_name_xls,
                            result_row, result_col, result_left, result_top,  width + result_right,
                           height + result_bottom, result_text)
                result_row = result_row + 1
                result_left = ImageToData.left(line_count)
                result_top = ImageToData.top(line_count)
                result_right = result_left
                result_bottom = result_top
                block_num = ImageToData.block_num(line_count)
                width, height, result_text = reset()
        else:
            if width == 0:
                width = ImageToData.width(line_count - 1)
            if height == 0:
                height = ImageToData.height(line_count - 1)
            write_data(path_image, page_num, block_num, par_num, path + result_book_name_xls,
                        result_row, result_col, result_left, result_top,  width + result_right,
                       height + result_bottom, result_text)
            result_row = result_row + 1
            result_left = ImageToData.left(line_count)
            result_top = ImageToData.top(line_count)
            result_right = result_left
            result_bottom = result_top
            page_num = ImageToData.page_num(line_count)
            width, height, result_text = reset()
    if width == 0:
        width = ImageToData.width(line_count-1)
    if height == 0:
        height = ImageToData.height(line_count-1)
    write_data(path_image, page_num, block_num, par_num, path + result_book_name_xls,
               result_row, result_col, result_left, result_top,  width + result_right,
               height + result_bottom, result_text)


def write_data(path_image, page_num, block_num, par_num, path, result_row,
               result_col, left, top, right, bottom, result_text):
    class_name = 'page' + str(int(page_num)) + 'blk' + str(int(block_num)) + 'par' + str(int(par_num))
    excel.write_excel_xls_row_append(path, result_row, result_col, class_name)
    result_col = result_col + 1 # 游标移动到position列
    c = CSSPosition("position", CSSPosition.CSSPositionValue[0])
    excel.write_excel_xls_row_append(path, result_row, result_col, c.write() + ";\n")
    result_col = result_col + 1 # 游标移动到position列
    excel.write_excel_xls_row_append(path, result_row, result_col, "left: " + str(left/0.8) + ";\n" + "right: " + str(right/5.5) + ";\n")
    result_col = result_col + 1 # 游标移动到position列
    excel.write_excel_xls_row_append(path, result_row, result_col, "top: " + str(top/4) + ";\n" )
    # + "bottom: " + str(bottom/4) + ";\n"
    result_col = result_col + 1  # 游标移动到position列
    # 对源图片进行分块切割
    print("这", class_name, "个块的具体位置为", "左:",left, "上：",top, "右：",right, "底", bottom)
    ImageCrop.image_crop(path_image, left, top, right, bottom, "saveImg/" + class_name +".png")
    print("《《《《《《正在执行低版本tesseract》》》》》》》")
    copy_file("../tessdata/tessdata-3.04.00")
    print("《《《《《《《正在识别这一模块的详细数据》》》》》")
    excel.write_excel_xls_row_append(path, result_row, result_col, BlockDetail.block_detail(path_image,
                                                                                            left, top, right, bottom))
    copy_file("../tessdata/tessdata-4.0.0")
    result_col = result_col + 1  # 游标移动到position列
    excel.write_excel_xls_row_append(path, result_row, result_col, result_text)


def reset():
    width = 0
    height = 0
    result_text = ""
    return width, height, result_text

def get_data_in_excel(path_image):# 生成CSS文件
    CSS_Text = "@charset \"UTF-8\";\n/* CSS Document */\n"
    get_data(path_image)
    print("result.xls生成")
    path_excel = "../excel/result.xls"
    line_count = 2  # 行数
    result_rows = excel.get_excel_rows(path_excel)  # 获取result.xls最大行数
    while line_count <= result_rows:
        CSS_Text += '.'
        CSS_Text += excel.read_excel_xls(path_excel, line_count - 1, 0) + '{\n'
        CSS_Text += excel.read_excel_xls(path_excel, line_count - 1, 1)
        CSS_Text += excel.read_excel_xls(path_excel, line_count - 1, 2)
        CSS_Text += excel.read_excel_xls(path_excel, line_count - 1, 3)
        CSS_Text += excel.read_excel_xls(path_excel, line_count - 1, 4) + "\n}\n"
        line_count += 1
    return CSS_Text


def copy_file(dir_name): # 输出文件夹下，每一个文件的名称
    for main_dir, subdir, file_name_list in os.walk(dir_name):
        for file_name in file_name_list:
            path_file = os.path.join(main_dir, file_name)#合并成一个完整路径
            shutil.copy(path_file, r'/usr/local/Cellar/tesseract/4.1.1/share/tessdata')
            # # 将其复制到tessdata数据的文件夹下
            # print(path_file) # 监测

# dirname = "../tessdata/tessdata-3.04.00"
# all_path(dirname)

# print(get_data_in_excel("../testImg/test6.png"))
# CSS_text = get_data_in_excel("../testImg/test7.png")
# os.chdir('../source/css') # 改变路径
# css_file_name = 'test.css'
# css_file = open(css_file_name, "w")
# css_file.write(CSS_text)
