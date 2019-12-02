import sys
import os
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import LPR_fgsm as fgsm
class picture(QWidget):
    def __init__(self):
        super(picture, self).__init__()
        self.imgPath = ''
        self.trans = False
        self.resize(800, 650)
        self.setWindowTitle("车牌识别Demo")

        btn = QPushButton(self)
        btn.setText("加载图片")
        btn.move(50,50)
        btn.clicked.connect(self.openimage)

        btn2 = QPushButton(self)
        btn2.setText("生成扰动")
        btn2.move(150,50)
        btn2.clicked.connect(self.fgsm)

        
        self.ori_img = QLabel(self)
        self.ori_img.setFixedSize(164, 48)
        self.ori_img.move(240, 30)
        self.ori_img.setStyleSheet("QLabel{background:white;}"
                                 "QLabel{color:rgb(300,300,300,120);font-size:10px;font-weight:bold;font-family:宋体;}"
                                 )  
        
        self.adv_img = QLabel(self)
        self.adv_img.setFixedSize(164, 48)
        self.adv_img.move(450, 30)
        self.adv_img.setStyleSheet("QLabel{background:white;}"
                                 "QLabel{color:rgb(300,300,300,120);font-size:10px;font-weight:bold;font-family:宋体;}"
                                 )  

        self.label1 = QLabel(self)
        self.label1.move(650,30)
        self.label1.setText("result：waiting")
        self.label2 = QLabel(self)
        self.label2.move(650,45)
        self.label2.setText("confidence：waiting")
        self.cb1 = QCheckBox('迁移已生成模型',self)
        self.cb1.move(650,60)
        self.cb1.stateChanged.connect(self.changecb1)


        self.label = QLabel(self)
        self.label.setFixedSize(700, 500)
        self.label.move(50, 100)
        self.label.setStyleSheet("QLabel{background:white;}"
                                 "QLabel{color:rgb(300,300,300,120);font-size:10px;font-weight:bold;font-family:宋体;}"
                                 )        

    def changecb1(self):
        if self.cb1.checkState() == Qt.Checked:
            if os.path.exists('no_noise.npy'):
                if os.path.exists('noise.npy') == False:
                    os.rename('no_noise.npy','noise.npy')
        elif self.cb1.checkState() == Qt.Unchecked:
            if os.path.exists('noise.npy'):
                if os.path.exists('no_noise.npy'):
                    os.remove('no_noise.npy')
                os.rename('noise.npy','no_noise.npy')
            

    def openimage(self):
        imgName, imgType = QFileDialog.getOpenFileName(self, "打开图片", "", "*.jpg;;*.png;;All Files(*)")
        jpg = QtGui.QPixmap(imgName).scaled(self.label.width(), self.label.height())
        self.label.setPixmap(jpg)
        if(len(imgName)>3):
            print(imgName)
            res = fgsm.perdict(imgName)
            self.label1.setText(u"result:"+str(res['class']))
            self.label2.setText(u"confidence:"+str(res['confidence']))
            self.imgPath = imgName
            img = QtGui.QPixmap('./images_out/b_img.jpg').scaled(self.ori_img.width(), self.ori_img.height())
            self.ori_img.setPixmap(img)
            self.adv_img.clear()

    def fgsm(self):
        if len(self.imgPath)>3:
            self.label1.setText(u"result:waiting")
            self.label2.setText(u"confidence:waiting")
            res = fgsm.attack(self.imgPath)
            self.label1.setText(u"result:"+str(res[0]))
            self.label2.setText(u"confidence:"+str(res[1]))
            img = QtGui.QPixmap('./images_out/adv_img.jpg').scaled(self.adv_img.width(), self.adv_img.height())
            self.adv_img.setPixmap(img)



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    my = picture()
    my.show()
    sys.exit(app.exec_())
