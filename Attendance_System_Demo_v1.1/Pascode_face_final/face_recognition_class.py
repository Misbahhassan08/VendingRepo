import cv2
import face_recognition
from imutils.video import VideoStream
from imutils.video import FPS
import imutils
import pickle
from PyQt5.QtCore import QThread,pyqtSignal
from PyQt5 import QtCore, QtGui, QtWidgets

class faceRecognition_thread(QtCore.QThread):
    change_pixmap = QtCore.pyqtSignal(QtGui.QPixmap)
    Face_signalFlow = pyqtSignal(str,str,name='m_signal')
    def __init__(self):
        QtCore.QThread.__init__(self)
        #Initialize 'currentname' to trigger only when a new person is identified.
        self.currentname = "unknown"
        #Determine faces from encodings.pickle file model created from train_model.py
        self.encodingsP = "encodings.pickle"

        # load the known faces and embeddings along with OpenCV's Haar
        # cascade for face detection
        print("[INFO] loading encodings + face detector...")
        self.data = pickle.loads(open(self.encodingsP, "rb").read())

        # initialize the video stream and allow the camera sensor to warm up
        # Set the ser to the followng
        # src = 0 : for the build in single web cam, could be your laptop webcam
        # src = 2 : I had to set it to 2 inorder to use the USB webcam attached to my laptop
    
        #vs = VideoStream(usePiCamera=True).start()
        #time.sleep(2.0)

        # start the FPS counter
        self.fps = FPS().start()
        #self.start()

        # loop over frames from the video file stream
    
    def run(self):
        vs = cv2.VideoCapture(0)
        self.thread_is_active = True
        while self.thread_is_active:
            # grab the frame from the threaded video stream and resize it
            # to 500px (to speedup processing)
            ret,frame = vs.read()
            frame = imutils.resize(frame, width=500)
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

                    # determine the recognized face with the largest number
                    # of votes (note: in the event of an unlikely tie Python
                    # will select first entry in the dictionary)
                    name = max(counts, key=counts.get)

                    #If someone in your dataset is identified, print their name on the screen
                    if self.currentname:
                        self.currentname = name
                        #print(self.currentname)
                        self.sname = self.currentname
                        self.Face_signalFlow.emit(self.sname,'Face_Recognition')
                        self.sname = ""

                # update the list of names
                names.append(name)

            # loop over the recognized faces
            for ((top, right, bottom, left), name) in zip(boxes, names):
                # draw the predicted face name on the image - color is in BGR
                cv2.rectangle(frame, (left, top), (right, bottom),
                    (0, 255, 225), 2)
                y = top - 15 if top - 15 > 15 else top + 15
                cv2.putText(frame, name, (left, y), cv2.FONT_HERSHEY_SIMPLEX,
                    .8, (0, 255, 255), 2)

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
            
            #cv2.imshow("Facial Recognition is Running", frame)
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
        #vs.stop()
    def stop(self):
        self.thread_is_active = False
        self.quit()
        
if __name__ == "__main__":
   face_object = faceRecognition_thread()
   face_object.start()