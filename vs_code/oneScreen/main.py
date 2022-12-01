import sys
import cv2
from PyQt5.QtGui import QPixmap
from PyQt5 import QtCore, QtGui, QtWidgets
from onescreen import Ui_MainWindow

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.stream_thread = Stream_thread()
        self.set_screen_btn.clicked.connect(self.screens_update)
        self.close_button.clicked.connect(self.close)
        self.select_screens = None
       
    def screens_update(self):
        self.select_screens = self.comboBox.currentText()
        if self.select_screens == "You want to play video":
           self.stream_thread.video_Start()
           self.stream_thread.change_pixmap.connect(self.screen_1.setPixmap)
           self.label.setText("Status : You are playing video")
        elif self.select_screens == "You want to play camera":
             self.stream_thread.camera_Start()
             self.stream_thread.change_pixmap.connect(self.screen_1.setPixmap)
             self.label.setText("Status : You are playing camera")
             
        self.stream_thread.start()

class Stream_thread(QtCore.QThread):
    change_pixmap = QtCore.pyqtSignal(QtGui.QPixmap)
    def __init__(self):
        QtCore.QThread.__init__(self)
        self.video_active = None
        self.camera_active = None
        self.frame_counter = 0
        self.thread_is_active = True 
        pass   # end of __init__ constructer
    def run(self):
        cap1 = cv2.VideoCapture('Videos\VID-20221007-WA0001.mp4')
        cap2 = cv2.VideoCapture(0)       
        while self.thread_is_active:
            if self.video_active:
               self.frame_counter += 1
               ret, frame = cap1.read()
               if self.frame_counter == cap1.get(cv2.CAP_PROP_FRAME_COUNT):
                  self.frame_counter = 0 #Or whatever as long as it is the same as next line
                  cap1.set(cv2.CAP_PROP_POS_FRAMES, 0)
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
            if self.camera_active:
                ret, frame = cap2.read()              
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
    def stop(self):
        self.thread_is_active = False
        self.quit()
    def video_Start(self):
        self.video_active = True
        self.camera_active = False
        pass    # end od video active
    def camera_Start(self):
        self.camera_active = True
        self.video_active = False
        pass    # end od video active
         
def main():
    app = QtWidgets.QApplication(sys.argv)
    controller = MainWindow()
    controller.showFullScreen()
    sys.exit(app.exec_())
    pass  # end of main()
if __name__ == "__main__":
    import sys
    main()
    pass   # end of if __name__