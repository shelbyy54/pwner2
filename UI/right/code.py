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


# class PythonHighlighter(QSyntaxHighlighter):
#     def __init__(self, document):
#         super().__init__(document)

#         # 定义语法高亮格式
#         self.keyword_format = QTextCharFormat()
#         self.keyword_format.setForeground(QColor(0, 0, 255))  # 蓝色

#         self.string_format = QTextCharFormat()
#         self.string_format.setForeground(QColor(255, 0, 0))  # 红色

#         # 定义高亮规则
#         self.highlighting_rules = [
#             (QRegularExpression(
#                 r'\b(def|class|import|from|as|return|if|else|elif|while|for|try|except|finally)\b'), self.keyword_format),
#             (QRegularExpression(r'"[^"]*"'), self.string_format),  # 字符串
#         ]

#     def highlightBlock(self, text):
#         for pattern, format in self.highlighting_rules:
#             expression = pattern
#             index = expression.match(text).hasMatch()
#             while index:
#                 length = expression.match(text).capturedLength()
#                 self.setFormat(index, length, format)
#                 index = expression.match(text, index + length).hasMatch()

class codeEditor(QDockWidget):
    def __init__(self, parent=None):
        super().__init__("代码编辑器", parent)

        # 创建 QPlainTextEdit 控件
        self.text_edit = QPlainTextEdit(self)
        self.text_edit.setPlainText("from pwn import *")  # 设置初始代码

        # 添加语法高亮
        # self.highlighter = PythonHighlighter(self.text_edit.document())

        # 创建保存按钮
        self.save_button = QPushButton("保存代码", self)
        self.save_button.clicked.connect(self.save_code)

        # 创建布局
        layout = QVBoxLayout()
        layout.addWidget(self.text_edit)
        layout.addWidget(self.save_button)

        # 设置窗口的布局
        widget = QWidget()
        widget.setLayout(layout)
        self.setWidget(widget)

        # 设置停靠区域，右侧
        self.setAllowedAreas(Qt.DockWidgetArea.RightDockWidgetArea)

    def save_code(self):
        # 获取文本框中的内容
        code = self.text_edit.toPlainText()
        with open("saved_code.py", "w", encoding="utf-8") as file:
            file.write(code)
        print("代码已保存到 saved_code.py")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = codeEditor()
    window.show()
    sys.exit(app.exec())
