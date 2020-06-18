from CSS.CSS import CSS


class CSSBackground(CSS):  # 背景
    CSSBackgroundDict = {'background': '',  # 简写属性，作用是将背景属性设置在一个声明中
                         'background-attachment': '',  # 背景图像是否固定或者随着页面的其余部分滚动
                         'background-color': '',  # 设置元素的背景颜色。
                         'background-image': '',  # 把图像设置为背景。
                         'background-position': '',  # 设置背景图像的起始位置。
                         'background-repeat': '',  # 设置背景图像是否及如何重复。
                         }
    colon = ': '  # 英文冒号+一个空格

    def __init__(self, VarName, value):
        CSS.__init__(self, VarName)
        self.value = value

    def write(self):
        self.CSSBackgroundDict[self.VarName] = self.value
        return self.VarName + self.colon + self.CSSBackgroundDict[self.VarName]
