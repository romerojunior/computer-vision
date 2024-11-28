import cv2

# use DirectShow (via videoInput) API on Camera index 0:
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
cap.set(3,640) # width
cap.set(4, 480) # height
cap.set(10, 100) # brightness


if not cap.isOpened():
    print("cannot open camera")
    exit()

while True:
    success, img = cap.read()
    if not success:
        print("cannot receive frame")
        exit()

    cv2.imshow("Video", img)
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()