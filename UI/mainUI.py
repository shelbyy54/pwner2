from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QTabWidget,
    QDockWidget,
    QTextEdit,
    QVBoxLayout,
    QWidget,
    QMenuBar,
    QMenu
)
from PyQt6.QtGui import QAction, QPalette, QColor
import sys

# 导入模块
from UI.tab.file import fileWidget
from UI.tab.signIn import signlnWidget
from UI.right.code import codeEditor
from UI.bottom.inputText import inputText
from UI.menu.view import floatingWindowMenu
from UI.menu.about import aboutMenu

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # 在这里放置模块
        tab_list: list[list[QWidget, str]] = [
            [fileWidget(), "设置文件"],
            [signlnWidget(), "签到栈溢出"],
            # 放置[你的类名字(),"你想要显示的标题"],<-别忘了还有个逗号
        ]
        
        # 在这里放置右侧窗口
        self.right_widget: QDockWidget = codeEditor(self)

        # 在这里放置底部窗口
        self.bottom_widget: QDockWidget = inputText(self)

        # 在这里放置菜单栏
        menu_list: list[list[QMenu, str]] = [
            [floatingWindowMenu(self,self.right_widget,
                                self.bottom_widget), "悬浮窗"],
            [aboutMenu(self), "关于"],
            # 放置[你的菜单名字(),"你想要显示的标题"],<-别忘了还有个逗号
        ]

        self.init_ui(tab_list,menu_list)

    # 启动函数，别动

    def init_ui(self, tab_widget_list,menu_list):
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
        self.addDockWidget(
            Qt.DockWidgetArea.RightDockWidgetArea, self.right_widget)

        # 底部悬浮窗
        self.addDockWidget(
            Qt.DockWidgetArea.BottomDockWidgetArea, self.bottom_widget)

        # 加载菜单栏
        self.menubar = self.menuBar()
        for menu, title in menu_list:
            menu.setTitle(title)
            self.menubar.addMenu(menu)
        self.setMenuBar(self.menubar)
