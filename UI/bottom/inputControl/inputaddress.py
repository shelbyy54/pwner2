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
from PyQt6.QtCore import Qt, QPoint, QMimeData
from PyQt6.QtGui import QDrag, QPixmap, QPainter


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

        # 创建水平布局
        layout = QHBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.system)
        layout.addWidget(self.text_input)

        # 用于存储鼠标按下的起始位置
        self.drag_position = QPoint()

        # 设置窗口的布局
        self.setLayout(layout)

    def mousePressEvent(self, event):
        """记录鼠标按下的位置"""
        if event.button() == Qt.MouseButton.LeftButton:
            self.drag_position = event.position().toPoint()

            # 开始拖动
            self.start_drag(event)

    def start_drag(self, event):
        """启动拖动操作"""
        drag = QDrag(self)  # 创建QDrag对象
        mime_data = QMimeData()  # 创建MIME数据

        # 设置拖动时显示的图像
        pixmap = QPixmap(self.size())
        self.render(pixmap)  # 渲染控件内容为图像
        drag.setPixmap(pixmap)  # 设置图像作为拖动时的图标

        # 设置MIME数据（此处为空，可以根据需要传输额外数据）
        drag.setMimeData(mime_data)

        # 执行拖动，使用移动动作
        drag.exec(Qt.DropAction.MoveAction)

    def mouseMoveEvent(self, event):
        """根据鼠标移动更新控件位置"""
        # 注意：此方法的实现已经不再需要用于处理拖动，因为我们已经使用了QDrag来处理拖动。
        pass

    def mouseReleaseEvent(self, event):
        """释放鼠标时恢复控件原位"""
        if event.button() == Qt.MouseButton.LeftButton:
            self.move(self.pos())  # 恢复控件到原始位置

    def get_value(self):
        """返回输入框中的值"""
        return self.text_input.text()

    def set_value(self, value):
        """设置输入框中的值"""
        self.text_input.setText(str(value))
