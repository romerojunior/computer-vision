import cv2
import numpy as np

img = cv2.imread("Resources/cards.png")


width, height = 255, 350

pts1 = np.float32([[546,564],[261,385],[990,253],[685,122]])
pts2 = np.float32([[0,0],[width,0],[0,height],[width,height]])

matrix = cv2.getPerspectiveTransform(pts1, pts2)

imgOutput = cv2.warpPerspective(img,matrix,(width,height))

cv2.imshow("Image", img)
cv2.imshow("ImageWarp", imgOutput)

cv2.waitKey(0)