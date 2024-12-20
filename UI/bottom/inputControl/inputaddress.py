from PyQt6.QtWidgets import (
    QWidget,
    QLabel,
    QHBoxLayout,
    QComboBox,
    QLineEdit
)
from PyQt6.QtCore import Qt, QMimeData
from PyQt6.QtGui import QDrag, QPixmap, QPainter
from PyQt6.QtWidgets import QPushButton


class inputAddress(QWidget):
    def __init__(self, label_text="请输入地址", parent=None):
        super().__init__(parent)

        # 创建标签和文本框控件
        self.label = QLabel(label_text, self)
        self.text_input = QLineEdit(self)

        # 设置下拉框
        self.system = QComboBox(self)
        self.system.addItem('请选择架构')
        self.system.addItem('x86')
        self.system.addItem('x64')
        self.system.addItem('arm')

        self.clear_button = QPushButton("清空", self)
        self.clear_button.clicked.connect(lambda: self.text_input.clear())

        # 创建水平布局
        layout = QHBoxLayout(self)
        layout.addWidget(self.label)
        layout.addWidget(self.system)
        layout.addWidget(self.text_input)
        layout.addWidget(self.clear_button)

        # 记录控件的初始文本内容
        self.original_text = self.text_input.text()

        # 记录控件的初始位置（用于可能的拖动恢复，虽然在此示例中不使用）
        self.original_position = self.pos()

        # 启用鼠标跟踪以检测拖动
        self.setMouseTracking(True)

    def mousePressEvent(self, event) -> None:
        if event.button() == Qt.MouseButton.LeftButton:
            self.start_drag(event)

    def start_drag(self, event):
        drag = QDrag(self)
        mime_data = QMimeData()
        pixmap = QPixmap(self.size())
        pixmap.fill(Qt.GlobalColor.white)
        painter = QPainter(pixmap)
        self.render(painter)
        painter.end()
        drag.setPixmap(pixmap)
        mime_data.setText(self.add_system_format_text(self.text_input.text()))
        drag.setMimeData(mime_data)
        drag.exec(Qt.DropAction.CopyAction)

    def add_system_format_text(self, base_text):
        selected_system = self.system.currentText()
        if selected_system == 'x86':
            return f'p32({base_text})'
        elif selected_system == 'x64':
            return f'p64({base_text})'
        elif selected_system == 'arm':
            return f'parm({base_text})'
        return base_text

    def get_value(self) -> str:
        """返回输入框中的值"""
        return self.text_input.text()

    def set_value(self, value: str) -> None:
        """设置输入框中的值"""
        self.text_input.setText(value)

    def restore_original_text(self):
        """恢复原始文本内容"""
        self.text_input.setText(self.original_text)
