import HTML.HTML
import excel

def create_html():
    path_excel = "../excel/result.xls"
    line_count = 2  # 行数
    result_rows = excel.get_excel_rows(path_excel)  # 获取result.xls最大行数
    source_code = HTML.HTML.meta + HTML.HTML.next_line # 声明
    source_code += HTML.HTML.html + HTML.HTML.next_line + HTML.HTML.find_your_another_one(HTML.HTML.html)
    title = HTML.HTML.next_line + HTML.HTML.title + HTML.HTML.next_line + \
                   excel.read_excel_xls(path_excel, 1, 5)  + HTML.HTML.next_line +\
                   HTML.HTML.find_your_another_one(HTML.HTML.title) +\
            HTML.HTML.next_line # 写入title
    head = HTML.HTML.next_line + HTML.HTML.head + \
           HTML.HTML.next_line + HTML.HTML.find_your_another_one(HTML.HTML.head) # 生成head
    css_state = HTML.HTML.split_detail("<link", HTML.HTML.link, "rel=\"stylesheet\" "
                                                            "type=\"text/css\" href=\"../css/test.css\"") # 生成CSS声明
    head = HTML.HTML.split_detail(HTML.HTML.head, head, title + css_state)
    body = HTML.HTML.body + HTML.HTML.find_your_another_one(HTML.HTML.body)
    div_block = ""
    while line_count <= result_rows:
        class_name = excel.read_excel_xls(path_excel, line_count - 1, 0)
        text = excel.read_excel_xls(path_excel, line_count - 1, 5)
        temp = HTML.HTML.split_detail("<div", HTML.HTML.div, HTML.HTML.class_name + "=\"" + class_name +"\"")
        div_block += (temp + HTML.HTML.next_line + text + HTML.HTML.next_line +
                      HTML.HTML.find_your_another_one(HTML.HTML.div) + HTML.HTML.next_line)
        line_count += 1
    body = HTML.HTML.next_line + HTML.HTML.split_detail(HTML.HTML.body, body, div_block)
    head_body = head + body
    source_code = HTML.HTML.split_detail(HTML.HTML.html, source_code, head_body)
    return source_code


# create_html()