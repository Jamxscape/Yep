import excel

path = "../excel/"
book_name_xls = "ImageToData.xls"  # 文件名


def level(i):
    return excel.read_excel_xls(path + book_name_xls, i-1, 0)


def page_num(i):
    return excel.read_excel_xls(path + book_name_xls, i-1, 1)


def block_num(i):
    return excel.read_excel_xls(path + book_name_xls, i-1, 2)


def par_num(i):
    return excel.read_excel_xls(path + book_name_xls, i-1, 3)


def line_num(i):
    return excel.read_excel_xls(path + book_name_xls, i-1, 4)


def word_num(i):
    return excel.read_excel_xls(path + book_name_xls, i-1, 5)


def left(i):
    return excel.read_excel_xls(path + book_name_xls, i-1, 6)


def top(i):
    return excel.read_excel_xls(path + book_name_xls, i-1, 7)


def width(i):
    return excel.read_excel_xls(path + book_name_xls, i-1, 8)


def height(i):
    return excel.read_excel_xls(path + book_name_xls, i-1, 9)


def conf(i):
    return excel.read_excel_xls(path + book_name_xls, i-1, 10)


def text(i):
    return excel.read_excel_xls(path + book_name_xls, i-1, 11)




