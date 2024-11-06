from PyQt6.QtWidgets import QApplication
from MainWindowEx import MainWindow
app = QApplication([])
myWindow = MainWindow()
myWindow.show()
app.exec()

