from PyQt6.QtCore import QRegularExpression, Qt
from PyQt6.QtGui import QSyntaxHighlighter, QTextCharFormat, QColor
from PyQt6.QtWidgets import (
    QApplication,
    QWidget,
    QPlainTextEdit,
    QVBoxLayout,
    QHBoxLayout,
    QPushButton,
    QDockWidget
)
import sys

from UI.bottom.inputControl.inputint import inputInt
from UI.bottom.inputControl.inputaddress import inputAddress

class inputText(QDockWidget):
    def __init__(self, parent=None):
        super().__init__("统一输入控制", parent)

        # 创建布局(水平)
        input_Layout = QHBoxLayout(self)
        # 竖直布局0
        input_0 = QVBoxLayout(self)
        self.int_input = inputInt("整数")
        input_0.addWidget(self.int_input)
        input_0.addWidget(inputInt())
        input_0.addWidget(inputInt())
        input_0.addWidget(inputInt())

        # 竖直布局1
        input_1 = QVBoxLayout(self)
        self.address_input = inputAddress("地址")
        input_1.addWidget(self.address_input)
        input_1.addWidget(inputAddress())
        input_1.addWidget(inputAddress())
        input_1.addWidget(inputAddress())
        input_Layout.addLayout(input_0)
        input_Layout.addLayout(input_1)

        # 设置窗口的布局
        widget = QWidget()
        widget.setLayout(input_Layout)
        self.setWidget(widget)

        # 设置停靠区域，底侧
        self.setAllowedAreas(Qt.DockWidgetArea.BottomDockWidgetArea)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = inputText()
    window.show()
    sys.exit(app.exec())
