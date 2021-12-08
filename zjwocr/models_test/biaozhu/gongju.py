# !/usr/bin/python3
# -*-coding:utf-8-*-
# Author: zhou jun wei
# CreatDate: 2021/12/8 13:05

# 标注工具v.1,仅支持缩放为100% 的电脑，例如 拯救者y7000  缩放比为 125% 本代码，不支持。

from PyQt5.QtWidgets import QApplication, QMessageBox, QLabel, QWidget, QPushButton
import sys, os, random, string
from PyQt5 import QtWidgets, QtGui


class Example(QWidget):

    def __init__(self):
        super().__init__()
        
        self.yzm_xian = "" #  验证码的变量，人工点过，记录的值
        self.get_img__ = ""  # 需要标注文件夹的路径
        self.save_img__ = "" # 保存文件夹的路径
        
        self.yuanshi_img = ''   #  这是临时保存的这张图片的路径
        
        self.yzm_num_shuliang = 0  # 初始标注数据的数量
        self.benci_yum_num_shuliang = 0 # 本次标注的数量
        self.all_yzm_num_shuliang = 0 # 文件夹一共的数量
        self.initUI()  #  入口函数

        
    # 传入图片绝对路径，将图片写入到指定区域，验证码图片
    def show_image(self, imgName):
        jpg = QtGui.QPixmap(imgName).scaled(self.label.width(), self.label.height())
        self.label.setPixmap(jpg)   # 写入图片，将所有图片
        
    def for_img_path(self):
        self.yzm_num_shuliang = len(os.listdir(self.save_img__))
        # 需要标注的数量先不写，没位置了
        self.all_yzm_num_shuliang = len(os.listdir(self.get_img__))
        if self.all_yzm_num_shuliang>1:
            self.yzm_num.setText(
                "需标注：{}     已标注：{}     本次标注：{}   ".format(self.all_yzm_num_shuliang, self.yzm_num_shuliang, self.benci_yum_num_shuliang))
            # 对数量进行更新
            for img in os.listdir(self.get_img__):
                if "png" not in img:
                    pass
                    # print('改一下这里的判断逻辑')
                if "png" not in img: continue
                # C:/Users/50510/Pictures/Saved Pictures/e1e630accbd0637cd626e831cc1e4bd.png
                _img = os.path.join(self.get_img__, img)
                self.yuanshi_img = _img
                self.show_image(_img)
                break
            # 显示1张
        else:
            QMessageBox.about(self, '兄弟', "没图") # 增加提示功能
            self.label.setText("没图了") # 增加提示功能
            
    # 获取图片文件夹路径
    def get_img_path(self):
        m = QtWidgets.QFileDialog.getExistingDirectory(None, "选取文件夹", "C:/")  # 起始路径
        self.get_img__ = m
        self.btn_1.setText(m) # # 写入白色区域
        
        if self.get_img__ and self.save_img__:
            self.for_img_path()
    
    # 写入图片文件夹路径
    def save_img_path(self):
        m = QtWidgets.QFileDialog.getExistingDirectory(None, "选取文件夹", "C:/")  # 起始路径
        self.save_img__ = m
        self.btn_2_2.setText(m) # # 写入白色区域
        if self.get_img__ and self.save_img__:
            self.for_img_path()
    
    def initUI(self):
        self.setGeometry(200, 200, 300, 300)  # 绘制一个窗口
        self.setWindowTitle('周军威标注工具-v.0.1') # title
        
        #########################################################
        # 显示图片区域

        self.yzm_xian = ""
        self.label = QLabel(self)
        self.label.setText(self.yzm_xian)
        self.label.setFixedSize(175, 85) # 设置显示区域大小
        self.label.move(10, 60) # 设置显示区域（坐标）
        self.label.setStyleSheet("QLabel{background:white;}"
                            "QLabel{color:rgb(300,300,300,120);font-size:10px;font-weight:bold;font-family:宋体;}"
                            )
        #################     上面这块是 初始化的时候，给一个白色区域，放入验证码使用的区域
        
        
        # 验证码显示区域
        self.yzm = QLabel(self)
        self.yzm.setText("验证码显示")
        self.yzm.setFixedSize(70, 25) # 设置显示区域大小
        self.yzm.move(220, 90) # 设置显示区域（坐标）
        self.yzm.setStyleSheet("QLabel{background:white;}"
                            "QLabel{color:rgb(300,300,300,120);font-size:10px;font-weight:bold;font-family:宋体;}"
                            )
        #################     上面这块是 初始化的时候，给一个白色区域， 后面用户点击的时候，绘制的白色区域
        
        
        # 显示数量的区域
        self.yzm_num = QLabel(self)
        self.yzm_num.setText("需标注：{}     已标注：{}     本次标注：{}   ".format(self.all_yzm_num_shuliang, self.yzm_num_shuliang, self.benci_yum_num_shuliang))
        self.yzm_num.setFixedSize(280, 25) # 设置显示区域大小
        self.yzm_num.move(10, 150) # 设置显示区域（坐标）
        # self.yzm_num.setStyleSheet("QLabel{background:white;}"
        #                     "QLabel{color:rgb(300,300,300,120);font-size:10px;font-weight:bold;font-family:宋体;}"
        #                     ) # 白框，后面调试代码使用
        #################    上面这块是 初始化的时候，显示 需要标注的数量区域
        

        
        ##############################################################
        # 打开图片
        btn = QPushButton(self)
        btn.setText("打开图片文件夹")
        btn.move(10, 10) # 这个是坐标
        btn.clicked.connect(self.get_img_path) # self.get_img_path 这个是打开一个窗口的
        #################    上面这块是 打开图片文件夹的按钮，加区域
        
        # 打开图片文件夹  设置显示窗口参数
        self.btn_1 = QLabel(self)
        self.btn_1.setFixedSize(180, 20) # 设置显示区域大小
        self.btn_1.move(105, 10) # 设置显示区域（坐标）
        self.btn_1.setStyleSheet("QLabel{background:white;}"
                            "QLabel{color:rgb(300,300,300,120);font-size:10px;font-weight:bold;font-family:宋体;}"
                            )
        
        
        
        #####################################
        btn_2 = QPushButton(self)
        btn_2.setText("保存图片文件夹")
        btn_2.move(10, 35)
        btn_2.clicked.connect(self.save_img_path)
        # 保存图片文件夹  设置显示窗口参数
        self.btn_2_2 = QLabel(self)
        self.btn_2_2.setFixedSize(180, 20) # 设置显示区域大小
        self.btn_2_2.move(105, 36) # 设置显示区域（坐标）
        self.btn_2_2.setStyleSheet("QLabel{background:white;}"
                            "QLabel{color:rgb(300,300,300,120);font-size:10px;font-weight:bold;font-family:宋体;}"
                            )
        #####################################
        
        
        ##############################################################
        
        
        # ####################################################
        # 按钮区
        
        w, h = 30, 30
        start_w = 10
        for labes in range(0, 9):
            bt1 = QPushButton(str(labes),self)
            bt1.setGeometry(start_w,180,w,h)
            # bt1.setText(str(labes))
            bt1.clicked.connect(self.buttonclicked)
            start_w+=31
            
        bt2 = QPushButton("9",self)
        bt2.setGeometry(10,210,w,h)
        bt2.clicked.connect(self.buttonclicked)
        
        
        bt2 = QPushButton("+",self)
        bt2.setGeometry(10+31,210,w,h)
        bt2.clicked.connect(self.buttonclicked)
        
        bt2 = QPushButton("-",self)
        bt2.setGeometry(10+31+31,210,w,h)
        bt2.clicked.connect(self.buttonclicked)
        
        bt2 = QPushButton("＊",self)
        bt2.setGeometry(10+31+31+31,210,w,h)
        bt2.clicked.connect(self.buttonclicked)
        
        bt2 = QPushButton("÷",self)
        bt2.setGeometry(10+31+31+31+31,210,w,h)
        bt2.clicked.connect(self.buttonclicked)
        
        bt2 = QPushButton("=",self)
        bt2.setGeometry(10+31+31+31+31+31,210,w,h)
        bt2.clicked.connect(self.buttonclicked)
        
        bt2 = QPushButton("？",self)
        bt2.setGeometry(196,210,w,h)
        bt2.clicked.connect(self.buttonclicked)
        
        
        queding = QPushButton("清除", self)
        queding.setGeometry(230,230,60,30)
        queding.clicked.connect(self.buttonclicked)
        
        queding = QPushButton("确定",self)
        queding.setGeometry(230,260,60,30)
        queding.clicked.connect(self.buttonclicked)
        
        # ####################################################
        self.show() # 最后一步显示
        
        
    def buttonclicked(self):
        sender = self.sender()
        
        # 清除功能
        if sender.text() == "清除":
            yzm_xian_temp = self.yzm_xian.split(" ")
            yzm_xian_temp.pop() #  删除最后一个元素
            self.yzm_xian = " ".join(yzm_xian_temp)
        
        # 判断点击功能
        if self.yzm_xian and "清除" != sender.text() and "确定" != sender.text():
            self.yzm_xian= self.yzm_xian+' '+sender.text()
        else:
            if "清除" != sender.text() and "确定" != sender.text():
                self.yzm_xian = sender.text()
        
        # 判断确定功能
        if sender.text() == "确定":
            if self.yzm_xian.endswith("＊"):
                QMessageBox.about(self, '兄弟，你弄啥嘞', "兄弟，你弄啥嘞，最后一位是✖？")
                self.yzm_xian = ""
            
            if self.yzm_xian: # 如果字符存在
                # 保存图片
                save_img_tag = self.yzm_xian.replace(" ","")
                start_path = self.yuanshi_img.replace("\\","/")
                i = ''.join(random.choices(string.ascii_lowercase, k=16))
                save_path_ = self.save_img__+"/"+save_img_tag+"_"+str(i)+".png"
                print(1,start_path)
                # print(2,save_path_)
                if start_path and save_path_:
                    with open(start_path, 'rb') as rb:
                        e1e630accbd0637cd626e831cc1e4bd = rb.read()
    
                    with open(save_path_, 'wb') as wb:
                        wb.write(e1e630accbd0637cd626e831cc1e4bd)
                    
                    os.remove(start_path)# 删除标注过的图片
                    self.yzm_xian = "" # 滞空 调用下一张图片
                    self.benci_yum_num_shuliang+=1  # 本次标注数量加1
                    
                ###########################################################################
                
            # 切换下一张图片
            self.for_img_path()
            pass
        
        self.yzm.setText(self.yzm_xian) # 最后写入点击过后的区域
        
# def run():
#     app = QApplication(sys.argv)
#     ex = Example()
#     sys.exit(app.exec_())  # 我也不懂，网上抄的

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())  # 我也不懂，网上抄的