from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow, QFileDialog
from PyQt5.QtGui import QPixmap
from ui import Ui_MainWindow
import os
from PIL import Image, ImageFilter, ImageOps

class EasyEditor(QMainWindow):
    def   __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.workdir = None
        self.filename = None
        self.last_image = None        
        self.image = None
        self.save_folder = "Edited/"
        self.image_name = None
        self.connects()

    def connects(self):
        self.ui.folder_btn.clicked.connect(self.choose_folder)
        # self.ui.action.triggered.connect(self.choose_folder)
        self.ui.image_list.currentRowChanged.connect(self.show_chosen_image)
        self.ui.BW_btn.clicked.connect(self.do_black)
        self.ui.left_btn.clicked.connect(self.do_left)
        self.ui.right_btn.clicked.connect(self.do_right)
        self.ui.mirror_btn.clicked.connect(self.do_mirror)
        self.ui.back_btn.clicked.connect(self.do_back)
        


    def filter(self, filenames):
        images = []
        for filename in filenames:
            if filename.endswith(".jpg") or filename.endswith(".png") or filename.endswith(".jpeg"):
                images.append(filename)

        return images

    def show_image_list(self):
        filenames = os.listdir(self.workdir)
        self.ui.image_list.clear()
        images = self.filter(filenames)
        self.ui.image_list.addItems(images)

    def choose_folder(self):
        try:
            self.workdir = QFileDialog.getExistingDirectory()
            self.show_image_list()
        except:
            pass

    def load_image(self, filename):
        self.image_name = filename
        self.filename = os.path.join(self.workdir, filename)
        self.image  = Image.open(self.filename)
       



    def show_image(self):
        self.ui.image_label.hide()
        h =self.ui.image_label.height()
        w =self.ui.image_label.width()
        
        pm_image = QPixmap(self.filename)
        pm_image = pm_image.scaled(w, h, Qt.KeepAspectRatio)
        self.ui.image_label.setPixmap(pm_image)
        self.ui.image_label.show()

    def show_chosen_image(self):
        if self.ui.image_list.currentRow() >= 0:
            filename = self.ui.image_list.currentItem().text()
            self.load_image(filename)
            self.show_image()

    def save_image(self):
        path = os.path.join(self.workdir, self.save_folder)
        if not(os.path.exists(path) or os.path.isdir(path)):
            os.mkdir(path)
        self.filename = os.path.join(path, self.image_name)

        self.image.save(self.filename)
        

    def do_black(self):
        if self.image:
            self.last_image = self.image
            self.image = self.image.convert("L")
            self.save_image()
            self.show_image()

    def do_left(self):
        if self.image:
            self.last_image = self.image
            self.image = self.image.transpose(Image.ROTATE_90)
            self.save_image()
            self.show_image()

    def do_right(self):
        if self.image:
            self.last_image = self.image
            self.image = self.image.transpose(Image.ROTATE_270)
            self.save_image()
            self.show_image()

    def do_mirror(self):
        if self.image:
            self.last_image = self.image
            self.image =ImageOps.mirror(self.image)
            self.save_image()
            self.show_image()

    def do_back(self):

        if self.image and self.last_image:
            self.image = self.last_image
            self.save_image()
            self.show_image()


app = QApplication([])
ex = EasyEditor()
ex.show()
app.exec_()
