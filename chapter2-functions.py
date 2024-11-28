import cv2
import numpy as np

img = cv2.imread("Resources/sample.png")

# convert to gray using the convert color function:
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# blur the image using gaussian function:
imgBlur = cv2.GaussianBlur(imgGray, (55,55),0)

# get the edges of the image:
imgCanny = cv2.Canny(img,150,200)

# make edges thicker:
imgDialation = cv2.dilate(
    imgCanny,
    kernel=np.ones((5,5), np.uint8),
    iterations=1
)

# make it thinner again:
imgEroded = cv2.erode(
    imgDialation,
    kernel=np.ones((5,5), np.uint8),
    iterations=1
)

# display images:
cv2.imshow("canny", imgCanny)
cv2.imshow("blur", imgBlur)
cv2.imshow("gray", imgGray)
cv2.imshow("dialation", imgDialation)
cv2.imshow("eroded", imgEroded)

cv2.waitKey(0)
