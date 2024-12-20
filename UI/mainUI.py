import sys
from PyQt6.QtWidgets import (
    QMainWindow,
    QTabWidget,
    QDockWidget,
    QVBoxLayout,
    QWidget,
)
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
)
from PyQt6.QtGui import QAction
import sys

# 导入模块
from UI.tab.file import fileWidget
from UI.tab.signIn import signlnWidget
from UI.right.code import codeEditor
from UI.bottom.inputText import inputText


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
        right_widget: QDockWidget = codeEditor(self)

        # 在这里放置底部窗口
        bottom_widget: QDockWidget = inputText(self)

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
        # 添加菜单栏
        self.create_menus()

    def create_menus(self):
        """创建菜单栏，允许重新打开右侧和底部悬浮窗"""
        menubar = self.menuBar()

        # 创建视图菜单
        view_menu = menubar.addMenu("视图")

        # 创建右侧悬浮窗的重新打开操作
        self.reopen_right_action = QAction("右侧悬浮窗", self)
        self.reopen_right_action.setCheckable(True)  # 设置为可检查
        self.reopen_right_action.toggled.connect(self.toggle_right_dock)  # 连接 toggled 信号
        view_menu.addAction(self.reopen_right_action)

        # 创建底部悬浮窗的重新打开操作
        self.reopen_bottom_action = QAction("底部悬浮窗", self)
        self.reopen_bottom_action.setCheckable(True)  # 设置为可检查
        self.reopen_bottom_action.toggled.connect(self.toggle_bottom_dock)  # 连接 toggled 信号
        view_menu.addAction(self.reopen_bottom_action)

        # 初始化菜单项的检查状态以匹配悬浮窗的可见性
        # 这里要确保右侧和底部的悬浮窗初始时是可见的，并将对应的菜单项选中
        self.reopen_right_action.setChecked(True)  # 右侧悬浮窗默认选中
        self.reopen_bottom_action.setChecked(True)  # 底部悬浮窗默认选中

        # 更新悬浮窗的可见性，以便它们在应用启动时显示
        self.right_widget.setVisible(True)
        self.bottom_widget.setVisible(True)

    def toggle_right_dock(self):
        """切换右侧悬浮窗的可见性，并更新菜单项的检查状态"""
        self.right_widget.setVisible(self.reopen_right_action.isChecked())

    def toggle_bottom_dock(self):
        """切换底部悬浮窗的可见性，并更新菜单项的检查状态"""
        self.bottom_widget.setVisible(self.reopen_bottom_action.isChecked())
