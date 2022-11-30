import sys
import cv2
from PyQt5.QtGui import QPixmap
from PyQt5 import QtCore, QtGui, QtWidgets
from multiscreens import Ui_MainWindow

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.init_properties()
        self.pushButton.clicked.connect(self.screens_update)
        self.no_Of_screens = None

    def init_properties(self):
        self.stream_thread_1 = Stream_thread_1() 
        self.stream_thread_2 = Stream_thread_2() 
        self.stream_thread_3 = Stream_thread_3()
        
    def screens_update(self):
        self.no_Of_screens = self.comboBox.currentText()
        self.no_Of_screens = int(self.no_Of_screens)
        print(self.no_Of_screens)
        if self.no_Of_screens >= 1:
           print(self.no_Of_screens)
           self.stream_thread_1.change_pixmap.connect(self.screen_1.setPixmap)
           if self.no_Of_screens >= 2:
              self.stream_thread_2.change_pixmap.connect(self.screen_2.setPixmap)
              if self.no_Of_screens >= 3:
                 self.stream_thread_3.change_pixmap.connect(self.screen_3.setPixmap)
                 if self.no_Of_screens >= 4:
                    self.stream_thread_1.change_pixmap.connect(self.screen_4.setPixmap)
                    if self.no_Of_screens >= 5:
                       self.stream_thread_1.change_pixmap.connect(self.screen_5.setPixmap)
                       if self.no_Of_screens >= 6:
                          self.stream_thread_1.change_pixmap.connect(self.screen_6.setPixmap)
                          if self.no_Of_screens >= 7:
                             self.stream_thread_1.change_pixmap.connect(self.screen_7.setPixmap)
                             if self.no_Of_screens >= 8:
                                self.stream_thread_1.change_pixmap.connect(self.screen_8.setPixmap)
        self.run_all_video_streaming()
    def run_all_video_streaming(self):
        self.stream_thread_1.start()
        self.stream_thread_2.start()
        self.stream_thread_3.start()
class Stream_thread_1(QtCore.QThread):
    change_pixmap = QtCore.pyqtSignal(QtGui.QPixmap)
    
    def run(self):
        cap = cv2.VideoCapture(0)  
        self.thread_is_active = True
        while self.thread_is_active:
            ret, frame = cap.read()
            if ret:
                width = 1800
                height = 950
                dsize = (width, height)
                output = cv2.resize(frame, dsize, interpolation = cv2.INTER_AREA)
                image = cv2.cvtColor(output, cv2.COLOR_BGR2RGB)
                flipped_image = cv2.flip(image, 1)
                qt_image = QtGui.QImage(flipped_image.data, flipped_image.shape[1], flipped_image.shape[0], QtGui.QImage.Format_RGB888)
                pixmap = QtGui.QPixmap.fromImage(qt_image)
                self.change_pixmap.emit(pixmap)
                
    def stop_thread_1(self):
        self.thread_1_is_active = False
        self.quit()

class Stream_thread_2(QtCore.QThread):
    change_pixmap = QtCore.pyqtSignal(QtGui.QPixmap)
    
    def run(self):
        cap = cv2.VideoCapture(1)
        self.thread_is_active = True
        while self.thread_is_active:
            ret, frame = cap.read()
            if ret:
                width = 1800
                height = 950
                dsize = (width, height)
                output = cv2.resize(frame, dsize, interpolation = cv2.INTER_AREA)
                image = cv2.cvtColor(output, cv2.COLOR_BGR2RGB)
                flipped_image = cv2.flip(image, 1)
                qt_image = QtGui.QImage(flipped_image.data, flipped_image.shape[1], flipped_image.shape[0], QtGui.QImage.Format_RGB888)
                pixmap = QtGui.QPixmap.fromImage(qt_image)
                self.change_pixmap.emit(pixmap)
                
    def stop_thread_2(self):
        self.thread_2_is_active = False
        self.quit()
       
class Stream_thread_3(QtCore.QThread):
    change_pixmap = QtCore.pyqtSignal(QtGui.QPixmap)
    
    def run(self):
        cap = cv2.VideoCapture('rtsp://192.168.31.238:8080/h264_ulaw.sdp')
        self.thread_is_active = True
        while self.thread_is_active:
            ret, frame = cap.read()
            if ret:
                width = 1800
                height = 950
                dsize = (width, height)
                output = cv2.resize(frame, dsize, interpolation = cv2.INTER_AREA)
                image = cv2.cvtColor(output, cv2.COLOR_BGR2RGB)
                flipped_image = cv2.flip(image, 1)
                qt_image = QtGui.QImage(flipped_image.data, flipped_image.shape[1], flipped_image.shape[0], QtGui.QImage.Format_RGB888)
                pixmap = QtGui.QPixmap.fromImage(qt_image)
                self.change_pixmap.emit(pixmap)
                
    def stop_thread_3(self):
        self.thread_3_is_active = False
        self.quit()
         

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec_())