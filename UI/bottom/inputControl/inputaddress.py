from PyQt6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QPushButton,
    QLabel,
    QTextEdit,
    QFileDialog,
    QApplication,
    QHBoxLayout,
    QComboBox,
    QCheckBox,
    QLineEdit
)
from PyQt6.QtCore import Qt


class inputAddress(QWidget):
    def __init__(self, label_text="请输入地址", parent=None):
        super().__init__(parent)

        # 创建标签和文本框控件
        self.label = QLabel(label_text, self)
        self.text_input = QLineEdit(self)
        # 设置下拉窗口
        self.system = QComboBox(self)
        self.system.addItem('请选择架构')
        self.system.addItem('x86')
        self.system.addItem('x64')
        self.system.addItem('arm')

        # 创建水平布局
        layout = QHBoxLayout(self)
        layout.addWidget(self.label)
        layout.addWidget(self.system)
        layout.addWidget(self.text_input)

        # 设置窗口的布局
        self.setLayout(layout)

    def get_value(self):
        """返回输入框中的值"""
        return self.text_input.text()

    def set_value(self, value):
        """设置输入框中的值"""
        self.text_input.setText(str(value))
