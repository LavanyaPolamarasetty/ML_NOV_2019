# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import cv2
#print(cv2.__version__)
# 0 fro gray 1 for color 

img = cv2.imread("C:\\Users\\APSSDC\\Desktop\\PHOTO.jpg",2)
cv2.imshow("Mercy",img)
print(img)
cv2.waitKey(1000)
cv2.destroyAllWindows()
