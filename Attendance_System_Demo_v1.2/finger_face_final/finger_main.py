import sys
from UI_video_finger import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from facial_req_class import faceRecognition_thread

import time


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent=parent)
        self.id = None
        self.name = None
        self.face_name = None
        self.showFullScreen()
        self.setupUi(self)
        self.init_properties()
        self.init_connections()
        
    def init_properties(self):
        self.Face_Recognition_thread = faceRecognition_thread()
        
    def init_connections(self):
        self.Face_Recognition_thread.change_pixmap.connect(self.image_label.setPixmap)
        self.Face_Recognition_thread.Finger_signalFlow.connect(self.finger_data)
        self.Face_Recognition_thread.Face_signalFlow.connect(self.face_Name)
        
        self.run_video_streaming()

    @QtCore.pyqtSlot(bool)
    def run_video_streaming(self):
        self.Face_Recognition_thread.start()
    def face_Name(self,Face_name,From):
        self.face_name = Face_name
        self.chek_loop()
        self.face_name = ""

        pass
    def finger_data(self,ID,Name):
        self.id = ID
        self.name = Name
        self.chek_loop()
        
        pass
    def chek_loop(self):
        if self.id == "3":
           self.label.setText(f"Your ID : {self.id} Please Show Your Face..")
           if self.face_name == self.id:
              self.label.setText(f"With ID : {self.id} Present...")
              self.id = ""
              self.face_name = ""
        '''
        if self.id == "1":  
           self.label.setText("Shafique ur Rehman Please Show Your Face..")
           if self.face_name == "Shafique ur Rehman":
               self.id = ""
               self.label.setText("Shafique ur Rehman Rafique Present...")
               self.face_name = ""
        elif self.id == "2":
           self.label.setText("Shafique ur Rehman Please Show Your Face..")
           if self.face_name == "Shafique ur Rehman":
               self.id = ""
               self.label.setText("Shafique ur Rehman Present...")
               self.face_name = ""
        elif self.id == "3":
           print(f"in chek_loop in if {self.id}")
           self.label.setText("Muhammad Atif Rafique Please Show Your Face..")
           if self.face_name == "Muhammad Atif Rafique":
               self.id = ""
               self.label.setText("Muhammad Atif Rafique Present...")
               self.face_name = ""
        elif self.id == "4":
           self.label.setText("Muhammad Atif Rafique Please Show Your Face..")
           if self.face_name == "Muhammad Atif Rafique":
               self.id = ""
               self.label.setText("Muhammad Atif Rafique Present...")
               self.face_name = ""
        elif self.id == "5":
           self.label.setText("Sayed Ali Sarmad Please Show Your Face..")
           if self.face_name == "Sayed Ali Sarmad":
               self.id = ""
               self.label.setText("Sayed Ali Sarmad Present...")
               self.face_name = ""
        elif self.id == "6":
           self.label.setText("Sayed Ali Sarmad Please Show Your Face..")
           if self.face_name == "Sayed Ali Sarmad":
               self.id = ""
               self.label.setText("Sayed Ali Sarmad Present...")
               self.face_name = ""
        elif self.id == "7":
           self.label.setText("Sayed Muhammad Aftab Please Show Your Face..")
           if self.face_name == "Sayed Muhammad Aftab":
               self.id = ""
               self.label.setText("Sayed Muhammad Aftab Present...")
               self.face_name = ""
        elif self.id == "8":
           self.label.setText("Sayed Muhammad Aftab Please Show Your Face..")
           if self.face_name == "Sayed Muhammad Aftab":
               self.id = ""
               self.label.setText("Sayed Muhammad Aftab Present...")
               self.face_name = ""
        elif self.id == "9":
           self.label.setText("Jahangir Afzal Please Show Your Face..")
           if self.face_name == "Jahangir Afzal":
               self.id = ""
               self.label.setText("Jahangir Afzal Present...")
               self.face_name = ""
        elif self.id == "10":
           self.label.setText("Jahangir Afzal Please Show Your Face..")
           if self.face_name == "Jahangir Afzal":
               self.id = ""
               self.label.setText("Jahangir Afzal Present...")
               self.face_name = ""
        '''
               
        pass


            
            
        
class _main():
    def __init__(self):
        #self.Face_Recognition_thread = faceRecognition_thread()
        
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
    
    
    
    