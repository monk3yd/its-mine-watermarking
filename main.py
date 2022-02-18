from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QApplication, QMainWindow
import sys


# Setup Application
def window():
    app = QApplication(sys.argv)
    win = QMainWindow()
    # Position & Dimensions
    win.setGeometry(200, 200, 300, 300)  # xpos, ypos, width, height
    # Title
    win.setWindowTitle("This is Mine - Watermarking App")
    # Label
    label = QtWidgets.QLabel(win)  # Input label location
    label.setText("My First Label")  # Label Text
    label.move(50, 50)

    # Show GUI
    win.show()
    # Clean Exit
    sys.exit(app.exec())


window()
# Build GUI

# Get Image & Watermark
