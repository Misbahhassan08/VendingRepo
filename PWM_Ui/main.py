from RPI import RPI_Class
from UI import Ui_PWM
from PyQt5 import QtCore, QtGui, QtWidgets
import pigpio
from time import sleep
import threading
# interface of UI file
class GUI(QtWidgets.QWidget,Ui_PWM):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.setupUi(self)
    pass # end of GUI file

# main class strating point of program
class _main(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.rpi = RPI_Class()
        self.gui = GUI()
        
        self.gui.show()
        self.rpi.signalFlow.connect(self.serial_data)
        self.gui.dutycycleBar.sliderMoved.connect(self.sliderval1)
        
        
        
    def sliderval1(self):
        self.dutycycle = self.gui.dutycycleBar.value()
        self.gui.dutycycletext.setText(str(self.dutycycle))
        self.rpi.hard_pwm(18,800,int(self.dutycycle))
    
    
    def serial_data(self,Data,Name):
        self.Data = Data
        self.Name = Name
        print(self.Name,self.Data)
        self.gui.arduinotext.append(self.Data)
        
        
def main():
    app = QtWidgets.QApplication(sys.argv)
    controller = _main()
    controller.start()
    sys.exit(app.exec_())
    
if __name__ == "__main__":
    import sys
    main()


