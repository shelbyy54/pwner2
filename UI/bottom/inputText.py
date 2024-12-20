from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QApplication,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QDockWidget
)
import sys

from UI.bottom.inputControl.inputint import inputInt
from UI.bottom.inputControl.inputaddress import inputAddress

class inputText(QDockWidget):
    def __init__(self, parent=None):
        super().__init__("统一输入控制", parent)

        # 创建布局(水平)
        input_Layout = QHBoxLayout()
        # 竖直布局0
        input_0 = QVBoxLayout()
        self.int_input = inputInt("整数")
        input_0.addWidget(self.int_input)
        input_0.addWidget(inputInt())
        input_0.addWidget(inputInt())
        input_0.addWidget(inputInt())

        # 竖直布局1
        input_1 = QVBoxLayout()
        self.address_input = inputAddress("地址")
        input_1.addWidget(self.address_input)
        input_1.addWidget(inputAddress())
        input_1.addWidget(inputAddress())
        input_1.addWidget(inputAddress())

        # 设置窗口的布局
        input_Layout.addLayout(input_0)
        input_Layout.addLayout(input_1)
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
