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
import io
import yaml

class settingWindow(QtWidgets.QMainWindow, setting.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


class easyWindow(QtWidgets.QMainWindow, easy.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.submit.accepted.connect(self.create_Yaml)
        self.submit.rejected.connect(self.use_main)

    def use_main(self):
        self.mainWind = mainWindow()
        self.mainWind.show()
        self.close()


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

    def use_template(self, hostName, username, password, DBname, clientID, clientSecret, redirectURI):
        with io.open('template.yml') as f:
                templates = yaml.safe_load(f)
        api_general_settings = {'TYPEORM_HOST': hostName,
                                'TYPEORM_USERNAME': username,
                                'TYPEORM_PASSWORD': password,
                                'TYPEORM_DATABASE': DBname
                                }
        oauth_settings = {'CLIENT_ID': clientID,
                          'CLIENT_SECRET': clientSecret,
                          'AUTH_REDIRECT_URI': redirectURI
                          }
        remote_repository_url = {'JISKEFET_API': 'https://github.com/SoftwareForScience/jiskefet-api.git',
                                 'JISKEFET_UI': 'https://github.com/SoftwareForScience/jiskefet-ui.git'
                                 }
        templates.update({'jiskefet_api_general_settings': api_general_settings})
        templates.update({'jiskefet_oauth_settings': oauth_settings})
        templates.update({'remote_repository_url': remote_repository_url})
        with io.open('ansible.config.yml', 'w') as f:
            yaml.dump(templates, f)

            
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
            self.use_template(hostName, username, password, DBname, clientID, clientSecret, redirectURI)
            self.use_main()
            
        else:
            checkErr = 0



class helpWindow(QtWidgets.QMainWindow, help.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        with io.open('help') as f:
                helpText = f.read()
        self.helpBrowser.setText(helpText)
    


class fullWindow(QtWidgets.QMainWindow, full.Ui_MainWindow):
    def view_label (self):
        if self.cern.checkState() == 2:
            self.cernURIlabel.setEnabled(True)
            self.cernURI.setEnabled(True)
        else:
            self.cernURIlabel.setDisabled(True)
            self.cernURI.setDisabled(True)

    
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.cernURIlabel.setDisabled(True)
        self.cernURI.setDisabled(True)
        self.cern.stateChanged.connect(self.view_label)
        self.submit.accepted.connect(self.create_Yaml)
        self.submit.rejected.connect(self.use_main)
    
            
    def use_main(self):
        self.mainWind = mainWindow()
        self.mainWind.show()
        self.close()


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

    def use_template(self, hostName, username, password, DBname, clientID, clientSecret, redirectURI, local, cern, cernURI, testDBhost, testDBusername, testDBpassword):
        with io.open('template.yml') as f:
                templates = yaml.safe_load(f)
        api_general_settings = {'TYPEORM_HOST': hostName,
                                'TYPEORM_USERNAME': username,
                                'TYPEORM_PASSWORD': password,
                                'TYPEORM_DATABASE': DBname
                                }
        oauth_settings = {'CLIENT_ID': clientID,
                          'CLIENT_SECRET': clientSecret,
                          'AUTH_REDIRECT_URI': redirectURI
                          }
        remote_repository_url = {'JISKEFET_API': 'https://github.com/SoftwareForScience/jiskefet-api.git',
                                 'JISKEFET_UI': 'https://github.com/SoftwareForScience/jiskefet-ui.git'
                                 }
        local_Repo = {'use_local_repository': local}
        CERN_SSO = {'USE_CERN_SSO': cern}
        CERN_registered_uri = {'CERN_REGISTERED_URI':''}
        if CERN_SSO.get('USE_CERN_SSO') == 'true':
            CERN_registered_uri = {'CERN_REGISTERED_URI': cernURI }
        api_optional_settings = {'TEST_DB_HOST': testDBhost,
                                 'TEST_DB_USERNAME': testDBusername,
                                 'TEST_DB_PASSWORD': testDBpassword
                                 }
        templates.update({'jiskefet_api_optional_settings': api_optional_settings})
        templates.update(local_Repo)
        templates.update(CERN_SSO)
        templates.update({'CERN_registered_uri': CERN_registered_uri})
        templates.update({'jiskefet_api_general_settings': api_general_settings})
        templates.update({'jiskefet_oauth_settings': oauth_settings})
        templates.update({'remote_repository_url': remote_repository_url})
        with io.open('ansible.config.yml', 'w') as f:
            yaml.dump(templates, f)

            
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
                self.err.setText(self.err.text() + 'Incorrect IP address')
                return 1
            except IndexError:
                self.err.setText(self.err.text() + 'Bad input IP')
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
        if self.local.checkState() == 2:
            local = 'yes'
        else:
            local = 'no'

        if self.cern.checkState() == 2:
            cern = 'true'
            cernURI = self.cernURI.text()
        else:
            cern = 'false'
            cernURI = ""
        testDBhost = str(self.testDBhost.text()) 
        testDBusername = str(self.testDBname.text()) 
        testDBpassword = str(self.testDBpassword.text()) 
        checkErr = self.check_host(hostName)
        checkErr = self.check_latin(username, 'username ')
        checkErr = self.check_latin(DBname, 'database name ')
        checkErr = self.check_latin(clientID, 'client ID ')
        checkErr = self.check_latin(clientSecret, 'client secret ')
        checkErr = self.check_redirectURI(redirectURI)
        checkErr = self.check_latin(cernURI, 'CERN URI ')
        checkErr = self.check_host(testDBhost)
        checkErr = self.check_latin(testDBusername, 'test database name ')
        if checkErr == 0:
            self.use_template(hostName, username, password, DBname, clientID, clientSecret, redirectURI, local, cern, cernURI, testDBhost, testDBusername, testDBpassword)
            self.use_main()
            self.close()
        else:
            checkErr = 0
        se


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


if __name__ == '__main__': 
    main()  # то запускаем функцию main()
