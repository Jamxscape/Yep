from CSS.CSS import CSS


class CSSText(CSS):
    CSSTextDict = {'color': '',  # 设置文本颜色
                   'direction': '',  # 设置文本方向
                   'letter-spacing': '',  # 设置字符间距
                   'line-height': '',  # 设置行高
                   'text-align': '',  # 对齐元素中的文本
                   'text-decoration': '',  # 向文本添加修饰
                   'text-indent': '',  # 缩进元素中文本的首行
                   'text-shadow': '',  # 设置文本阴影
                   'text-transform': '',  # 控制元素中的字母
                   'unicode-bidi': '',  # 设置或返回文本是否被重写
                   'vertical-align': '',  # 设置元素的垂直对齐
                   'white-space': '',  # 设置元素中空白的处理方式
                   'word-spacing': '',  # 设置字间距
                   }
    colon = ': '  # 英文冒号+一个空格

    def __init__(self, VarName, value):
        CSS.__init__(self, VarName)
        self.value = value

    def write(self):
        self.CSSTextDict[self.VarName] = self.value
        return self.VarName + self.colon + self.CSSTextDict[self.VarName]


