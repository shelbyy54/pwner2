from PyQt6.QtWidgets import QLineEdit, QApplication
from PyQt6.QtCore import QMimeData, Qt

class inputLineEdit(QLineEdit):
    def __init__(self, allowed_types=None, parent=None):
        super().__init__(parent)
        self.setAcceptDrops(True)
        self.allowed_types = allowed_types if allowed_types is not None else []
        self.update_placeholder_text()

    def update_placeholder_text(self):
        if self.allowed_types:
            allowed_types_str = ", ".join(self.allowed_types)
            self.setPlaceholderText(f"允许输入的类型: {allowed_types_str}")
        else:
            self.setPlaceholderText("允许输入任何类型")

    def dragEnterEvent(self, event) -> None:
        if self.allowed_types:
            for allowed_type in self.allowed_types:
                if event.mimeData().hasFormat(f"application/x-{allowed_type}"):
                    event.acceptProposedAction()
                    return
            event.ignore()
        else:
            event.acceptProposedAction()

    def dropEvent(self, event) -> None:
        if self.allowed_types:
            for allowed_type in self.allowed_types:
                if event.mimeData().hasFormat(f"application/x-{allowed_type}"):
                    text = event.mimeData().text()
                    self.setText(text)
                    event.acceptProposedAction()
                    return
            event.ignore()
        else:
            text = event.mimeData().text()
            self.setText(text)
            event.acceptProposedAction()

if __name__ == "__main__":
    app = QApplication([])
    widget = inputLineEdit(["int", "bit"])
    widget.show()
    app.exec()