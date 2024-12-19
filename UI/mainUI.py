import sys
from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QTabWidget,
    QDockWidget,
    QTextEdit,
    QVBoxLayout,
    QWidget,
    QLabel
)
from PyQt6.QtCore import Qt

# 导入模块
# 把你的ui模块丢到/UI/tab里面，然后输入
# from UI.tab.你的模块名字 import 你的类名字
from UI.tab.file import fileWidget
from UI.tab.signIn import signlnWidget
from UI.right.code import codeEditor


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # 在这里放置模块
        tab_list: list[list[QWidget, str]] = [
            [fileWidget(), "设置文件"],
            [signlnWidget(), "签到栈溢出"],
            #放置[你的类名字(),"你想要显示的标题"],<-别忘了还有个逗号
        ]
        # 在这里放置右侧窗口
        right_widget: QDockWidget = codeEditor(self)
        # 在这里放置底部窗口
        bottom_widget: QDockWidget = codeEditor(self)

        self.init_ui(tab_list, right_widget, bottom_widget)

    # 启动函数，别动
    def init_ui(self, tab_widget_list, right_widget, bottom_widget):

        self.setWindowTitle("归海言诺pwn工具箱")
        self.setGeometry(100, 100, 1000, 700)

        # 中心窗口
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        # QTabWidget与加载模块
        self.tab_widget = QTabWidget(central_widget)
        for widget, label in tab_widget_list:
            self.tab_widget.addTab(widget, label)

        # 创建并设置布局
        layout = QVBoxLayout(central_widget)
        layout.addWidget(self.tab_widget)

        # 右边悬浮窗
        self.right_widget = right_widget
        self.addDockWidget(
            Qt.DockWidgetArea.RightDockWidgetArea, right_widget)

        # 底部悬浮窗
        self.bottom_widget = bottom_widget
        self.addDockWidget(
            Qt.DockWidgetArea.BottomDockWidgetArea, bottom_widget)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
