from PyQt6.QtWidgets import QMenu, QMessageBox
from PyQt6.QtGui import QAction


class aboutMenu(QMenu):
    def __init__(self, parent):
        super().__init__(parent)

        # 关于程序的动作
        self.about_action = QAction("关于程序", parent)
        self.about_action.triggered.connect(self.show_about_dialog)
        self.addAction(self.about_action)

    def show_about_dialog(self):
        about_text = (
            "程序名字: pwner2UI\n"
            "版本号: 1.0.0开发板\n"
            "作者: 归海言诺（shelbyy54）"
        )
        QMessageBox.about(self, "关于程序", about_text)
