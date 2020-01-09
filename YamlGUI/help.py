# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/Users/User/Desktop/full.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 600)
        MainWindow.setMinimumSize(QtCore.QSize(600, 600))
        MainWindow.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(230)
        sizePolicy.setVerticalStretch(250)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setMinimumSize(QtCore.QSize(230, 250))
        self.groupBox.setStyleSheet("\n"
"\n"
" QGroupBox {\n"
"     font: 12pt \"Arial\";\n"
"    background-color: rgb(255, 255, 255);\n"
"     border: 01px solid gray;\n"
"     border-radius: 5px;\n"
"     margin-top: 1ex; \n"
"    padding:2px;\n"
" }\n"
"\n"
" QGroupBox::title {\n"
"     subcontrol-origin: margin;\n"
"     subcontrol-position: top center; \n"
"     padding: 0 3px;\n"
"     background-color: rgb(255, 255, 255);\n"
" }")
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.groupBox)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.helpBrowser = QtWidgets.QTextBrowser(self.groupBox)
        self.helpBrowser.setMinimumSize(QtCore.QSize(0, 0))
        self.helpBrowser.setStyleSheet("margin: 5px;\n"
"border:none;")
        self.helpBrowser.setObjectName("helpBrowser")
        self.horizontalLayout_2.addWidget(self.helpBrowser)
        self.verticalLayout.addWidget(self.groupBox)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox.setTitle(_translate("MainWindow", "Help"))
