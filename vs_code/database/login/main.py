from mainscreen import Mainscreen
from secondscreen import Secondscreen
from database import Database
from PyQt5 import QtCore, QtGui, QtWidgets




class MainScreen(QtWidgets.QWidget,Mainscreen):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.setupUi(self)
    pass # end of GUI file

class SecondScreen(QtWidgets.QWidget,Secondscreen):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.setupUi(self)
    pass # end of GUI file


class _main:
    def __init__(self):
        self.main_screen = MainScreen()
        self.second_screen = SecondScreen()
        self.main_screen.show()
        self.database = Database()
        self.outdata = self.database.get_Data()
        self.main_screen.pushButton.clicked.connect(self.get_pass_user)

        pass    # end of open second screen


    def get_pass_user(self):
        self.get_username = self.main_screen.lineEdit.text()
        self.get_password = self.main_screen.lineEdit_2.text()
        if self.get_username == self.outdata[1]:
            if self.get_password == self.outdata[2]:
                self.second_screen.show()
                self.second_screen.label.setText(str(self.outdata[1]))
                self.second_screen.label1.setText(str(self.outdata[2]))
                print(self.outdata)
            else:
                self.second_screen.show()
                self.second_screen.label.setText("incorrect")
                self.second_screen.label1.setText("Pass|User")
        else:
            self.second_screen.show()
            self.second_screen.label.setText("incorrect")
            self.second_screen.label1.setText("Pass|User")
        pass


    pass



def main():
    app = QtWidgets.QApplication(sys.argv)
    controller = _main()
    sys.exit(app.exec_())
    pass

if __name__ == "__main__":
    import sys
    main()
    pass