# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(865, 662)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(40, 350, 771, 271))
        self.textEdit.setObjectName("textEdit")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(40, 330, 54, 12))
        self.label_4.setObjectName("label_4")
        self.ori_img = QtWidgets.QLabel(self.centralwidget)
        self.ori_img.setGeometry(QtCore.QRect(450, 50, 361, 81))
        self.ori_img.setFrameShape(QtWidgets.QFrame.Box)
        self.ori_img.setText("")
        self.ori_img.setObjectName("ori_img")
        self.new_img = QtWidgets.QLabel(self.centralwidget)
        self.new_img.setGeometry(QtCore.QRect(450, 160, 361, 81))
        self.new_img.setFrameShape(QtWidgets.QFrame.Box)
        self.new_img.setText("")
        self.new_img.setObjectName("new_img")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(450, 30, 54, 12))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(450, 140, 54, 12))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(450, 270, 71, 20))
        self.label_7.setObjectName("label_7")
        self.z1 = QtWidgets.QLabel(self.centralwidget)
        self.z1.setGeometry(QtCore.QRect(450, 301, 41, 20))
        self.z1.setObjectName("z1")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(640, 270, 71, 20))
        self.label_9.setObjectName("label_9")
        self.z2 = QtWidgets.QLabel(self.centralwidget)
        self.z2.setGeometry(QtCore.QRect(640, 301, 41, 20))
        self.z2.setObjectName("z2")
        self.formLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.formLayoutWidget.setGeometry(QtCore.QRect(140, 270, 161, 54))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.load = QtWidgets.QPushButton(self.formLayoutWidget)
        self.load.setObjectName("load")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.load)
        self.generate = QtWidgets.QPushButton(self.formLayoutWidget)
        self.generate.setObjectName("generate")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.generate)
        self.recog = QtWidgets.QPushButton(self.formLayoutWidget)
        self.recog.setObjectName("recog")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.recog)
        self.clearlog = QtWidgets.QPushButton(self.formLayoutWidget)
        self.clearlog.setObjectName("clearlog")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.clearlog)
        self.origin = QtWidgets.QLabel(self.centralwidget)
        self.origin.setGeometry(QtCore.QRect(40, 30, 361, 221))
        self.origin.setFrameShape(QtWidgets.QFrame.Box)
        self.origin.setText("")
        self.origin.setObjectName("origin")
        self.ori_result = QtWidgets.QLabel(self.centralwidget)
        self.ori_result.setGeometry(QtCore.QRect(520, 270, 91, 20))
        self.ori_result.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.ori_result.setText("")
        self.ori_result.setObjectName("ori_result")
        self.z1_c = QtWidgets.QLabel(self.centralwidget)
        self.z1_c.setGeometry(QtCore.QRect(520, 301, 91, 20))
        self.z1_c.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.z1_c.setText("")
        self.z1_c.setObjectName("z1_c")
        self.new_result = QtWidgets.QLabel(self.centralwidget)
        self.new_result.setGeometry(QtCore.QRect(720, 270, 91, 20))
        self.new_result.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.new_result.setText("")
        self.new_result.setObjectName("new_result")
        self.z2_c = QtWidgets.QLabel(self.centralwidget)
        self.z2_c.setGeometry(QtCore.QRect(720, 301, 91, 20))
        self.z2_c.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.z2_c.setText("")
        self.z2_c.setObjectName("z2_c")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_4.setText(_translate("MainWindow", "Debug Log"))
        self.label_5.setText(_translate("MainWindow", "原始图像"))
        self.label_6.setText(_translate("MainWindow", "扰动图像"))
        self.label_7.setText(_translate("MainWindow", "原始结果"))
        self.z1.setText(_translate("MainWindow", "置信度"))
        self.label_9.setText(_translate("MainWindow", "扰动结果"))
        self.z2.setText(_translate("MainWindow", "置信度"))
        self.load.setText(_translate("MainWindow", "加载图像"))
        self.generate.setText(_translate("MainWindow", "生成扰动"))
        self.recog.setText(_translate("MainWindow", "识别图像"))
        self.clearlog.setText(_translate("MainWindow", "清空日志"))