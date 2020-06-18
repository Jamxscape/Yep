# coding=UTF-8
import xlrd
import xlwt
from xlutils.copy import copy
import openpyxl
import re


def is_number(s):
    """
    判断是否为数字的函数
    """
    try:
        float(s)
        return True
    except ValueError:
        pass
    #
    # try:
    #     import unicodedata
    #     unicodedata.numeric(s)
    #     return True
    # except (TypeError, ValueError):
    #     pass

    return False


def write_excel_xls(path, sheet_name):
    #index = len(value)  # 获取需要写入数据的行数
    workbook = xlwt.Workbook()  # 新建一个工作簿
    sheet = workbook.add_sheet(sheet_name)  # 在工作簿中新建一个表格
    workbook.save(path)  # 保存工作簿
    # print("xls格式表格创建成功！")


def write_excel_xls_append(path, value):
    row_excel = 0
    start_col = 0
    workbook = xlrd.open_workbook(path)  # 打开工作簿
    sheets = workbook.sheet_names()  # 获取工作簿中的所有表格
    worksheet = workbook.sheet_by_name(sheets[0])  # 获取工作簿中所有表格中的的第一个表格
    # rows_old = worksheet.nrows  # 获取表格中已存在的数据的行数
    new_workbook = copy(workbook)  # 将xlrd对象拷贝转化为xlwt对象
    new_worksheet = new_workbook.get_sheet(0)  # 获取转化后工作簿中的第一个表格

    line = re.split('\n|\t',value) #根据制表符\t和换行符\n分割成每一个单元
    line_num = int(len(line)/12) # 获取返回值的行数，这是由于无法转化成二维数组，只能作中间转换
    for i in range(0, line_num):
        col_excel = start_col
        if len(str(line[i * 12 + 11])) == 0 or line[i * 12 + 11].isspace(): # 监测text是否为空或者空格，为得是最后只得到字符不为空的字符
            pass
        else:
            for j in range(0, 12):
                # print(line[j])
                index = i * 12 + j
                if is_number(line[index]): # 判断是否为数字
                    data = int(line[index])
                else:
                    data = line[index]
                new_worksheet.write(row_excel, col_excel, data)
                col_excel += 1
                new_workbook.save(path)
            row_excel += 1
    # print("xls格式表格【追加】写入数据成功！")


def read_excel_xls(path, row, col):
    workbook = xlrd.open_workbook(path)  # 打开工作簿
    sheets = workbook.sheet_names()  # 获取工作簿中的所有表格
    worksheet = workbook.sheet_by_name(sheets[0])  # 获取工作簿中所有表格中的的第一个表格
    #for i in range(0, worksheet.nrows):
    #for j in range(0, worksheet.ncols):
    return worksheet.cell_value(row, col)  # 逐行逐列读取数据

def get_excel_rows(path):
    excel = xlrd.open_workbook(path)
    table = excel.sheet_by_name('sheet1')  # 通过表名获取
    rows = table.nrows
    return rows

def write_excel_xls_row_append(path, row, col, value):
    workbook = xlrd.open_workbook(path)  # 打开工作簿
    sheets = workbook.sheet_names()  # 获取工作簿中的所有表格
    worksheet = workbook.sheet_by_name(sheets[0])  # 获取工作簿中所有表格中的的第一个表格
    rows_old = worksheet.nrows  # 获取表格中已存在的数据的行数
    new_workbook = copy(workbook)  # 将xlrd对象拷贝转化为xlwt对象
    new_worksheet = new_workbook.get_sheet(0)  # 获取转化后工作簿中的第一个表格

    new_worksheet.write(row, col, value)
    new_workbook.save(path)


