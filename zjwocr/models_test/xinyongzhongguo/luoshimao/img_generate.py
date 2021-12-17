import os, random, math, cv2
import numpy as np


def get_toumingdu(x, y, img, _name_=None):
    # 画上一个透明的圆
    overlay = img.copy()
    original = img.copy()
    cv2.circle(overlay, (x, y), 13, (255, 255, 255), -1)
    cv2.circle(original, (x, y), 13, (255, 255, 255), -1)
    alpha = 0.3
    img = cv2.addWeighted(overlay, alpha, img, 1 - alpha, 0)  # 透明度调整

    x1, y1, x2, y2 = x - 13, y - 13, x + 13, y + 13
    # img = cv2.rectangle(img, (x1, y1), (x2, y2), (0, 0, 255), 1)  # 这是红框

    # AddText = img.copy() # 文字
    # img  =cv2.putText(AddText, _name_, (x1, y1), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 0), 1)

    return x1, y1, x2, y2, img


def sanjiaoxing(x, y, img):  # 三角形  输入 x-25 y-25
    # 画一个三角形
    shan_ge_dian_list = [(x + 9, y + 0), (x + 2, y + 11), (x + 15, y + 11)]  # 三个点的坐标
    img = cv2.fillPoly(img, [np.array(shan_ge_dian_list)], [200, 200, 200])  # 根据3个点的位置，填充

    x, y = x + 9, y + 5
    x1, y1, x2, y2, img = get_toumingdu(x, y, img,"a")
    return x1, y1, x2, y2, img


def yuan(x, y, img):
    # 画一个原点
    img = cv2.circle(img, (x, y), 6, [200, 200, 200], -1)
    x1, y1, x2, y2, img = get_toumingdu(x, y, img,"b")
    return x1, y1, x2, y2, img


def fangkuai(x, y, img):
    # 画一个方块
    img = cv2.rectangle(img, (x, y), (x + 9, y + 9), (200, 200, 200), -1)

    x, y = x + 4, y + 4
    x1, y1, x2, y2, img = get_toumingdu(x, y, img,"c")
    return x1, y1, x2, y2, img


def wujiaoxing(x, y, img):
    # 画一个五角星
    points = []
    start_angle = 15
    x_ = 8
    y_ = x_ / (math.cos(0.4 * math.pi) + math.sin(0.2 * math.pi) / math.tan(0.1 * math.pi))

    def get_point(angle, d, base):
        angle = angle / 180.0 * math.pi
        _x, _y = math.cos(angle) * d, math.sin(angle) * d
        return [base[0] + _x, base[1] - _y]

    for i in range(5):
        _x, _y = math.cos(start_angle), math.sin(start_angle)
        points.append(get_point(start_angle, x_, (x, y)))

        start_angle -= 36
        points.append(get_point(start_angle, y_, (x, y)))
        start_angle -= 36

    points = np.array([points], np.int32)
    img = cv2.fillPoly(img, points, (200, 200, 200), cv2.LINE_AA)  # 五角星绘制结束

    x1, y1, x2, y2, img = get_toumingdu(x, y, img, "d")
    return x1, y1, x2, y2, img

def save_img(name_):
    # img = np.zeros((160, 300, 3), np.uint8) # numpy 生成一张图片
    img = cv2.imread(name_)
    def_list  = [yuan, fangkuai, sanjiaoxing, wujiaoxing]
    def_list.remove(random.choice(def_list))  # 随机干掉1个
    zuobiao_str = ''
    name_str = ''
    for i in def_list:
        x, y = random.randint(25, 275), random.randint(25, 135)
        # x, y = x_y()
        name__ = i.__name__
        x1, y1, x2, y2, img = i(x, y, img)
        zuobiao_str+=str(x1)+','+str(y1)+','+str(x2)+','+str(y2)+"_"
        name_str += name__+'~'
    
    # img_name = r"D:/img/luoshimao/train/"+zuobiao_str+name_str[:-1]+".png"
    # print(img_name)
    # cv2.imwrite(img_name,img)
    cv2.imshow('test', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

save_img("1-1.jpg")