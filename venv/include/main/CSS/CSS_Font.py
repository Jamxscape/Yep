from CSS.CSS import CSS


class CSSFont(CSS):
    CSSFontDict = {'font': '',  # 在一个声明中设置所有的字体属性
                   'font-family': '',  # 设指定文本的字体系列
                   'font-size': '',  # 指定文本的字体大小
                   'font-style': '',  # 设置行高
                   'font-variant': '',  # 以小型大写字体或者正常字体显示文本。
                   'font-weight': '',  # 指定字体的粗细。
                   }
    colon = ': '  # 英文冒号+一个空格

    def __init__(self, VarName, value):
        CSS.__init__(self, VarName)
        self.value = value

    def write(self):
        self.CSSFontDict[self.VarName] = self.value
        return self.VarName + self.colon + self.CSSFontDict[self.VarName]


