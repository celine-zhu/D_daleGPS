""""import reco_distance
# capture frames from a camera
cap = cv2.VideoCapture(0)
while (cap.isOpened()):
    reco_distance(cap)"""
import cv2
from imutils import paths
import imutils
def main():
    windowname="Live Video Feed"
    cv2.namedWindow(windowname)
    cap=cv2.VideoCapture(0)
    if cap.isOpened():
        ret, frame=cap.read()
    else:
        ret=False
    while ret:
        ret, frame=cap.read()
        gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        gray = cv2.GaussianBlur(gray, (5, 5), 0)
        edged=cv2.Canny(gray,50,150)
        """cnts=cv2.findContours(edged.copy(),cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)
        cnts=cv2.imutils.grab_contours(cnts)"""
        cv2.imshow(windowname,frame)
        cv2.imshow("edged",edged)
        if cv2.waitKey(1)== 27:
            break
    cv2.destroyAllWindow()
    cap.release()
    
if __name__ == "__main__":
    main()