
import cv2



im = cv2.imread('snsy.png',2)  # 第二个参数是通道数
cv2.imshow("im", im)
cv2.waitKey(0)
cv2.imwrite('hui.png', im)





