# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design_gui.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setMaximumSize(QtCore.QSize(1280, 720))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.btnLoadImg = QtWidgets.QPushButton(self.centralwidget)
        self.btnLoadImg.setGeometry(QtCore.QRect(20, 600, 221, 25))
        self.btnLoadImg.setObjectName("btnLoadImg")
        self.verticalLayout.addWidget(self.btnLoadImg)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(270, 600, 81, 21))
        self.label.setObjectName("label")
        self.lbl_path = QtWidgets.QLabel(self.centralwidget)
        self.lbl_path.setGeometry(QtCore.QRect(370, 600, 67, 17))
        self.lbl_path.setText("")
        self.lbl_path.setObjectName("lbl_path")
        self.lblImage = QtWidgets.QLabel(self.centralwidget)
        self.lblImage.setMaximumSize(QtCore.QSize(1200, 600))
        self.lblImage.setText("")
        self.lblImage.setObjectName("lblImage")
        self.verticalLayout.addWidget(self.lblImage)  
        MainWindow.setCentralWidget(self.centralwidget)
     

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Object Detection v1.0 by OK"))
        self.btnLoadImg.setText(_translate("MainWindow", "Load Image"))
        self.label.setText(_translate("MainWindow", "Img Path:"))
