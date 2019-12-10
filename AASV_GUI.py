import sys
import os
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from mainWindow import *
import LPR_fgsm as fgsm

class EmittingStream(QtCore.QObject):  
        textWritten = QtCore.pyqtSignal(str)
        def write(self, text):
            self.textWritten.emit(str(text))  


class MyWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyWindow, self).__init__(parent)
        self.setupUi(self)
        sys.stdout = EmittingStream(textWritten=self.outputWritten)  
        sys.stderr = EmittingStream(textWritten=self.outputWritten)

        self.load.clicked.connect(self.loadImage)
        self.recog.clicked.connect(self.predict)
        self.generate.clicked.connect(self.attack)
        self.clearlog.clicked.connect(self.clearup)

        self.imgPath = ''
        self.flag = 1
        self.adv_result = ''
        self.adv_confidence = ''

    def outputWritten(self, text):  
        cursor = self.textEdit.textCursor()  
        cursor.movePosition(QtGui.QTextCursor.End)  
        cursor.insertText(text)  
        self.textEdit.setTextCursor(cursor)  
        self.textEdit.ensureCursorVisible() 

    def loadImage(self):
        imgName, imgType = QFileDialog.getOpenFileName(self, "打开图片", "", "*.jpg;;*.png;;All Files(*)")
        jpg = QtGui.QPixmap(imgName).scaled(self.origin.width(), self.origin.height())
        self.origin.setPixmap(jpg)
        self.flush()
        self.new_img.clear()
        self.ori_img.clear()
        self.imgPath = imgName
        
    def predict(self):
        if(len(self.imgPath)>3):
            if self.flag == 1:
                print(self.imgPath)
                res = fgsm.predict(self.imgPath)
                self.ori_result.setText(str(res['class']))
                self.z1_c.setText(str(res['confidence']))
                img = QtGui.QPixmap('./images_out/b_img.jpg').scaled(self.ori_img.width(), self.ori_img.height())
                self.ori_img.setPixmap(img)
            else:
                self.new_result.setText(self.adv_result)
                self.z2_c.setText(self.adv_confidence)


    def attack(self):
        res = fgsm.attack(self.imgPath)
        img = QtGui.QPixmap('./images_out/adv_img.jpg').scaled(self.new_img.width(), self.new_img.height())
        self.new_img.setPixmap(img)
        self.flag = 2
        self.adv_result = str(res[0])
        self.adv_confidence = str(res[1])


    def flush(self):
        self.textEdit.clear()
        self.imgPath = ''
        self.flag = 1
        self.adv_result = []
        self.adv_confidence = []

    def clearup(self):
        self.textEdit.clear()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWin = MyWindow()
    myWin.show()
    sys.exit(app.exec_())