import cv2 #OpenCV is a huge python library which can be used to capture images manuplate images and perform
           #other image proccesing works
def take_snapshot():
    capture = cv2.VideoCapture(0)
    result = True
    while(result):
        #it will read frames while camera is on
        #r is dummy variable which returns a bolean value , basically to tell us if something is beign returned or not
        #frame has the frame of the video
        r,frame = capture.read()
        #cv2.imwrite() is used to save an image to any storage device
        cv2.imwrite("newPicture.jpg",frame)
        result = False
    
    capture.release()#it releases the camera
    cv2.destroyAllWindows()

take_snapshot()