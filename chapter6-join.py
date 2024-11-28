import cv2
import numpy as np

img = cv2.imread("Resources/sample.png")


# vertical stack function, or horizontal (hstack)
# both images must be of same size and have the same amount of channels (similar matrix)
imgHor = np.vstack((img,img))

# different matrix must be normalized first...

cv2.imshow("Horizontal", imgHor)

cv2.waitKey(0)