import sys
from UI_video_rfid import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
import threading
from RFID import Reader
from PyQt5.QtCore import QThread,pyqtSignal
from face_recognition_class import faceRecognition_thread

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
        self.reader = Reader()
        
    def init_connections(self):
        self.Face_Recognition_thread.change_pixmap.connect(self.image_label.setPixmap)
        self.reader.signalFlow.connect(self.rfid_data)
        self.Face_Recognition_thread.Face_signalFlow.connect(self.face_Name)
        
        self.run_video_streaming()

    @QtCore.pyqtSlot(bool)
    def run_video_streaming(self):
        self.Face_Recognition_thread.start()
    def rfid_data(self,ID,Name):
        self.id = ID
        print(self.id)
        self.name = Name
        self.chek_loop()
        pass
    def face_Name(self,Face_name):
        self.face_name = Face_name
        self.chek_loop()
        self.face_name = ""
        pass
    def chek_loop(self):
        
        if self.id == "419700483814":
           self.label.setText("Shafique ur Rehman Please Show Your Face..")
           if self.face_name == "Shafique ur Rehman":
               self.id = ""
               self.label.setText("Shafique ur Rehman Present...")
               self.face_name = ""
        elif self.id == "417650910869":
           self.label.setText("Muhammad Atif Rafique Please Show Your Face..")
           if self.face_name == "Muhammad Atif Rafique":
               self.id = ""
               self.label.setText("Muhammad Atif Rafique Present...")
               self.face_name = ""
        elif self.id == "1076670962393":
           self.label.setText("Sayed Ali Sarmad Please Show Your Face..")
           if self.face_name == "Sayed Ali Sarmad":
               self.id = ""
               self.label.setText("Sayed Ali Sarmad Present...")
               self.face_name = ""
        elif self.id == "412488440394":
           self.label.setText("Sayed Muhammad Aftab Please Show Your Face..")
           if self.face_name == "Sayed Muhammad Aftab":
               self.id = ""
               self.label.setText("Sayed Muhammad Aftab Present...")
               self.face_name = ""
        elif self.id == "757966053799":
           self.label.setText("Jahangir Afzal Please Show Your Face..")
           if self.face_name == "Jahangir Afzal":
               self.id = ""
               self.label.setText("Jahangir Afzal Present...")
               self.face_name = ""
        pass
       
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