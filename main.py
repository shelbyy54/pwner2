'''
作者：归海言诺
这个文件是所有的启动点，即./的默认位置，此文件不可更改
'''
'''
使用的开源软件：
pyqt6
'''

import sys
from PyQt6.QtWidgets import QApplication
from UI.mainUI import MainWindow

def main():
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
