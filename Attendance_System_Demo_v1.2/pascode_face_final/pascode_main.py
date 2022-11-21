import sys
from UI_video_pascode import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
import threading
from keypad import keypad_4x4
from PyQt5.QtCore import QThread,pyqtSignal
from facial_req_class import faceRecognition_thread
from time import sleep

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent=parent)
        self.id = None
        self.name = None
        self.face_name = None
        self.NID = ""
        #self.showFullScreen()
        self.setupUi(self)
        self.init_properties()
        self.init_connections()


    def init_properties(self):
        self.Face_Recognition_thread = faceRecognition_thread()
        
    def init_connections(self):
        self.Face_Recognition_thread.change_pixmap.connect(self.image_label.setPixmap)
        self.Face_Recognition_thread.Passcode_signalFlow.connect(self.pascode_data)
        self.Face_Recognition_thread.Face_signalFlow.connect(self.face_Name)
        
        self.run_video_streaming()

    @QtCore.pyqtSlot(bool)
    def run_video_streaming(self):
        self.Face_Recognition_thread.start()
        pass
    def face_Name(self,Face_name):
        self.face_name = Face_name
        self.chek_loop()
        self.face_name = ""
        pass
    def pascode_data(self,ID,Name):
        self.id = ID
        self.name = Name
        self.NID += self.id
        print(self.NID)
        self.label.setText(f"{self.NID}")
        self.chek_loop()
        pass
    def chek_loop(self):
        if self.id == "C":
           print("Clear")           
           self.id = None
           self.label.setText("Please Enter Your Pascode :")
           self.NID = ""
        elif self.NID == "126107":
             self.label.setText(f"With ID : {self.NID} Please Show Your Face..")
             if self.face_name == self.NID:
                self.label.setText(f"ID : {self.face_name} Present...")
                self.id = ""
                self.face_name = ""
        pass
    
    '''
        if self.id == "C":
           print("Clear")           
           self.id = None
           self.label.setText("Please Enter Your Pascode :")
           self.NID = ""
            
        elif self.NID == "123456":
             self.label.setText("Shafique ur Rehman Please Show Your Face..")
             if self.face_name == "Shafique ur Rehman":
                self.label.setText("Shafique ur Rehman Present...")
                self.NID = ""
                self.face_name = ""
                
        elif self.NID == "126107":
             self.label.setText("Muhammad Atif Rafique Please Show Your Face..")
             if self.face_name == "Muhammad Atif Rafique":
                self.label.setText("Muhammad Atif Rafique Present...")
                self.id = ""
                self.face_name = ""
        elif self.NID == "654321":
             self.label.setText("Sayed Ali Sarmad Please Show Your Face..")
             if self.face_name == "Sayed Ali Sarmad":
                self.label.setText("Sayed Ali Sarmad Present...")
                self.NID = ""
                self.face_name = ""
        elif self.NID == "111222":
             self.label.setText("Sayed Muhammad Aftab Please Show Your Face..")
             if self.face_name == "Sayed Muhammad Aftab":
                self.label.setText("Sayed Muhammad Aftab Present...")
                self.id = ""
                self.face_name = ""
        elif self.NID == "786786":
             self.label.setText("Jahangir Afzal Please Show Your Face..")
             if self.face_name == "Jahangir Afzal":
                self.label.setText("Jahangir Afzal Present...")
                self.NID = ""
                self.face_name = ""
             '''   
    
       
class _main():
    def __init__(self):
        
        self.mainwindow = MainWindow()
        
        self.mainwindow.show()
        #self.mainwindow.label.setText("Atif")
    pass
    
    

def main():
    app = QtWidgets.QApplication(sys.argv)
    w = _main()
    sys.exit(app.exec_())
    pass
       
         

if __name__ == "__main__":
    
    main()
    pass
         
