from CSS.CSS import CSS


class CSSPosition(CSS):
    CSSPositionDict = {'bottom': '',  # 定义了定位元素下外边距边界与其包含块下边界之间的偏移。
                       'clip': '',  # 剪辑一个绝对定位的元素。
                       'cursor': '',  # 显示光标移动到指定的类型。
                       'left': '',  # 定义了定位元素左外边距边界与其包含块左边界之间的偏移。
                       'overflow': '',  # 设置当元素的内容溢出其区域时发生的事情。
                       'overflow-y': '',  # 指定如何处理顶部/底部边缘的内容溢出元素的内容区域
                       'overflow-x': '',  # 指定如何处理右边/左边边缘的内容溢出元素的内容区域
                       'position': '',  # 指定元素的定位类型
                       'right': '',  # 定义了定位元素右外边距边界与其包含块右边界之间的偏移。
                       'top': '',  # 定义了定位元素右外边距边界与其包含块右边界之间的偏移。
                       'z-index': '',  # 设置元素的堆叠顺序
                       }
    CSSPositionValue = ["absolute",  # 生成绝对定位的元素，相对于 static 定位以外的第一个父元素进行定位,
                                       #  元素的位置通过 "left", "top", "right" 以及 "bottom" 属性进行规定。
                        "fixed",      # 生成固定定位的元素，相对于浏览器窗口进行定位
                        "relative",
                        "static",
                        "sticky",
                        "inherit",
                        "initial"]
    colon = ': '  # 英文冒号+一个空格

    def __init__(self, VarName, value):
        CSS.__init__(self, VarName)
        self.value = value

    def write(self):
        self.CSSPositionDict[self.VarName] = self.value
        return self.VarName + self.colon + self.CSSPositionDict[self.VarName]


# 简单的测试一下这个类哦
# c = CSSPosition("position", CSSPosition.CSSPositionValue[0])
# print(c.write())


