
import cv2
from LaplaceFilter import *
import numpy as np

# [3,2,1] [11,00000010,00000001] -> 110000001000000001 -> 197121
def rgbtoint32(rgb):
    color = 0
    for c in rgb[::-1]:
        color = (color<<8) + c
    return color

def int32torgb(color):
    rgb = []
    for i in range(3):
        rgb.append(color&255)
        color = color >> 8
    return rgb


img = cv2.imread("img1.jpeg")

(rows , cols )=(len(img),len(img[0]))

# rows = 3
# cols = 4
pixelMatrix = np.arange(rows * cols).reshape(rows, cols)

for i in range(rows):
    for j in range(cols):
        pixelMatrix[i][j] = rgbtoint32(img[i][j])


# Applying Laplacian Filter
m = myMatrix(pixelMatrix)
pixelMatrixFiltered = m.Filter()

gen = np.array(pixelMatrixFiltered ,dtype=np.uint8)
cv2.imshow('output',gen)
cv2.waitKey(0)
cv2.destroyWindow('i')




