from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QApplication, QMainWindow, QFileDialog

from PIL import Image, ImageFont, ImageDraw

# import matplotlib.pyplot as plt
# import numpy as np

import sys


# Window
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # MainWindow Position & Dimensions
        self.setGeometry(200, 200, 274, 90)  # xpos, ypos, width, height
        # self.resize(269, 137)
        # TODO - Window dimensions Fixed

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
        # self.widget.setObjectName("widget")

        # Create Layout
        self.formLayout = QtWidgets.QFormLayout(self.widget)
        # self.widget.setObjectName("formLayout")

        # Labels
        self.label = QtWidgets.QLabel(self.widget)  # Input label location
        # self.label.setObjectName("label")
        self.label.setText("Upload Image:")  # Label Text
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label)
        # self.label.setGeometry(QtCore.QRect(30, 30, 91, 27))
        # self.label.move(50, 50)
        # self.label.adjustSize()

        self.label_2 = QtWidgets.QLabel(self.widget)
        # self.label_2.setObjectName("label_2")
        self.label_2.setText("Please select an image. Then watermark it!")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.ItemRole.SpanningRole, self.label_2)

        # Buttons
        self.button = QtWidgets.QPushButton(self.widget)
        # self.button.setObjectName("button")
        self.button.setText("Select...")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.FieldRole, self.button)
        # self.button.setGeometry(QtCore.QRect(130, 30, 151, 31))
        # self.button.move(50, 100)
        # self.button.adjustSize()

        self.button_2 = QtWidgets.QPushButton(self.widget)
        # self.button_2.setObjectName("button_2")
        self.button_2.setText("Watermark!")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.ItemRole.FieldRole, self.button_2)
        # self.button2.setGeometry(QtCore.QRect(130, 80, 151, 31))
        # self.button2.adjustSize()

        # Put Widget into MainWindow
        self.setCentralWidget(self.widget)

        # TODO - Menubar & Statusbar GUI
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

        # Link buttons to click functions
        self.button.clicked.connect(self.select_click)
        self.button_2.clicked.connect(self.watermark_click)

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
            self.PATH = self.fileNames[0]
            print(f"You've selected your image.\nPATH: {self.PATH}")
            self.label_2.setText("You've selected your image.")
            self.update()

    def watermark_click(self):
        print(f"Opening Image...")
        # TODO - implement Image Watermarking
        # Open Image & Create New Text Layer
        img = Image.open(self.PATH).convert("RGBA")
        txt = Image.new('RGBA', img.size, (255, 255, 255, 0))

        print(f"Format: {img.format} | Width: {img.size[0]}, Height: {img.size[1]} | ColorMode: {img.mode}")

        # Set Text & Font of Watermark
        # TODO - Personalized Text when Watermarking
        text = "monk3yd"
        font = ImageFont.truetype("font/Raleway-Medium.ttf", 50)
        font_color = (0, 0, 0, 125)

        # Select Image by Creating Draw Object
        draw = ImageDraw.Draw(txt)

        # Text Watermark Position
        width, height = img.size  # Image Dimensions
        markwidth, markheight = draw.textsize(text, font)  # Watermark Dimensions
        x = width - markwidth - 100
        y = height - markheight - 50

        # Draw Watermark into Img through Draw Object
        draw.text((x, y), text, font_color, font=font)

        # Combining Image with Text & Save
        watermarked = Image.alpha_composite(img, txt)
        watermarked.show()

        # TODO - Save New Img
        # self.watermark_img.save()
        # plt.imshow(self.watermark_img)

        # Success
        print("Success! Your image was watermarked :)")
        self.label_2.setText("Success! Your image was watermarked :)")
        self.update()

    def update(self):
        self.label_2.adjustSize()


# Setup Application
def window():
    app = QApplication(sys.argv)
    win = MainWindow()

    # Show GUI
    win.show()
    # Clean Exit
    sys.exit(app.exec())


if __name__ == "__main__":
    window()
