from PyQt6.QtWidgets import QMenu
from PyQt6.QtGui import QAction


class floatingWindowMenu(QMenu):
    def __init__(self, parent, right_widget, bottom_widget):
        super().__init__(parent)

        # 右侧悬浮窗的重新打开操作
        self.reopen_right_action = QAction("右侧悬浮窗", parent)
        self.reopen_right_action.setCheckable(True)
        self.reopen_right_action.setChecked(True)  # 默认右侧悬浮窗可见
        self.reopen_right_action.toggled.connect(
            lambda: right_widget.setVisible(self.reopen_right_action.isChecked()))
        self.addAction(self.reopen_right_action)

        # 底部悬浮窗的重新打开操作
        self.reopen_bottom_action = QAction("底部悬浮窗", parent)
        self.reopen_bottom_action.setCheckable(True)
        self.reopen_bottom_action.setChecked(True)  # 默认底部悬浮窗可见
        self.reopen_bottom_action.toggled.connect(
            lambda: bottom_widget.setVisible(self.reopen_bottom_action.isChecked()))
        self.addAction(self.reopen_bottom_action)
