
from PyQt5 import QtCore, QtGui, QtWidgets

class Secondscreen(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setWindowModality(QtCore.Qt.WindowModality.WindowModal)
        Form.resize(250, 200)
        Form.setStyleSheet("")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(70, 14, 120, 34))
        self.label.setMinimumSize(QtCore.QSize(41, 0))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.label.setLineWidth(1)
        self.label.setMidLineWidth(0)
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")

        self.label1 = QtWidgets.QLabel(Form)
        self.label1.setGeometry(QtCore.QRect(70, 70, 120, 34))
        self.label1.setMinimumSize(QtCore.QSize(41, 0))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label1.setFont(font)
        self.label1.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.label1.setLineWidth(1)
        self.label1.setMidLineWidth(0)
        self.label1.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label1.setObjectName("label1")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        _translate = QtCore.QCoreApplication.translate
        #self.label.setText(_translate("Form", "Username"))
        #self.label1.setText(_translate("Form", "password"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Secondscreen()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec())
