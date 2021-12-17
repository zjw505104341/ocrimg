from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QLabel, QPushButton, QDialog, QApplication, QWidget
import sys, os, random, string, cv2


class Ui_Dialog(QWidget):
    get_img_path = ""
    save_img_path = ""
    
    # 传入图片绝对路径，将图片写入到指定区域，验证码图片
    def show_image(self, imgName):
        # TODO 这里建议使用图片原始大小
        jpg = QtGui.QPixmap(imgName).scaled(300, 160)
        self.yzm_img_area.setPixmap(jpg)  # 写入图片，将所有图片
    
    def for_img_path(self):
        print(1111, os.listdir(self.get_img_path))
        for img in os.listdir(self.get_img_path):
            if "png" not in img:
                pass
                # print('改一下这里的判断逻辑')
            if "png" not in img: continue
            # C:/Users/50510/Pictures/Saved Pictures/e1e630accbd0637cd626e831cc1e4bd.png
            _img = os.path.join(self.get_img_path, img)
            self.yuanshi_img = _img
            self.show_image(_img)
            break
    
    # 获取图片文件夹路径
    def click_get_img_path(self):
        m = QtWidgets.QFileDialog.getExistingDirectory(None, "选取文件夹", "C:/")  # 起始路径
        self.get_img_path = m
        self.click_img_path_label_1.setText(m)
        if self.get_img_path and self.save_img_path:
            self.for_img_path()
    
    # 保存图片文件夹路径
    def click_save_img_path(self):
        m = QtWidgets.QFileDialog.getExistingDirectory(None, "选取文件夹", "C:/")  # 起始路径
        self.save_img_path = m
        self.click_img_path_label_2.setText(m)
        
        if self.get_img_path and self.save_img_path:
            self.for_img_path()
    
    # 打开文件夹的方法
    def open_path_ui_def(self, Dialog):
        btn_1 = QPushButton(Dialog)
        btn_1.setText("图片文件夹")
        btn_1.move(30, 20)  # 这个是坐标
        btn_1.clicked.connect(self.click_get_img_path)  # self.click_get_img_path 这个是打开一个窗口的
        
        # 下面是区域
        self.click_img_path_label_1 = QtWidgets.QLabel(Dialog)
        self.click_img_path_label_1.setGeometry(QtCore.QRect(130, 25, 255, 16))
        self.click_img_path_label_1.setText("")
        self.click_img_path_label_1.setObjectName("点击过文件夹显示的区域")
        
        btn_2 = QPushButton(Dialog)
        btn_2.setText("标注文件夹")
        btn_2.move(30, 50)  # 这个是坐标
        btn_2.clicked.connect(self.click_save_img_path)  # self.click_save_img_path 这个是打开一个窗口的
        
        # 下面是区域
        self.click_img_path_label_2 = QtWidgets.QLabel(Dialog)
        self.click_img_path_label_2.setGeometry(QtCore.QRect(130, 55, 255, 16))
        self.click_img_path_label_2.setText("")
        self.click_img_path_label_2.setObjectName("点击过文件夹显示的区域")
    
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1500, 800)
        
        self.open_path_ui_def(Dialog)  # 打开两个文件夹
        
        self.yzm_img_area = QtWidgets.QLabel(Dialog)
        self.yzm_img_area.setGeometry(QtCore.QRect(30, 85, 410, 410))
        self.yzm_img_area.setText("验证码显示区域")
        self.yzm_img_area.setObjectName("图片区域")
        self.yzm_img_area.setStyleSheet("QLabel{background:white;}"
                                        "QLabel{color:rgb(255,0,0);font-size:20px;font-weight:bold;font-family:宋体;}"
                                        )
        
        
        
        
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(1000, 500 + 70, 255, 16))
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(1000, 500 + 110, 255, 16))
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.retranslateUi(Dialog)
        
        QtCore.QMetaObject.connectSlotsByName(Dialog)
    
    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))


class MyForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.show()

    def mousePressEvent(self,event):
        if event.buttons() & QtCore.Qt.LeftButton:
            x = event.x()
            y = event.y()
            text = "x: {0},y: {1}".format(x, y)
            self.ui.label_2.setText('鼠标按下：' + text)
    
    def mouseReleaseEvent(self, event):
        x = event.x()
        y = event.y()
        text = "x: {0},y: {1}".format(x, y)
        self.ui.label_3.setText("鼠标释放：" + text)
        self.update()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MyForm()
    sys.exit(app.exec_())
