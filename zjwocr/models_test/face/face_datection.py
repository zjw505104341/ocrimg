import cv2

im = cv2.imread('multi_face/duoren2.jpg')
h, w, l = im.shape
print(h, w)
h, w = int(h / 1), int(w / 1)
print(h, w)
im = cv2.resize(im, (w, h))
cv2.imshow('111.jpg', im)
def face_detect_demo(im):
    face_detect = cv2.CascadeClassifier(r"D:/python3/Anaconda/envs/model_test/Lib/site-packages/cv2/data/haarcascade_frontalface_alt2.xml")
    face = face_detect.detectMultiScale(im)  # 参数重要，后期可以调
    for x, y, w, h in face:
        print(x, y, w, h)
        cv2.rectangle(im, (x, y), (x + w, y + h), color=(0, 0, 255), thickness=1)
    cv2.imshow('test.png', im)


face_detect_demo(im)
cv2.waitKey(0)
cv2.destroyAllWindows()
