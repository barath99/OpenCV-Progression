import cv2
img=cv2.imread('img.jpg',cv2.IMREAD_COLOR)
img=cv2.imread('1.jpg',0)
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
