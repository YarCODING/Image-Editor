from PyQt5 import QtCore, QtGui, QtWidgets
from PIL import Image, ImageFilter, ImageEnhance
import os

class ImageEditor():
    def __init__(self):
        self.directory = None
        self.original = None
        self.edited = None
        self.editedphotos = []

    def open(self, directory:str):
        self.directory = directory
        self.original = Image.open(f'{self.directory}')
        self.edited = self.original

    def close(self):
        self.directory = None
        self.original = None


    def show_original(self):
        self.original.show()
    
    def show_edited(self):
        self.edited.show()


    def do_mirror(self):
        self.edited = self.edited.transpose(Image.FLIP_LEFT_RIGHT)
    
    def do_gray(self):
        self.edited = self.original.convert('L')

    def do_turn_90(self):
        self.edited = self.edited.transpose(Image.ROTATE_90)
    
    def do_turn_180(self):
        self.edited = self.edited.transpose(Image.ROTATE_180)

    def do_blur(self):
        self.edited = self.edited.filter(ImageFilter.BLUR)

    def do_crop(self, coordinates:tuple):
        self.edited = self.edited.crop(coordinates)

    def save(self, name):
        self.edited.save(name)

        self.editedphotos.append(self.edited)


editor = ImageEditor()

class Ui_Image_Editor(object):
    def setupUi(self, Image_Editor):
        Image_Editor.setObjectName("Image_Editor")
        Image_Editor.resize(800, 700)
        self.centralwidget = QtWidgets.QWidget(Image_Editor)
        self.centralwidget.setObjectName("centralwidget")
        self.to_left_btn = QtWidgets.QPushButton(self.centralwidget)
        self.to_left_btn.setGeometry(QtCore.QRect(240, 650, 101, 41))
        self.to_left_btn.setStyleSheet("background-color: rgb(255, 0, 0);")
        self.to_left_btn.setObjectName("to_left_btn")
        self.to_right_btn = QtWidgets.QPushButton(self.centralwidget)
        self.to_right_btn.setGeometry(QtCore.QRect(350, 650, 101, 41))
        self.to_right_btn.setStyleSheet("background-color: rgb(255, 170, 0);")
        self.to_right_btn.setObjectName("to_right_btn")
        self.mirror_btn = QtWidgets.QPushButton(self.centralwidget)
        self.mirror_btn.setGeometry(QtCore.QRect(460, 650, 101, 41))
        self.mirror_btn.setStyleSheet("background-color: rgb(255, 255, 0);")
        self.mirror_btn.setObjectName("mirror_btn")
        self.L_btn = QtWidgets.QPushButton(self.centralwidget)
        self.L_btn.setGeometry(QtCore.QRect(680, 650, 101, 41))
        self.L_btn.setStyleSheet("background-color: rgb(85, 170, 255);")
        self.L_btn.setObjectName("L_btn")
        self.rizkist_btn = QtWidgets.QPushButton(self.centralwidget)
        self.rizkist_btn.setGeometry(QtCore.QRect(570, 650, 101, 41))
        self.rizkist_btn.setStyleSheet("background-color: rgb(85, 170, 0);")
        self.rizkist_btn.setObjectName("rizkist_btn")
        self.list = QtWidgets.QListWidget(self.centralwidget)
        self.list.setGeometry(QtCore.QRect(10, 80, 231, 561))
        self.list.setObjectName("list")
        self.papka_btn = QtWidgets.QPushButton(self.centralwidget)
        self.papka_btn.setGeometry(QtCore.QRect(20, 20, 211, 41))
        self.papka_btn.setObjectName("papka_btn")
        self.Image = QtWidgets.QLabel(self.centralwidget)
        self.Image.setGeometry(QtCore.QRect(266, 32, 511, 601))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Image.setFont(font)
        self.Image.setAlignment(QtCore.Qt.AlignCenter)
        self.Image.setObjectName("Image")
        Image_Editor.setCentralWidget(self.centralwidget)

        self.retranslateUi(Image_Editor)
        QtCore.QMetaObject.connectSlotsByName(Image_Editor)

    def retranslateUi(self, Image_Editor):
        _translate = QtCore.QCoreApplication.translate
        Image_Editor.setWindowTitle(_translate("Image_Editor", "MainWindow"))
        self.to_left_btn.setText(_translate("Image_Editor", "Вліво"))
        self.to_right_btn.setText(_translate("Image_Editor", "Вправо"))
        self.mirror_btn.setText(_translate("Image_Editor", "Дзеркало"))
        self.L_btn.setText(_translate("Image_Editor", "Ч/Б"))
        self.rizkist_btn.setText(_translate("Image_Editor", "Різкість"))
        self.papka_btn.setText(_translate("Image_Editor", "Папка"))
        self.Image.setText(_translate("Image_Editor", "Image"))

        self.papka_btn.clicked.connect(self.open_folder)

    def open_folder(self):
        self.list.clear()
        workdir = QtWidgets.QFileDialog.getExistingDirectory()
        filenames = os.listdir(workdir)
        filenames_filtered = []
        for file in filenames:
            if file.endswith(('.jpg', '.png','.gif', '.jpeg', '.JPG', '.PNG')):
                filenames_filtered.append(file)
        self.list.addItems(filenames_filtered)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Image_Editor = QtWidgets.QMainWindow()
    ui = Ui_Image_Editor()
    ui.setupUi(Image_Editor)
    Image_Editor.show()
    sys.exit(app.exec_())