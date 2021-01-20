import cv2
def take_snapshot():
    capture = cv2.VideoCapture(0)
    result = True
    while(result):
        r,frame = capture.read()
        cv2.imwrite("newPicture.jpg",frame)
        result = False
    
    capture.release()
    cv2.destroyAllWindows()

take_snapshot()
