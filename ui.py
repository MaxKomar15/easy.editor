# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 597)
        MainWindow.setStyleSheet("background: #442ebf;\n"
"color: black;\n"
"font size: 20px;")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.folder_btn = QtWidgets.QPushButton(self.centralwidget)
        self.folder_btn.setGeometry(QtCore.QRect(0, 0, 101, 41))
        self.folder_btn.setStyleSheet("background:#2ebf55;\n"
"border:3px solid black;\n"
"border-radius: 12px;")
        self.folder_btn.setObjectName("folder_btn")
        self.save_btn = QtWidgets.QPushButton(self.centralwidget)
        self.save_btn.setGeometry(QtCore.QRect(10, 510, 111, 41))
        self.save_btn.setStyleSheet("background:#fa0202;\n"
"border:3px solid black;\n"
"border-radius: 12px;")
        self.save_btn.setObjectName("save_btn")
        self.right_btn = QtWidgets.QPushButton(self.centralwidget)
        self.right_btn.setGeometry(QtCore.QRect(110, 0, 111, 41))
        self.right_btn.setStyleSheet("background:#2ebf55;\n"
"border:3px solid black;\n"
"border-radius: 12px;")
        self.right_btn.setObjectName("right_btn")
        self.left_btn = QtWidgets.QPushButton(self.centralwidget)
        self.left_btn.setGeometry(QtCore.QRect(230, 0, 101, 41))
        self.left_btn.setStyleSheet("background:#2ebf55;\n"
"border:3px solid black;\n"
"border-radius: 12px;")
        self.left_btn.setObjectName("left_btn")
        self.edit_btn = QtWidgets.QPushButton(self.centralwidget)
        self.edit_btn.setGeometry(QtCore.QRect(340, 0, 81, 41))
        self.edit_btn.setStyleSheet("background:#2ebf55;\n"
"border:3px solid black;\n"
"border-radius: 12px;")
        self.edit_btn.setObjectName("edit_btn")
        self.BW_btn = QtWidgets.QPushButton(self.centralwidget)
        self.BW_btn.setGeometry(QtCore.QRect(430, 0, 81, 41))
        self.BW_btn.setStyleSheet("background:#2ebf55;\n"
"border:3px solid black;\n"
"border-radius: 12px;")
        self.BW_btn.setObjectName("BW_btn")
        self.image_label = QtWidgets.QLabel(self.centralwidget)
        self.image_label.setGeometry(QtCore.QRect(170, 60, 621, 481))
        self.image_label.setStyleSheet("color:white;\n"
"border: 3px solid black;\n"
"border-radius: 12px;\n"
"")
        self.image_label.setObjectName("image_label")
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(520, 0, 80, 41))
        self.pushButton_7.setStyleSheet("background:#2ebf55;\n"
"border:3px solid black;\n"
"border-radius: 12px;")
        self.pushButton_7.setObjectName("pushButton_7")
        self.mirror_btn = QtWidgets.QPushButton(self.centralwidget)
        self.mirror_btn.setGeometry(QtCore.QRect(520, 0, 80, 41))
        self.mirror_btn.setStyleSheet("background:#2ebf55;\n"
"border:3px solid black;\n"
"border-radius: 12px;")
        self.mirror_btn.setObjectName("mirror_btn")
        self.image_list = QtWidgets.QListWidget(self.centralwidget)
        self.image_list.setGeometry(QtCore.QRect(10, 60, 131, 441))
        self.image_list.setStyleSheet("color:white;\n"
"border: 3px solid black;\n"
"border-radius: 12px;\n"
"")
        self.image_list.setObjectName("image_list")
        self.back_btn = QtWidgets.QPushButton(self.centralwidget)
        self.back_btn.setGeometry(QtCore.QRect(610, 0, 80, 41))
        self.back_btn.setStyleSheet("background:#2ebf55;\n"
"border:3px solid black;\n"
"border-radius: 12px;")
        self.back_btn.setObjectName("back_btn")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "easy.editor"))
        self.folder_btn.setText(_translate("MainWindow", "Відкрити папку"))
        self.save_btn.setText(_translate("MainWindow", "Зберегти"))
        self.right_btn.setText(_translate("MainWindow", "Повернути вправо"))
        self.left_btn.setText(_translate("MainWindow", "Повернути вліво"))
        self.edit_btn.setText(_translate("MainWindow", "Редагувати"))
        self.BW_btn.setText(_translate("MainWindow", "Чорно-білий"))
        self.image_label.setText(_translate("MainWindow", "Зображення"))
        self.pushButton_7.setText(_translate("MainWindow", "Відзеркалення"))
        self.mirror_btn.setText(_translate("MainWindow", "Відзеркалення"))
        self.back_btn.setText(_translate("MainWindow", "Крок назад"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
