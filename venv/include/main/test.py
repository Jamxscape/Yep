import os
import stat
import excel
import ImageToData
from CSS import CSS_Text
from CSS import CSS_Font

dir_name_CSS = "../source/css"
if not os.path.isdir(dir_name_CSS):
    os.makedirs(dir_name_CSS)
dir_name_HTML = "../source/html"
if not os.path.isdir(dir_name_HTML):
    os.makedirs(dir_name_HTML)
dir_name_JS = "../source/js"
if not os.path.isdir(dir_name_JS):
    os.makedirs(dir_name_JS)
# file_name = '/source/test.css'
# open(file_name, "w")
# filename = '/tmp/tmpfile'
# mode = stat.S_IRUSR
#
# # 文件系统节点指定不同模式
# os.mknod(filename, mode)
os.chdir('../source/css')
file_name = 'test.css'
open(file_name, "w")




