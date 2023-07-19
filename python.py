import cv2 #pip install opencv-python
import numpy as np
butterfly = cv2.imread("butterfly.jpg")
grey = cv2.cvtColor(butterfly,cv2.COLOR_BGR2GRAY)
# cv2.imshow("blue butterfly", grey)
# cv2.waitKey(0)
# print(grey)

black=np.zeros([600,600])
row = black[1:2]
column = black[:,1:2 ]
# row: 3 and 4 , column: 3 and 4
black[200:400, 200:400] = 255
# cv2.imshow("black and white", black)
# cv2.waitKey(0)
# print(black)

poster= cv2.imread("poster.jpg")
cv2.imshow("rocket",poster)
cv2.putText(poster,"hello",(20,200), fontFace=cv2.FONT_HERSHEY_COMPLEX,fontScale=1,color=(255,0,0))
cv2.waitKey(0)
