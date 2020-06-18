html = "<html>"
head = "<head>"
title = "<title>"
div = "<div>"
par = "<p>"
body = "<body>"
next_line = "\n"
state = "<!doctype html>"
meta = "<meta charset=\"UTF-8\">"
class_name = "class"
link = "<link>"
rel = "rel"
type_name = "type"
href_name = "href"

def find_your_another_one(var_name): # 生成一对标签
    another_name = "</" + var_name.strip("<")
    return another_name

def append_detail(var_name, value_name, value): # 对标签内添加详细信息，如类
    append_element = var_name.strip('>') + ' ' + value_name + "=\"" + value + "\">"
    return append_element

def split_detail(var_name, source_code, value): # 对一整块进行添加
    temp = source_code.split(var_name)
    temp.append(value)
    temp[0] = temp[0] + var_name + " " #
    temp_value = temp[1]
    temp[2] = temp_value
    temp[1] = value
    source_code = ''.join(temp)
    return source_code


# html = find_your_another_one(state)
# a = append_detail(link, rel, "text")
#
# source_code1 = "<link>"
# b = split_detail("<link", source_code1, "text")
# source_code2 = "<link></link>"
# c = split_detail("<link>", source_code2, "text")
# print(b)
# print(c)