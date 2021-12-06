import cv2


def face_datection_temp(frame):
    face_detect = cv2.CascadeClassifier(
        r"D:/python3/Anaconda/envs/model_test/Lib/site-packages/cv2/data/haarcascade_frontalface_alt2.xml")
    face = face_detect.detectMultiScale(frame)  # 参数重要，后期可以调
    for x, y, w, h in face:
        print(x, y, w, h)
        cv2.rectangle(frame, (x, y), (x + w, y + h), color=(0, 0, 255), thickness=1)
    cv2.imshow('test.png', frame)

# cap = cv2.VideoCapture(0) # 参数 0 默认调取本机摄像头
cap = cv2.VideoCapture("test.mp4") # 参数 0 默认调取本机摄像头



while 1:
    flag, frame = cap.read()
    if not flag:
        break
    face_datection_temp(frame)
    if ord('q') == cv2.waitKey(0):
        break


# cv2.waitKey(0)
cv2.destroyAllWindows()
cap.release() # 关闭摄像头