# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1117, 683)
        MainWindow.setMinimumSize(QtCore.QSize(1117, 683))
        MainWindow.setMaximumSize(QtCore.QSize(1117, 683))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("picture/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 20, 91, 16))
        self.label.setStyleSheet("color: rgb(255, 255, 255);")
        self.label.setObjectName("label")
        self.wenjianlujingxianshikuang = QtWidgets.QTextBrowser(self.centralwidget)
        self.wenjianlujingxianshikuang.setGeometry(QtCore.QRect(100, 10, 441, 31))
        self.wenjianlujingxianshikuang.setStyleSheet("background-color: rgba(255,255, 255, 100);")
        self.wenjianlujingxianshikuang.setObjectName("wenjianlujingxianshikuang")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 60, 211, 16))
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_2.setObjectName("label_2")
        self.yuyinshibiejieguoxianshikuang = QtWidgets.QTextEdit(self.centralwidget)
        self.yuyinshibiejieguoxianshikuang.setGeometry(QtCore.QRect(20, 90, 521, 191))
        self.yuyinshibiejieguoxianshikuang.setStyleSheet("background-color: rgba(255,255, 255, 100);")
        self.yuyinshibiejieguoxianshikuang.setObjectName("yuyinshibiejieguoxianshikuang")
        self.yuyinshibieanniu = QtWidgets.QPushButton(self.centralwidget)
        self.yuyinshibieanniu.setGeometry(QtCore.QRect(600, 10, 171, 28))
        self.yuyinshibieanniu.setStyleSheet("background-image: url(:/picture/bj.jpg);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));")
        self.yuyinshibieanniu.setObjectName("yuyinshibieanniu")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(600, 190, 171, 28))
        self.pushButton.setStyleSheet("font: 9pt \"??????\";\n"
"background-image: url(:/picture/bj.jpg);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(600, 70, 171, 28))
        self.pushButton_2.setStyleSheet("font: 9pt \"??????\";\n"
"background-image: url(:/picture/bj.jpg);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(600, 130, 171, 28))
        self.pushButton_3.setStyleSheet("font: 9pt \"??????\";\n"
"background-image: url(:/picture/bj.jpg);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));")
        self.pushButton_3.setObjectName("pushButton_3")
        self.yusutiaojietiao = QtWidgets.QSlider(self.centralwidget)
        self.yusutiaojietiao.setGeometry(QtCore.QRect(720, 370, 281, 22))
        self.yusutiaojietiao.setMinimum(1)
        self.yusutiaojietiao.setProperty("value", 50)
        self.yusutiaojietiao.setOrientation(QtCore.Qt.Horizontal)
        self.yusutiaojietiao.setObjectName("yusutiaojietiao")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(590, 320, 121, 16))
        self.label_3.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(640, 370, 72, 15))
        self.label_4.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(640, 430, 72, 15))
        self.label_5.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_5.setObjectName("label_5")
        self.fayanrenlan = QtWidgets.QComboBox(self.centralwidget)
        self.fayanrenlan.setGeometry(QtCore.QRect(720, 430, 281, 22))
        self.fayanrenlan.setMinimumContentsLength(0)
        self.fayanrenlan.setObjectName("fayanrenlan")
        self.fayanrenlan.addItem("")
        self.fayanrenlan.addItem("")
        self.fayanrenlan.addItem("")
        self.fayanrenlan.addItem("")
        self.fayanrenlan.addItem("")
        self.yusuzhi = QtWidgets.QLabel(self.centralwidget)
        self.yusuzhi.setGeometry(QtCore.QRect(1020, 370, 72, 15))
        self.yusuzhi.setStyleSheet("color: rgb(255, 255, 255);")
        self.yusuzhi.setObjectName("yusuzhi")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(640, 530, 81, 16))
        self.label_6.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(640, 590, 81, 16))
        self.label_7.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_7.setObjectName("label_7")
        self.yuzhonglan = QtWidgets.QComboBox(self.centralwidget)
        self.yuzhonglan.setGeometry(QtCore.QRect(720, 530, 281, 22))
        self.yuzhonglan.setObjectName("yuzhonglan")
        self.yuzhonglan.addItem("")
        self.yuzhonglan.addItem("")
        self.nianlingleixinglan = QtWidgets.QComboBox(self.centralwidget)
        self.nianlingleixinglan.setGeometry(QtCore.QRect(720, 590, 281, 22))
        self.nianlingleixinglan.setObjectName("nianlingleixinglan")
        self.nianlingleixinglan.addItem("")
        self.nianlingleixinglan.addItem("")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(590, 490, 141, 16))
        self.label_8.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(20, 320, 121, 16))
        self.label_9.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(40, 370, 72, 15))
        self.label_10.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_10.setObjectName("label_10")
        self.yuanyuzhongxialalan = QtWidgets.QComboBox(self.centralwidget)
        self.yuanyuzhongxialalan.setGeometry(QtCore.QRect(100, 370, 131, 22))
        self.yuanyuzhongxialalan.setObjectName("yuanyuzhongxialalan")
        self.yuanyuzhongxialalan.addItem("")
        self.yuanyuzhongxialalan.addItem("")
        self.yuanyuzhongxialalan.addItem("")
        self.yuanyuzhongxialalan.addItem("")
        self.yuanyuzhongxialalan.addItem("")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(250, 370, 81, 16))
        self.label_11.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_11.setObjectName("label_11")
        self.mubiaoyuzhongxialalan = QtWidgets.QComboBox(self.centralwidget)
        self.mubiaoyuzhongxialalan.setGeometry(QtCore.QRect(320, 370, 111, 22))
        self.mubiaoyuzhongxialalan.setObjectName("mubiaoyuzhongxialalan")
        self.mubiaoyuzhongxialalan.addItem("")
        self.mubiaoyuzhongxialalan.addItem("")
        self.mubiaoyuzhongxialalan.addItem("")
        self.mubiaoyuzhongxialalan.addItem("")
        self.mubiaoyuzhongxialalan.addItem("")
        self.fanyianniu = QtWidgets.QPushButton(self.centralwidget)
        self.fanyianniu.setGeometry(QtCore.QRect(460, 360, 81, 41))
        self.fanyianniu.setObjectName("fanyianniu")
        self.yuanyuzhongshurukuang = QtWidgets.QTextEdit(self.centralwidget)
        self.yuanyuzhongshurukuang.setGeometry(QtCore.QRect(20, 410, 211, 201))
        self.yuanyuzhongshurukuang.setStyleSheet("background-color: rgba(255,255, 255, 100);")
        self.yuanyuzhongshurukuang.setObjectName("yuanyuzhongshurukuang")
        self.mubiaoyuzhongxianshikuang = QtWidgets.QTextBrowser(self.centralwidget)
        self.mubiaoyuzhongxianshikuang.setGeometry(QtCore.QRect(250, 410, 291, 201))
        self.mubiaoyuzhongxianshikuang.setStyleSheet("background-color: rgba(255,255, 255, 100);")
        self.mubiaoyuzhongxianshikuang.setObjectName("mubiaoyuzhongxianshikuang")
        self.tongshengchuanyianniu = QtWidgets.QPushButton(self.centralwidget)
        self.tongshengchuanyianniu.setGeometry(QtCore.QRect(860, 10, 171, 28))
        self.tongshengchuanyianniu.setStyleSheet("font: 9pt \"??????\";\n"
"background-image: url(:/picture/bj.jpg);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));")
        self.tongshengchuanyianniu.setObjectName("tongshengchuanyianniu")
        self.tscyml = QtWidgets.QPushButton(self.centralwidget)
        self.tscyml.setGeometry(QtCore.QRect(840, 70, 211, 31))
        self.tscyml.setStyleSheet("font: 9pt \"??????\";\n"
"background-image: url(:/picture/bj.jpg);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));")
        self.tscyml.setObjectName("tscyml")
        self.yyhcml = QtWidgets.QPushButton(self.centralwidget)
        self.yyhcml.setGeometry(QtCore.QRect(580, 250, 211, 28))
        self.yyhcml.setStyleSheet("font: 9pt \"??????\";\n"
"background-image: url(:/picture/bj.jpg);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));")
        self.yyhcml.setObjectName("yyhcml")
        self.beijing = QtWidgets.QGraphicsView(self.centralwidget)
        self.beijing.setGeometry(QtCore.QRect(-60, -20, 1611, 791))
        self.beijing.setStyleSheet("background-image: url(:/picture/bj2_1261x709.jpg);\n"
"\n"
"")
        self.beijing.setObjectName("beijing")
        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(-10, -10, 1131, 711))
        self.graphicsView.setStyleSheet("background-color: rgba(0, 0, 0,200);")
        self.graphicsView.setObjectName("graphicsView")
        self.tscyyuanyuzhongxialalan = QtWidgets.QComboBox(self.centralwidget)
        self.tscyyuanyuzhongxialalan.setGeometry(QtCore.QRect(920, 180, 131, 22))
        self.tscyyuanyuzhongxialalan.setObjectName("tscyyuanyuzhongxialalan")
        self.tscyyuanyuzhongxialalan.addItem("")
        self.tscyyuanyuzhongxialalan.addItem("")
        self.tscyyuanyuzhongxialalan.addItem("")
        self.tscyyuanyuzhongxialalan.addItem("")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(820, 130, 121, 16))
        self.label_12.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(830, 180, 72, 15))
        self.label_13.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(830, 220, 81, 16))
        self.label_14.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_14.setObjectName("label_14")
        self.tscymubiaoyuzhongxialalan = QtWidgets.QComboBox(self.centralwidget)
        self.tscymubiaoyuzhongxialalan.setGeometry(QtCore.QRect(920, 220, 131, 22))
        self.tscymubiaoyuzhongxialalan.setObjectName("tscymubiaoyuzhongxialalan")
        self.tscymubiaoyuzhongxialalan.addItem("")
        self.tscymubiaoyuzhongxialalan.addItem("")
        self.tscymubiaoyuzhongxialalan.addItem("")
        self.tscymubiaoyuzhongxialalan.addItem("")
        self.label_15 = QtWidgets.QLabel(self.centralwidget)
        self.label_15.setGeometry(QtCore.QRect(830, 260, 72, 15))
        self.label_15.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_15.setObjectName("label_15")
        self.tscyfayanrenlan = QtWidgets.QComboBox(self.centralwidget)
        self.tscyfayanrenlan.setGeometry(QtCore.QRect(920, 260, 131, 22))
        self.tscyfayanrenlan.setMinimumContentsLength(0)
        self.tscyfayanrenlan.setObjectName("tscyfayanrenlan")
        self.tscyfayanrenlan.addItem("")
        self.tscyfayanrenlan.addItem("")
        self.tscyfayanrenlan.addItem("")
        self.tscyfayanrenlan.addItem("")
        self.tscyfayanrenlan.addItem("")
        self.beijing.raise_()
        self.graphicsView.raise_()
        self.label.raise_()
        self.wenjianlujingxianshikuang.raise_()
        self.label_2.raise_()
        self.yuyinshibiejieguoxianshikuang.raise_()
        self.yuyinshibieanniu.raise_()
        self.pushButton.raise_()
        self.pushButton_2.raise_()
        self.pushButton_3.raise_()
        self.yusutiaojietiao.raise_()
        self.label_3.raise_()
        self.label_4.raise_()
        self.label_5.raise_()
        self.fayanrenlan.raise_()
        self.yusuzhi.raise_()
        self.label_6.raise_()
        self.label_7.raise_()
        self.yuzhonglan.raise_()
        self.nianlingleixinglan.raise_()
        self.label_8.raise_()
        self.label_9.raise_()
        self.label_10.raise_()
        self.yuanyuzhongxialalan.raise_()
        self.label_11.raise_()
        self.mubiaoyuzhongxialalan.raise_()
        self.fanyianniu.raise_()
        self.yuanyuzhongshurukuang.raise_()
        self.mubiaoyuzhongxianshikuang.raise_()
        self.tongshengchuanyianniu.raise_()
        self.tscyml.raise_()
        self.yyhcml.raise_()
        self.tscyyuanyuzhongxialalan.raise_()
        self.label_12.raise_()
        self.label_13.raise_()
        self.label_14.raise_()
        self.tscymubiaoyuzhongxialalan.raise_()
        self.label_15.raise_()
        self.tscyfayanrenlan.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.yuyinshibieanniu.clicked.connect(MainWindow.yuyinshibie)
        self.pushButton.clicked.connect(MainWindow.yuyinhecheng)
        self.yusutiaojietiao.actionTriggered['int'].connect(MainWindow.yusuzhishezhi)
        self.pushButton_2.clicked.connect(MainWindow.xingbienianlingfenxi)
        self.pushButton_3.clicked.connect(MainWindow.juzifenxianniu)
        self.fanyianniu.clicked.connect(MainWindow.fanyi)
        self.tongshengchuanyianniu.pressed.connect(MainWindow.tongshengchuanyianxia)
        self.tongshengchuanyianniu.released.connect(MainWindow.tongshengchnuayitaiqi)
        self.tscyml.clicked.connect(MainWindow.dakaitongshengchuanyimulu)
        self.yyhcml.clicked.connect(MainWindow.dakaiyuyinhechengmulu)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "???????????????"))
        self.label_2.setText(_translate("MainWindow", "?????????????????????"))
        self.yuyinshibieanniu.setText(_translate("MainWindow", "????????????????????"))
        self.pushButton.setText(_translate("MainWindow", "????????????????????"))
        self.pushButton_2.setText(_translate("MainWindow", "????????????????????"))
        self.pushButton_3.setText(_translate("MainWindow", "?????????????????????????????"))
        self.label_3.setText(_translate("MainWindow", "?????????????????????"))
        self.label_4.setText(_translate("MainWindow", "?????????"))
        self.label_5.setText(_translate("MainWindow", "????????????"))
        self.fayanrenlan.setItemText(0, _translate("MainWindow", "x3_doudou"))
        self.fayanrenlan.setItemText(1, _translate("MainWindow", "x3_panting"))
        self.fayanrenlan.setItemText(2, _translate("MainWindow", "xiaoyan"))
        self.fayanrenlan.setItemText(3, _translate("MainWindow", "aisjiuxu"))
        self.fayanrenlan.setItemText(4, _translate("MainWindow", "aisxping"))
        self.yusuzhi.setText(_translate("MainWindow", "50"))
        self.label_6.setText(_translate("MainWindow", "???????????????"))
        self.label_7.setText(_translate("MainWindow", "???????????????"))
        self.yuzhonglan.setItemText(0, _translate("MainWindow", "cn_vip"))
        self.yuzhonglan.setItemText(1, _translate("MainWindow", "en_vip"))
        self.nianlingleixinglan.setItemText(0, _translate("MainWindow", "adult"))
        self.nianlingleixinglan.setItemText(1, _translate("MainWindow", "pupil"))
        self.label_8.setText(_translate("MainWindow", "???????????????????????????"))
        self.label_9.setText(_translate("MainWindow", "?????????????????????"))
        self.label_10.setText(_translate("MainWindow", "????????????"))
        self.yuanyuzhongxialalan.setItemText(0, _translate("MainWindow", "???????????????"))
        self.yuanyuzhongxialalan.setItemText(1, _translate("MainWindow", "??????"))
        self.yuanyuzhongxialalan.setItemText(2, _translate("MainWindow", "??????"))
        self.yuanyuzhongxialalan.setItemText(3, _translate("MainWindow", "??????"))
        self.yuanyuzhongxialalan.setItemText(4, _translate("MainWindow", "?????????"))
        self.label_11.setText(_translate("MainWindow", "???????????????"))
        self.mubiaoyuzhongxialalan.setItemText(0, _translate("MainWindow", "??????"))
        self.mubiaoyuzhongxialalan.setItemText(1, _translate("MainWindow", "???????????????"))
        self.mubiaoyuzhongxialalan.setItemText(2, _translate("MainWindow", "??????"))
        self.mubiaoyuzhongxialalan.setItemText(3, _translate("MainWindow", "??????"))
        self.mubiaoyuzhongxialalan.setItemText(4, _translate("MainWindow", "?????????"))
        self.fanyianniu.setText(_translate("MainWindow", "??????"))
        self.tongshengchuanyianniu.setText(_translate("MainWindow", "??????????????????"))
        self.tscyml.setText(_translate("MainWindow", "??????????????????????????????????????"))
        self.yyhcml.setText(_translate("MainWindow", "??????????????????????????????????????"))
        self.tscyyuanyuzhongxialalan.setItemText(0, _translate("MainWindow", "???????????????"))
        self.tscyyuanyuzhongxialalan.setItemText(1, _translate("MainWindow", "??????"))
        self.tscyyuanyuzhongxialalan.setItemText(2, _translate("MainWindow", "??????"))
        self.tscyyuanyuzhongxialalan.setItemText(3, _translate("MainWindow", "?????????"))
        self.label_12.setText(_translate("MainWindow", "?????????????????????"))
        self.label_13.setText(_translate("MainWindow", "????????????"))
        self.label_14.setText(_translate("MainWindow", "???????????????"))
        self.tscymubiaoyuzhongxialalan.setItemText(0, _translate("MainWindow", "??????"))
        self.tscymubiaoyuzhongxialalan.setItemText(1, _translate("MainWindow", "???????????????"))
        self.tscymubiaoyuzhongxialalan.setItemText(2, _translate("MainWindow", "??????"))
        self.tscymubiaoyuzhongxialalan.setItemText(3, _translate("MainWindow", "?????????"))
        self.label_15.setText(_translate("MainWindow", "????????????"))
        self.tscyfayanrenlan.setItemText(0, _translate("MainWindow", "x3_doudou"))
        self.tscyfayanrenlan.setItemText(1, _translate("MainWindow", "x3_panting"))
        self.tscyfayanrenlan.setItemText(2, _translate("MainWindow", "xiaoyan"))
        self.tscyfayanrenlan.setItemText(3, _translate("MainWindow", "aisjiuxu"))
        self.tscyfayanrenlan.setItemText(4, _translate("MainWindow", "aisxping"))
import res
