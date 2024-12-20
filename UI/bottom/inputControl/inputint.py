from PyQt6.QtWidgets import QWidget, QLabel, QLineEdit, QHBoxLayout
from PyQt6.QtCore import Qt


class inputInt(QWidget):
    def __init__(self, label_text="请输入数字", parent=None):
        super().__init__(parent)

        # 创建标签和文本框控件
        self.label = QLabel(label_text, self)
        self.text_input = QLineEdit(self)

        # 创建水平布局
        layout = QHBoxLayout(self)
        layout.addWidget(self.label)
        layout.addWidget(self.text_input)

        # 设置窗口的布局
        self.setLayout(layout)

    def get_value(self):
        """返回输入框中的值"""
        return self.text_input.text()

    def set_value(self, value):
        """设置输入框中的值"""
        self.text_input.setText(str(value))
