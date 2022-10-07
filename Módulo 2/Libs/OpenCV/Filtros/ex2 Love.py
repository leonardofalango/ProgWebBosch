# -*- coding: utf-8 -*-
"""
Created on Thu Feb 17 11:04:52 2022

@author: Leonardo Falango
"""

import cv2
import numpy as np

img = cv2.imread('../dados/ruido.jpg')
kernel = np.ones((3,3), np.uint8)
erosao = cv2.erode(img, kernel)

cv2.imshow("Erodado", erosao)
cv2.imshow("Original", img)

cv2.waitKey(0) & 0xFF
cv2.destroyAllWindows()