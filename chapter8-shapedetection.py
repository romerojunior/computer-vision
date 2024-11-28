import cv2
import numpy as np

path = "Resources/shapes.png"
img = cv2.imread(path)
imgContour = img.copy()

def getContours(i):
    contours, hierarchy = cv2.findContours(i, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area > 500:
            cv2.drawContours(imgContour, cnt, -1, (255,0,0))
            peri = cv2.arcLength(cnt,True)
            # counts the amount of corners of a closed geometrical shape:
            approx = cv2.approxPolyDP(cnt,0.02*peri,True)
            objCorners = len(approx)

            # draws a bounding rectangle around the shape:
            x, y, w, h = cv2.boundingRect(approx)
            cv2.rectangle(imgContour,(x,y),(x+w,y+h),(0,0,255),2)
            # the above can be used to identify things like the "center point" of an object, and so on.

            # detect shapes:

            if objCorners == 3:
                objectType = "TRIANGLE"
            elif objCorners == 4:
                aspRatio = float(w)/float(h)
                if 0.90 < aspRatio < 1.05:
                    objectType = "SQUARE"
                else:
                    objectType = "RECTANGLE"
            elif objCorners == 6:
                objectType = "HEXAGON"
            elif objCorners > 7:
                objectType = "CIRCLE"
            else:
                objectType = "NONE"

            cv2.putText(
                imgContour,
                objectType,
                (x + (w // 2) - 10, y + (h // 2) - 10),
                cv2.FONT_HERSHEY_PLAIN,
                1,
                (0, 0, 0),
                2
            )

imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray,(7,7), 1)
imgCanny = cv2.Canny(imgBlur,50,50)
imgBlank = np.zeros_like(img)

getContours(imgCanny)

# cv2.imshow("original", img)
# cv2.imshow("gray", imgGray)
# cv2.imshow("blur", imgBlur)
# cv2.imshow("canny", imgCanny)
# cv2.imshow("blank", imgBlank)
cv2.imshow("contour", imgContour)



cv2.waitKey(0)