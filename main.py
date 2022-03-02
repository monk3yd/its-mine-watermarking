from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QApplication, QMainWindow, QFileDialog
import sys


# Window
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # MainWindow Position & Dimensions
        self.setGeometry(200, 200, 320, 130)  # xpos, ypos, width, height
        self.resize(269, 137)
        # TODO Window dimensions Fixed

        # Title
        self.setWindowTitle("Image Watermarking App")

        # Init User Interface
        self.initUI()

    # Build GUI
    def initUI(self):
        # Font
        font = QtGui.QFont()
        font.setWeight(400)
        self.setFont(font)

        # Create Widget
        self.widget = QtWidgets.QWidget(self)
        self.widget.setObjectName("widget")

        # Create Layout
        self.formLayout = QtWidgets.QFormLayout(self.widget)
        self.widget.setObjectName("formLayout")

        # Labels
        self.label = QtWidgets.QLabel(self.widget)  # Input label location
        self.label.setObjectName("label")
        self.label.setText("Upload Image:")  # Label Text
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label)
        # self.label.setGeometry(QtCore.QRect(30, 30, 91, 27))
        # self.label.move(50, 50)
        # self.label.adjustSize()

        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setObjectName("label_2")
        self.label_2.setText("Success! Your image was watermarked :)")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.ItemRole.SpanningRole, self.label_2)

        # Buttons
        self.button = QtWidgets.QPushButton(self.widget)
        self.button.setObjectName("button")
        self.button.setText("Select...")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.FieldRole, self.button)
        # self.button.setGeometry(QtCore.QRect(130, 30, 151, 31))
        # self.button.move(50, 100)
        # self.button.adjustSize()

        self.button_2 = QtWidgets.QPushButton(self.widget)
        self.button_2.setObjectName("button_2")
        self.button_2.setText("Watermark!")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.ItemRole.FieldRole, self.button_2)
        # self.button2.setGeometry(QtCore.QRect(130, 80, 151, 31))
        # self.button2.adjustSize()

        # Put Widget into MainWindow
        self.setCentralWidget(self.widget)

        # TODO - Menubar & Statusbar
        # Menubar
        # self.menubar = QtWidgets.QMenuBar(self)
        # self.menubar.setGeometry(QtCore.QRect(0, 0, 269, 21))
        # self.menubar.setObjectName("menubar")
        # self.menuFile = QtWidgets.QMenu(self.menubar)
        # self.menuFile.setObjectName("menuFile")
        # self.setMenuBar(self.menubar)
        # Statusbar
        # self.statusbar = QtWidgets.QStatusBar(self)
        # self.setStatusBar(self.statusbar)
        # self.menubar.addAction(self.menuFile.menuAction())

        # Link select button to click func
        self.button.clicked.connect(self.select_click)

        # QtCore.QMetaObject.connectSlotsByName(self)
        # def retranslateUI(self):
        #     pass

    def select_click(self):
        # File Dialog
        self.dialog = QFileDialog(self)
        self.dialog.setFileMode(QFileDialog.FileMode.ExistingFile)
        self.dialog.setNameFilter("Images (*.png *.xpm *.jpg)")
        self.dialog.setViewMode(QFileDialog.ViewMode.List)
        self.fileNames = []
        if self.dialog.exec():
            self.fileNames = self.dialog.selectedFiles()
            print(self.fileNames)
        self.update()

    def update(self):
        self.label.adjustSize()


# Setup Application
def window():
    app = QApplication(sys.argv)
    win = MainWindow()

    # Show GUI
    win.show()
    # Clean Exit
    sys.exit(app.exec())


window()

# Get Image & Watermark
