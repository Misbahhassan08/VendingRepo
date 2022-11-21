
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_PWM(object):
    
    def setupUi(self, PWM,):
        PWM.setObjectName("PWM")
        PWM.resize(700, 300)
        
        self.label = QtWidgets.QLabel(PWM)
        self.label.setGeometry(QtCore.QRect(20, 50, 71, 20))
        self.label.setTextFormat(QtCore.Qt.TextFormat.RichText)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(PWM)
        self.label_2.setGeometry(QtCore.QRect(20, 90, 71, 20))
        self.label_2.setObjectName("label_2")
        self.label_4 = QtWidgets.QLabel(PWM)
        self.label_4.setGeometry(QtCore.QRect(20, 180, 71, 20))
        self.label_4.setObjectName("label_4")
        self.label_3 = QtWidgets.QLabel(PWM)
        self.label_3.setGeometry(QtCore.QRect(20, 140, 101, 16))
        self.label_3.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.label_3.setObjectName("label_3")
        
        self.dutycycletext = QtWidgets.QTextEdit(PWM)
        self.dutycycletext.setGeometry(QtCore.QRect(150, 130, 241, 31))
        self.dutycycletext.setObjectName("textEdit")
        
        self.frequencytext = QtWidgets.QTextEdit(PWM)
        self.frequencytext.setGeometry(QtCore.QRect(150, 170, 241, 31))
        self.frequencytext.setObjectName("textEdit_1")
        
        self.arduinotext = QtWidgets.QTextEdit(PWM)
        self.arduinotext.setGeometry(QtCore.QRect(400, 130, 280, 160))
        self.arduinotext.setObjectName("textEdit_2")
       
        

        self.dutycycleBar = QtWidgets.QScrollBar(PWM)
        self.dutycycleBar.setGeometry(QtCore.QRect(150, 50, 500, 16))
        self.dutycycleBar.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.dutycycleBar.setObjectName("horizontalScrollBar")
        self.dutycycleBar.setMaximum(100)
        self.dutycycleBar.setMinimum(0)
        
        #self.arduinotext.setSizePolicy(QtWidgets.QSizePolicy.Preferred,QtWidgets.QSizePolicy.Preferred)
        
        
        self.frequencyBar = QtWidgets.QScrollBar(PWM)
        self.frequencyBar.setGeometry(QtCore.QRect(150, 90, 500, 16))
        self.frequencyBar.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.frequencyBar.setObjectName("horizontalScrollBar_2")
        self.frequencyBar.setMaximum(2000)
        self.frequencyBar.setMinimum(800)
        self.retranslateUi(PWM)
        QtCore.QMetaObject.connectSlotsByName(PWM)
        

    def retranslateUi(self, PWM):
        _translate = QtCore.QCoreApplication.translate
        PWM.setWindowTitle(_translate("PWM", "Test"))
        self.label.setText(_translate("PWM", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Dutycycle</span></p></body></html>"))
        self.label_2.setText(_translate("PWM", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Frequency</span></p></body></html>")) 
        self.label_3.setText(_translate("PWM", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">DutyCycle</span></p></body></html>"))
        self.label_4.setText(_translate("PWM", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Frequency</span></p></body></html>"))
        
    


        


if __name__ == "__main__":
    
    import sys
    app = QtWidgets.QApplication(sys.argv)
    PWM = QtWidgets.QDialog()
    ui = Ui_PWM()
    ui.setupUi(PWM)
    PWM.show()
    sys.exit(app.exec())



