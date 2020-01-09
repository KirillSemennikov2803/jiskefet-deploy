import sys
from PyQt5 import QtWidgets
import menu
import help
import full
import easy
import setting
from ipaddress import ip_address
import getpass
import validators
import re

class settingWindow(QtWidgets.QMainWindow, setting.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


class easyWindow(QtWidgets.QMainWindow, easy.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.submit.accepted.connect(self.create_Yaml)

    def use_main(self):
        self.mainWind = mainWindow()
        self.mainWind.show()


    def check_redirectURI(self, redirect):
        if validators.url(redirect):
            if redirect.endswith('/callback'):
                return 0

            else:
                self.err.setText(self.err.text()+ '\n missing postfix / callback. \n correct format: http: // {{ansible_remote_address}} / callback')
                return 1
        else:
            self.err.setText(self.err.text()+ '\n redirect URI was entered incorrectly. \n correct format: http: // {{ansible_remote_address}} / callback')
            return 1

    def check_latin(self, username, name):
        if re.match(r'[A-Za-z0-9]', username) is not None:
            return 0
        else:
            self.err.setText(self.err.text()+ '\n Use only the Latin alphabet and/or numbers when entering '+ name)
            return 1

    def check_host(self, host):
        if host == 'localhost':
                host = '127.0.0.1'
                return 0
        elif host[0:4] == 'http':
            return 0
        else:
            try:
                ip = ip_address(host.split()[0])
            except ValueError:
                self.err.setText('Incorrect IP address')
                return 1
            except IndexError:
                self.err.setText('Bad input IP')
                return 1
            return 0

    def create_Yaml(self):
        checkErr = 0
        self.err.clear()
        hostName = str(self.host.text())
        username = str(self.username.text())
        password = self.password.text()
        DBname = self.DBname.text()
        clientID = self.clientID.text()
        clientSecret = self.clientSecret.text()
        redirectURI = self.redirectURI.text()
        checkErr = self.check_host(hostName)
        checkErr = self.check_latin(username, 'username ')
        checkErr = self.check_latin(DBname, 'database name ')
        checkErr = self.check_latin(clientID, 'client ID ')
        checkErr = self.check_latin(clientSecret, 'client secret ')
        checkErr = self.check_redirectURI(redirectURI)
        if checkErr == 0:
            self.use_main()
            self.close()
        else:
            checkErr = 0



class helpWindow(QtWidgets.QMainWindow, help.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)



class fullWindow(QtWidgets.QMainWindow, full.Ui_MainWindow):
        def __init__(self):
            super().__init__()
            self.setupUi(self)


class mainWindow(QtWidgets.QMainWindow, menu.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.help.clicked.connect(self.get_help)
        self.full.clicked.connect(self.use_full)
        self.full.clicked.connect(self.close)
        self.easy.clicked.connect(self.use_easy)
        self.easy.clicked.connect(self.close)
        self.setting.clicked.connect(self.use_setting)
        self.setting.clicked.connect(self.close)

    def get_help(self):
        self.helpWind = helpWindow()
        self.helpWind.show()

    def use_full(self):
        self.fullWind = fullWindow()
        self.fullWind.show()

    def use_easy(self):
        self.easyWind = easyWindow()
        self.easyWind.show()

    def use_setting(self):
        self.settingWind = settingWindow()
        self.settingWind.show()


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = mainWindow()
    window.show()
    app.exec_()


if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    main()  # то запускаем функцию main()
