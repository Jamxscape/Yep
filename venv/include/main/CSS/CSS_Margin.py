from CSS.CSS import CSS


class CSSMargin(CSS):
    CSSMarginDict = {'margin': '',  # 简写属性。在一个声明中设置所有外边距属性。
                     'margin-bottom': '',  # 设置元素的下外边距。
                     'margin-left': '',  # 设置元素的左外边距。
                     'margin-right': '',  # 设置元素的右外边距。
                     'margin-top': '',  # 设置元素的上外边距
                   }
    colon = ': '  # 英文冒号+一个空格

    def __init__(self, VarName, value):
        CSS.__init__(self, VarName)
        self.value = value

    def write(self):
        self.CSSMarginDict[self.VarName] = self.value
        return self.VarName + self.colon + self.CSSMarginDict[self.VarName]


