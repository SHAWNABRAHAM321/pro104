import cv2
poster= cv2.imread("poster.jpg")
cv2.imshow("rocket",poster)
cv2.putText(poster,"hello",(20,200), fontFace=cv2.FONT_HERSHEY_COMPLEX,fontScale=1,color=(255,0,0))
cv2.waitKey(0)







