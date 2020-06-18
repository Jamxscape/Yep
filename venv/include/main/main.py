from PIL import Image
import pytesseract
import excel
import os
import io
import locale
locale.setlocale(locale.LC_ALL, 'C')
import tesserocr
import GetData
import sys
import CreateHtml

if __name__ == '__main__':
    # 识别汉字的 pytesteract
    image_path = "../testImg/test1.png"
    print("《《《《《《《《《正在打开图片》》》》》》》》》》》》")
    image = Image.open(image_path)
    # code = pytesseract.image_to_string(image, lang="chi_sim")
    # #print(code)
    # complexCode = pytesseract.image_to_boxes(image, lang="chi_sim")
    #print(complexCode)
    print("《《《《《《《《正在将图片转化为data对象》》》》》》》")
    ImageToData = pytesseract.image_to_data(image, lang="chi_sim")
    #print(ImageToData)
    print("《《《《《《《《图片识别如下》》》》》》》》》》》》")
    print(ImageToData)#输出object的类型
    # output = pytesseract.Output()
    #print(output)
    #每一种字体的识别

    #写入Excel中
    path = "../excel/"
    book_name_xls = "ImageToData.xls" # 文件名
    sheet_name_xls = "sheet1" # 表格名
    # value_title = [["level","page_num","block_num","par_num","line_num","word_num","left","top","width","height","conf","text"],]
    excel.write_excel_xls(path+book_name_xls,sheet_name_xls) # 创建文件成功
    print("《《《《《《《《《ImageToData.xls生成成功》》》》》》》")
    excel.write_excel_xls_append(path+book_name_xls,ImageToData)
    #从Excel中读取数据
    #创建源文件
    dir_name_CSS = "../source/css"
    if not os.path.isdir(dir_name_CSS):
        os.makedirs(dir_name_CSS)
        print("CSS文件夹生成")
    dir_name_HTML = "../source/html"
    if not os.path.isdir(dir_name_HTML):
        os.makedirs(dir_name_HTML)
        print("HTML文件夹生成")
    dir_name_JS = "../source/js"
    if not os.path.isdir(dir_name_JS):
        os.makedirs(dir_name_JS)
        print("JS文件夹生成")

    """
    以下都是写入CSS文件
    识别文字的大小
    识别文字大小根据width和height求出面积，先计算
    识别层次逐层降低
    """
    # print(os.getcwd()) 获取当前的位置
    print("《《《《《《正在对生成的数据进行处理》》》》》》")
    CSS_text = GetData.get_data_in_excel(image_path)
    print("《《《《《《数据处理完毕》》》》》》》》》》》》》")
    os.chdir('../source/css') # 改变路径
    css_file_name = 'test.css'
    print("《《《《《《《《正在生成CSS文件》》》》》》》》》")
    css_file = open(css_file_name, "w")
    print("《《《《《《《《正在将数据写入CSS文件中》》》》》")
    css_file.write(CSS_text)
    # 生成HTML文件
    os.chdir('../../main') # 改变路径
    html_text = CreateHtml.create_html()
    os.chdir('../source/html')
    html_file_name = "test.html"
    print("《《《《《《《《正在生成HTML文件》》》》》》》》》")
    html_file = open(html_file_name, "w")
    print("《《《《《《《《正在将数据写入HTML文件》》》》》》》》》")
    html_file.write(html_text)
    print("《《《《《《《《源代码已经生成》》》》》》》》》")
