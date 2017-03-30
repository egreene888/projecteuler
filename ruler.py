import numpy
import cv2

ruler = numpy.zeros((1600, 2560), dtype = 'uint8')

for i in range(5):
	ruler[:, 227 * i] = 255

cv2.imshow('ruler', ruler)
cv2.waitKey()