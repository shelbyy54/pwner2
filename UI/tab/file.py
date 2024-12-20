from PyQt6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QPushButton,
    QLabel,
    QFileDialog,
    QApplication,
    QHBoxLayout,
    QLineEdit,
    QScrollArea
)
from PyQt6.QtCore import QDir

class fileWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        # 创建一个 QWidget 作为滚动区域的内容
        scroll_area_content = QWidget(self)
        # ！上面是八股文，不用动

        # 把你的布局丢在这里
        layout = QVBoxLayout(scroll_area_content)
        file_path_Layout = QHBoxLayout()
        # 创建提示标签
        self.prompt_label = QLabel("请选择一个文件：", self)
        file_path_Layout.addWidget(self.prompt_label)
        # 创建文件选择框按钮
        self.file_button = QPushButton("选择文件", self)
        self.file_button.clicked.connect(self.open_file_dialog)
        file_path_Layout.addWidget(self.file_button)
        layout.addLayout(file_path_Layout)
        # 创建提示标签
        self.prompt_text_label = QLabel("请选择的文件为:", self)
        layout.addWidget(self.prompt_text_label)

        # 创建不可编辑的文本框
        self.read_only_text = QLineEdit(self)
        self.read_only_text.setReadOnly(True)
        layout.addWidget(self.read_only_text)
        for i in range(300):
            layout.addWidget(QLabel("测试",self))


        # ！下面是八股文，不用动
        # 创建 QScrollArea 并设置其内容为 scroll_area_content
        scroll_area = QScrollArea(self)
        scroll_area.setWidget(scroll_area_content)
        scroll_area.setWidgetResizable(True)  # 允许内容调整大小

        # 设置 fileWidget 的最外层布局，并将 QScrollArea 添加到其中
        outer_layout = QVBoxLayout(self)
        outer_layout.addWidget(scroll_area)

    def open_file_dialog(self):
        # 打开文件选择对话框
        file_name, _ = QFileDialog.getOpenFileName(
            self, "选择文件", QDir.currentPath(), "All Files (*);;Text Files (*.txt)")
        if file_name:
            self.read_only_text.setText("{}".format(file_name))


# 这是一个简单的测试函数，用于在独立运行时显示窗口（通常不需要在最终项目中）
if __name__ == "__main__":
    app = QApplication([])
    widget = fileWidget()
    widget.show()
    app.exec()
