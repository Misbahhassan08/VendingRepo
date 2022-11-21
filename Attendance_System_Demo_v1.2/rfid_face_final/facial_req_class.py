#! /usr/bin/python

#! /usr/bin/python

# import the necessary packages
import cv2
import face_recognition
from imutils.video import VideoStream
from imutils.video import FPS
import imutils
import pickle
from PyQt5.QtCore import QThread,pyqtSignal
from PyQt5 import QtCore, QtGui, QtWidgets
from RFID import Reader

class faceRecognition_thread(QtCore.QThread):
    change_pixmap = QtCore.pyqtSignal(QtGui.QPixmap)
    Face_signalFlow = pyqtSignal(str,str,name='Face_signal')
    Rfid_signalFlow = pyqtSignal(str,str,name='Rfid_signal')
    def __init__(self):
        QtCore.QThread.__init__(self)
        self.currentname = "unknown"
        self.encodingsP = "encoding.pickle"
        self.model_Folder = 'Model'
        self.rfid_Id = 0
        self.scan_id = True
        self.data = None     
        print("[INFO] loading encodings + face detector...")
        self.vs = cv2.VideoCapture(0)
        #vs = VideoStream(usePiCamera=True).start()
        #time.sleep(2.0)

        # start the FPS counter
        self.fps = FPS().start()
        self.reader = Reader()
        pass # end of init function
        
    def run(self):
        while True:
            # grab the frame from the threaded video stream and resize it
            # to 500px (to speedup processing)
            ret,frame = self.vs.read()
            frame = imutils.resize(frame, width=500)    
                #cv2.imshow("Video Streaming", frame1)
            
            if self.scan_id:
                self.rfid_Id = self.reader.get_id()
                if self.rfid_Id == 417650910869:
                    self.Rfid_signalFlow.emit(str(self.rfid_Id),'RFID Data')
                    print(f"RFID ID: {self.rfid_Id}")
                    print("Pickle file loading Done ")
                    self.data = pickle.loads(open(f"{self.rfid_Id}/{self.model_Folder}/{self.encodingsP}", "rb").read())
                    self.scan_id = False
                    
            if self.rfid_Id == 417650910869:
                # Detect the fce boxes
                boxes = face_recognition.face_locations(frame)
                # compute the facial embeddings for each face bounding box
                encodings = face_recognition.face_encodings(frame, boxes)
                names = []
                # loop over the facial embeddings
                for encoding in encodings:
                    # attempt to match each face in the input image to our known
                    # encodings
                    matches = face_recognition.compare_faces(self.data["encodings"],
                            encoding)
                    name = "Unknown" #if face is not recognized, then print Unknown

                    # check to see if we have found a match
                    if True in matches:
                        # find the indexes of all matched faces then initialize a
                        # dictionary to count the total number of times each face
                        # was matched
                        matchedIdxs = [i for (i, b) in enumerate(matches) if b]
                        counts = {}

                        # loop over the matched indexes and maintain a count for
                        # each recognized face face
                        for i in matchedIdxs:
                            name = self.data["names"][i]
                            counts[name] = counts.get(name, 0) + 1
                            #print(name)

                        # determine the recognized face with the largest number
                        # of votes (note: in the event of an unlikely tie Python
                        # will select first entry in the dictionary)
                        name = max(counts, key=counts.get)

                        #If someone in your dataset is identified, print their name on the screen
                        #If someone in your dataset is identified, print their name on the screen
                        if self.currentname:
                            self.currentname = name
                            self.sname = self.currentname
                            self.Face_signalFlow.emit(self.sname,'Face_Recognition')
                            self.sname = ""
                           

                    # update the list of names  mis
                    names.append(name) # 2 minutes
                    if len(names) > 0:
                        self.scan_id = True
                        self.rfid_Id = 0  

                # loop over the recognized faces
                for ((top, right, bottom, left), name) in zip(boxes, names):
                    # draw the predicted face name on the image - color is in BGR
                    cv2.rectangle(frame, (left, top), (right, bottom),
                            (0, 255, 225), 2)
                    y = top - 15 if top - 15 > 15 else top + 15
                    cv2.putText(frame, name, (left, y), cv2.FONT_HERSHEY_SIMPLEX,
                            .8, (0, 255, 255), 2)

                # display the image to our screen
            # display the image to our screen
            #percent by which the image is resized
            scale_percent = 100

            #calculate the 50 percent of original dimensions
            width = 1800
            height = 1500

            # dsize
            dsize = (width, height)

            # resize image
            output = cv2.resize(frame, dsize, interpolation = cv2.INTER_AREA)
            image = cv2.cvtColor(output, cv2.COLOR_BGR2RGB)
            flipped_image = cv2.flip(image, 1)
            qt_image = QtGui.QImage(flipped_image.data, flipped_image.shape[1], flipped_image.shape[0], QtGui.QImage.Format_RGB888)
            #pic = qt_image.scaled(640, 480, QtCore.Qt.KeepAspectRatio)
            pixmap = QtGui.QPixmap.fromImage(qt_image)
            self.change_pixmap.emit(pixmap)
            #cv2.imshow("Video Streaming", frame)
                
            key = cv2.waitKey(1) & 0xFF

             # quit when 'q' key is pressed
             
            if key == ord("q"):
                break
                # update the FPS counter
            self.fps.update()

        # stop the timer and display FPS information
        self.fps.stop()
        print("[INFO] elasped time: {:.2f}".format(self.fps.elapsed()))
        print("[INFO] approx. FPS: {:.2f}".format(self.fps.fps()))
        
        # do a bit of cleanup
        cv2.destroyAllWindows()
        #self.vs.stop()
        pass
if __name__ == "__main__":
    Face_recognition = faceRecognition()
   # Face_recognition.recognition()

