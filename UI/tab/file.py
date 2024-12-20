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
from PyQt6.QtCore import QDir, QProcess
import json
import sys

class fileWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        # 创建布局
        layout = QVBoxLayout()

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

        # 设置布局
        self.setLayout(layout)

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
