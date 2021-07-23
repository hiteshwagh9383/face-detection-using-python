import cv2
#import the cascade for face detection
FaceClassifier =cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
# access the webcam (every webcam has
capture = cv2.VideoCapture(0)

while(True):
    # Capture frame-by-frame
    ret, frame = capture.read()
    if not capture:
        print ("Error opening webcam device")
        sys.exit(1)
    # to detect faces in video
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = FaceClassifier.detectMultiScale(gray, 1.3, 5)

    # Resize Image
    minisize = (frame.shape[1],frame.shape[0])
    miniframe = cv2.resize(frame, minisize)
    # Store detected frames in variable name faces
    faces =  FaceClassifier.detectMultiScale(miniframe)
   # Draw rectangle
    for f in faces:
        x, y, w, h = [ v for v in f ]
        cv2.rectangle(frame, (x,y), (x+w,y+h), (255,255,255))
        #Save just the rectangle faces in SubRecFaces
        sub_face = frame[y:y+h, x:x+w]
        FaceFileName = "faces/face_" + str(y) + ".jpg"
        cv2.imwrite(FaceFileName, sub_face)
        #Display the image
        cv2.imshow('Result',frame)
        cv2.waitKey(180)
        break

    # When everything done, release the capture

img.release()
cv2.destroyAllWindows()
