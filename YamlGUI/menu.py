# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/Users/User/Desktop/untitled.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(330, 350)
        MainWindow.setMinimumSize(QtCore.QSize(330, 350))
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
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.help = QtWidgets.QPushButton(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.help.sizePolicy().hasHeightForWidth())
        self.help.setSizePolicy(sizePolicy)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 219, 77))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 219, 77))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 219, 77))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 219, 77))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 219, 77))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 219, 77))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 219, 77))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 219, 77))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 219, 77))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.help.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.help.setFont(font)
        self.help.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.help.setStyleSheet("QPushButton {\n"
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
        self.help.setIconSize(QtCore.QSize(12, 12))
        self.help.setObjectName("help")
        self.verticalLayout_2.addWidget(self.help)
        self.full = QtWidgets.QPushButton(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.full.sizePolicy().hasHeightForWidth())
        self.full.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.full.setFont(font)
        self.full.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.full.setStyleSheet("QPushButton {\n"
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
        self.full.setIconSize(QtCore.QSize(12, 12))
        self.full.setObjectName("full")
        self.verticalLayout_2.addWidget(self.full)
        self.easy = QtWidgets.QPushButton(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.easy.sizePolicy().hasHeightForWidth())
        self.easy.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.easy.setFont(font)
        self.easy.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.easy.setStyleSheet("QPushButton {\n"
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
        self.easy.setIconSize(QtCore.QSize(12, 12))
        self.easy.setObjectName("easy")
        self.verticalLayout_2.addWidget(self.easy)
        self.setting = QtWidgets.QPushButton(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.setting.sizePolicy().hasHeightForWidth())
        self.setting.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.setting.setFont(font)
        self.setting.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.setting.setStyleSheet("QPushButton {\n"
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
        self.setting.setIconSize(QtCore.QSize(12, 12))
        self.setting.setObjectName("setting")
        self.verticalLayout_2.addWidget(self.setting)
        self.verticalLayout.addWidget(self.groupBox)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox.setTitle(_translate("MainWindow", "Create YAML"))
        self.help.setText(_translate("MainWindow", "Get help"))
        self.full.setText(_translate("MainWindow", "Use full configuration"))
        self.easy.setText(_translate("MainWindow", "Use easy configuration"))
        self.setting.setText(_translate("MainWindow", "Setting"))
