import cv2
import os

id_Folder = '126107'
dataset_Folder = id_Folder
model_Folder = 'Model'
id_Folder_directory = f"/home/pi/Desktop/TechnoVerse/Attendance_System_Demo_v1.2/pascode_face_final/"
os.mkdir(id_Folder_directory + id_Folder)
dataset_Folder_directory = f"/home/pi/Desktop/TechnoVerse/Attendance_System_Demo_v1.2/pascode_face_final/{id_Folder}/"
os.mkdir(dataset_Folder_directory + dataset_Folder)
model_Folder_directory = f"/home/pi/Desktop/TechnoVerse/Attendance_System_Demo_v1.2/pascode_face_final/{id_Folder}/"
os.mkdir(model_Folder_directory + model_Folder)

cam = cv2.VideoCapture(0)
cv2.namedWindow("press space to take a photo", cv2.WINDOW_NORMAL)
cv2.resizeWindow("press space to take a photo", 500, 300)

img_counter = 0

while True:
    ret, frame = cam.read()
    if not ret:
        print("failed to grab frame")
        break
    cv2.imshow("press space to take a photo", frame)

    k = cv2.waitKey(1)
    if k%256 == 27:
        # ESC pressed
        print("Escape hit, closing...")
        break
    elif k%256 == 32:
        # SPACE pressed
        
        img_name = f"{id_Folder}/{dataset_Folder}/image_{img_counter}.jpg"
        cv2.imwrite(img_name, frame)
        print(f"{img_name} written!")
        img_counter += 1

cam.release()

cv2.destroyAllWindows()
