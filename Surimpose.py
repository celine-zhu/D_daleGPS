import reco_distance
# capture frames from a camera
cap = cv2.VideoCapture(0)
while (cap.isOpened()):
    reco_distance(cap)