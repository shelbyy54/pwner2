from PyQt6.QtCore import Qt, QMimeData
from PyQt6.QtGui import QDrag, QPixmap, QPainter
from PyQt6.QtWidgets import QWidget, QLabel, QLineEdit, QHBoxLayout, QApplication,QPushButton


class inputInt(QWidget):
    def __init__(self, label_text="请输入数字", parent=None):
        super().__init__(parent)

        # 创建标签和文本框控件
        self.label = QLabel(label_text, self)
        self.text_input = QLineEdit(self)
        self.clear_button = QPushButton("清空", self)
        self.clear_button.clicked.connect(lambda: self.text_input.clear())

        # 创建水平布局
        layout = QHBoxLayout(self)
        layout.addWidget(self.label)
        layout.addWidget(self.text_input)
        layout.addWidget(self.clear_button)


        # 记录控件的初始位置（用于可能的拖动恢复，虽然在此示例中不使用）
        self.original_position = self.pos()

        # 启用鼠标跟踪以检测拖动
        self.setMouseTracking(True)

    # 启用鼠标跟踪
    def mousePressEvent(self, event) -> None:
        if event.button() == Qt.MouseButton.LeftButton:
            self.start_drag(event)

    def start_drag(self, event) -> None:
        """开始拖动操作"""
        drag = QDrag(self)  # 创建拖动对象
        mime_data = QMimeData()  # 创建 MIME 数据对象

        # 设置拖动时显示的图像（将控件渲染成图像）
        pixmap = QPixmap(self.size())
        pixmap.fill(Qt.GlobalColor.white)  # 填充背景色，避免透明问题
        painter = QPainter(pixmap)
        self.render(painter)  # 将控件的当前视图渲染为图像
        painter.end()  # 结束绘制
        drag.setPixmap(pixmap)  # 设置拖动时显示的图像

        # 设置 MIME 数据（这里我们传输文本数据）
        mime_data.setText(self.text_input.text())
        drag.setMimeData(mime_data)  # 设置 mime_data

        # 启动拖动操作，使用 CopyAction 允许复制
        drag.exec(Qt.DropAction.CopyAction)  # 执行拖动操作

    def mouseMoveEvent(self, event) -> None:
        """鼠标移动事件，用于检测拖动开始"""
        if event.buttons() & Qt.MouseButton.LeftButton:
            pass

    def mouseReleaseEvent(self, event) -> None:
        """释放鼠标事件"""
        pass

    def get_value(self) -> str:
        """返回输入框中的值"""
        return self.text_input.text()

    def set_value(self, value: str) -> None:
        """设置输入框中的值"""
        self.text_input.setText(value)

if __name__ == "__main__":
    app = QApplication([])
    widget = inputInt()
    widget.show()
    app.exec()
