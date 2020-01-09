# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/Users/User/Desktop/setting.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(300, 162)
        MainWindow.setMinimumSize(QtCore.QSize(300, 130))
        MainWindow.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setMinimumSize(QtCore.QSize(230, 100))
        self.groupBox.setStyleSheet("\n"
"\n"
" QGroupBox {\n"
"     font: 12pt \"Arial\";\n"
"    background-color: rgb(255, 255, 255);\n"
"     border: 01px solid gray;\n"
"     border-radius: 5px;\n"
"     margin-top: 1ex; /* оставляем пространство вверху для заголовка */\n"
" }\n"
"\n"
" QGroupBox::title {\n"
"     subcontrol-origin: margin;\n"
"     subcontrol-position: top center; /* помещаем вверху по центру */\n"
"     padding: 0 3px;\n"
"     background-color: rgb(255, 255, 255);\n"
" }")
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.groupBox)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.language = QtWidgets.QPushButton(self.groupBox)
        self.language.setStyleSheet("QPushButton {\n"
"    font: 10pt \"Arial\";\n"
"    padding: 4 ;\n"
"    background-color: #ffdb4d;\n"
"    border: none;\n"
"    border-radius: 10px;\n"
"}\n"
"QPushButton::hover{\n"
"background-color: #fc3;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color: #fc0;\n"
"}\n"
"")
        self.language.setObjectName("language")
        self.horizontalLayout_2.addWidget(self.language)
        self.dark = QtWidgets.QPushButton(self.groupBox)
        self.dark.setStyleSheet("QPushButton {\n"
"    font: 10pt \"Arial\";\n"
"    padding: 4 ;\n"
"    background-color: #ffdb4d;\n"
"    border: none;\n"
"    border-radius: 10px;\n"
"}\n"
"QPushButton::hover{\n"
"background-color: #fc3;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color: #fc0;\n"
"}\n"
"")
        self.dark.setObjectName("dark")
        self.horizontalLayout_2.addWidget(self.dark)
        self.verticalLayout.addWidget(self.groupBox)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox.setTitle(_translate("MainWindow", "Setting"))
        self.language.setText(_translate("MainWindow", "ru/en"))
        self.dark.setText(_translate("MainWindow", "dark theme"))
