from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QApplication, QMainWindow
import sys


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # Position & Dimensions
        self.setGeometry(200, 200, 300, 300)  # xpos, ypos, width, height
        # Title
        self.setWindowTitle("This is Mine - Watermarking App")
        self.initUI()

    def initUI(self):
        # Label
        self.label = QtWidgets.QLabel(self)  # Input label location
        self.label.setText("My First Label")  # Label Text
        self.label.move(50, 50)
        # Button
        self.button = QtWidgets.QPushButton(self)
        self.button.setText("Click Me!")
        # Link button to click func
        self.button.clicked.connect(self.click)

    def click(self):
        self.label.setText("You pressed the button!")
        self.update()

    def update(self):
        self.label.adjustSize()


# Setup Application
def window():
    app = QApplication(sys.argv)
    win = MyWindow()

    # Show GUI
    win.show()
    # Clean Exit
    sys.exit(app.exec())


window()
# Build GUI

# Get Image & Watermark
