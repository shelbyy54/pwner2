from PyQt6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QPushButton,
    QLabel,
    QApplication,
    QHBoxLayout,
    QComboBox,
    QCheckBox,
    QLineEdit,
    QScrollArea
)
from UI.tab.inputLineEdit import inputLineEdit

class signlnWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        # 创建一个主要的 QWidget 作为滚动区域的内容
        scroll_area_content = QWidget()
        # ！上面是八股文，不用动

        # 把你的布局丢在这里
        layout = QVBoxLayout(scroll_area_content)

        # 水平布局
        fun_name_Layout = QHBoxLayout()
        #设置标签
        self.fun_Label = QLabel("请选择栈溢出函数", self)
        # 设置下拉窗口
        self.fun_ComboBox = QComboBox(self)
        self.fun_ComboBox.addItem('请选择函数')
        self.fun_ComboBox.addItem('scanf')
        self.fun_ComboBox.addItem('read')
        self.fun_ComboBox.addItem('gets')
        # 将标签和下拉框添加到水平布局中
        fun_name_Layout.addWidget(self.fun_Label)
        fun_name_Layout.addWidget(self.fun_ComboBox)
        # 丢进来
        layout.addLayout(fun_name_Layout)


        # 设置溢出数字
        fun_Layout = QHBoxLayout()
        self.fun_unmber = QLabel("请输入溢出的数据大小", self)
        self.add8 = QCheckBox("覆盖帧指针（即数据+8）",self)
        self.fun_number_text = inputLineEdit(["int"])
        self.fun_number_text.resize(100,5)
        fun_Layout.addWidget(self.fun_unmber)
        fun_Layout.addWidget(self.fun_number_text)
        fun_Layout.addWidget(self.add8)
        layout.addLayout(fun_Layout)

        # 设置溢出地址
        fun_arr = QHBoxLayout()
        self.fun_arr_unmber = QLabel("请输入要溢出到的地址", self)
        self.add1 = QCheckBox("跳过首指令（即地址+1）", self)
        self.fun_arr_text = inputLineEdit( ["bit"])
        self.fun_arr_text.resize(100, 5)
        fun_arr.addWidget(self.fun_arr_unmber)
        fun_arr.addWidget(self.fun_arr_text)
        fun_arr.addWidget(self.add1)
        layout.addLayout(fun_arr)

        self.fun_make_code = QPushButton("生成代码")
        layout.addWidget(self.fun_make_code)

        # ！下面是八股文，不用动
        # 创建 QScrollArea 并设置其内容为 scroll_area_content
        scroll_area = QScrollArea(self)
        scroll_area.setWidget(scroll_area_content)
        scroll_area.setWidgetResizable(True)  # 允许内容调整大小

        # 创建一个最外层的 QVBoxLayout 并将 QScrollArea 添加到其中
        outer_layout = QVBoxLayout(self)
        outer_layout.addWidget(scroll_area)


# 这是一个简单的测试函数，用于在独立运行时显示窗口（通常不需要在最终项目中）
if __name__ == "__main__":
    app = QApplication([])
    widget = signlnWidget()
    widget.show()
    app.exec()
