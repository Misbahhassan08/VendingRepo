import sys
import cv2
from PyQt5.QtGui import QPixmap
from PyQt5 import QtCore, QtGui, QtWidgets
from multiscreens import Ui_MainWindow

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        #self.showFullScreen()
        self.init_properties()
        self.pushButton.clicked.connect(self.screens_update)
        self.no_Of_screens = None

    def init_properties(self):
        self.stream_thread = Stream_thread()  
        
    def screens_update(self):
        self.no_Of_screens = self.comboBox.currentText()
        self.no_Of_screens = int(self.no_Of_screens)
        print(self.no_Of_screens)
        if self.no_Of_screens >= 1:
           self.stream_thread.change_pixmap1.connect(self.screen_1.setPixmap)
           #self.screen_5.setText("")
           if self.no_Of_screens >= 2:
              self.stream_thread.change_pixmap2.connect(self.screen_2.setPixmap)
              if self.no_Of_screens >= 3:
                 self.stream_thread.change_pixmap3.connect(self.screen_3.setPixmap)
                 if self.no_Of_screens >= 4:
                    self.stream_thread.change_pixmap.connect(self.screen_4.setPixmap)
                    if self.no_Of_screens >= 5:
                       self.stream_thread.change_pixmap.connect(self.screen_5.setPixmap)
                       if self.no_Of_screens >= 6:
                          self.stream_thread.change_pixmap.connect(self.screen_6.setPixmap)
                          if self.no_Of_screens >= 7:
                             self.stream_thread.change_pixmap.connect(self.screen_7.setPixmap)
                             if self.no_Of_screens >= 8:
                                self.stream_thread.change_pixmap.connect(self.screen_8.setPixmap)
        self.run_video_streaming()

    @QtCore.pyqtSlot(bool)
    def run_video_streaming(self):
        self.stream_thread.start()

class Stream_thread(QtCore.QThread):
    change_pixmap1 = QtCore.pyqtSignal(QtGui.QPixmap)
    change_pixmap2 = QtCore.pyqtSignal(QtGui.QPixmap)
    change_pixmap3 = QtCore.pyqtSignal(QtGui.QPixmap)
    def run(self):
        cap1 = cv2.VideoCapture('rtsp://192.168.31.238:8080/h264_ulaw.sdp')
        cap2 = cv2.VideoCapture(0)
        cap3 = cv2.VideoCapture(1)
        #cap4 = cv2.VideoCapture(0)
        #cap5 = cv2.VideoCapture(0)
        #cap6 = cv2.VideoCapture(0)
        #cap7 = cv2.VideoCapture(0)
        #cap8 = cv2.VideoCapture(0)
        self.thread_is_active = True
        while self.thread_is_active:
            ret, frame = cap1.read()
            if ret:
                width = 1800
                height = 950
                dsize = (width, height)
                output = cv2.resize(frame, dsize, interpolation = cv2.INTER_AREA)
                image = cv2.cvtColor(output, cv2.COLOR_BGR2RGB)
                flipped_image = cv2.flip(image, 1)
                qt_image = QtGui.QImage(flipped_image.data, flipped_image.shape[1], flipped_image.shape[0], QtGui.QImage.Format_RGB888)
                #pic = qt_image.scaled(640, 480, QtCore.Qt.KeepAspectRatio)
                pixmap = QtGui.QPixmap.fromImage(qt_image)
                self.change_pixmap1.emit(pixmap)
                
            ret, frame = cap2.read()
            if ret:
                width = 1800
                height = 950
                dsize = (width, height)
                output = cv2.resize(frame, dsize, interpolation = cv2.INTER_AREA)
                image = cv2.cvtColor(output, cv2.COLOR_BGR2RGB)
                flipped_image = cv2.flip(image, 1)
                qt_image = QtGui.QImage(flipped_image.data, flipped_image.shape[1], flipped_image.shape[0], QtGui.QImage.Format_RGB888)
                #pic = qt_image.scaled(640, 480, QtCore.Qt.KeepAspectRatio)
                pixmap = QtGui.QPixmap.fromImage(qt_image)
                self.change_pixmap2.emit(pixmap)
            ret, frame = cap3.read()
            if ret:
                width = 1800
                height = 950
                dsize = (width, height)
                output = cv2.resize(frame, dsize, interpolation = cv2.INTER_AREA)
                image = cv2.cvtColor(output, cv2.COLOR_BGR2RGB)
                flipped_image = cv2.flip(image, 1)
                qt_image = QtGui.QImage(flipped_image.data, flipped_image.shape[1], flipped_image.shape[0], QtGui.QImage.Format_RGB888)
                #pic = qt_image.scaled(640, 480, QtCore.Qt.KeepAspectRatio)
                pixmap = QtGui.QPixmap.fromImage(qt_image)
                self.change_pixmap3.emit(pixmap)
                
    def stop(self):
        self.thread_is_active = False
        self.quit()
       
         

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec_())