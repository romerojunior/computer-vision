import cv2
import numpy as np

img = np.zeros((512, 512, 3), np.uint8)

# height, width
# img[200:300,100:300] = 0,255,0

cv2.line(img, (0,0), (img.shape[1],img.shape[0]),(0,255,0),3)

cv2.rectangle(img, (0,0), (250,350), (255,0,0), cv2.FILLED)

cv2.circle(img, (400,50), 30, (255,255,0),5)

cv2.putText(img, "HELLO WORLD", (300,100), cv2.FONT_HERSHEY_PLAIN, 1.3, (255,255,0),1)

cv2.imshow("image", img)

cv2.waitKey(0)