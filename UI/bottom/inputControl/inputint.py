from PyQt6.QtWidgets import QWidget, QLabel, QLineEdit, QHBoxLayout
from PyQt6.QtCore import Qt, QPoint, QMimeData
from PyQt6.QtGui import QDrag, QPixmap, QPainter


class inputInt(QWidget):
    def __init__(self, label_text="请输入数字", parent=None):
        super().__init__(parent)

        # 创建标签和文本框控件
        self.label = QLabel(label_text, self)
        self.text_input = QLineEdit(self)

        # 创建水平布局
        layout = QHBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.text_input)

        # 设置窗口的布局
        self.setLayout(layout)

        # 记录控件的原始位置
        self.original_position = self.pos()

    def mousePressEvent(self, event):
        """当鼠标按下时，开始拖动控件"""
        if event.button() == Qt.MouseButton.LeftButton:
            self.start_drag(event)

    def start_drag(self, event):
        """开始拖动操作"""
        drag = QDrag(self)  # 创建拖动对象
        mime_data = QMimeData()  # 创建 MIME 数据对象

        # 设置拖动时显示的图像（这里将控件渲染成图像）
        pixmap = QPixmap(self.size())
        self.render(pixmap)  # 将控件的当前视图渲染为图像
        drag.setPixmap(pixmap)  # 设置拖动时显示的图像

        # 设置 MIME 数据（可选，在拖放时传输数据）
        drag.setMimeData(mime_data)

        # 启动拖动，使用 MoveAction 来允许移动控件
        drag.exec(Qt.DropAction.MoveAction)

    def mouseReleaseEvent(self, event):
        """释放鼠标时，如果控件没有被放置到新的有效位置，恢复到原位"""
        if event.button() == Qt.MouseButton.LeftButton:
            self.move(self.original_position)  # 恢复控件到原始位置

    def get_value(self):
        """返回输入框中的值"""
        return self.text_input.text()

    def set_value(self, value):
        """设置输入框中的值"""
        self.text_input.setText(str(value))
