# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'repeat_run.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1540, 578)
        self.tableWidget = QtWidgets.QTableWidget(Dialog)
        self.tableWidget.setGeometry(QtCore.QRect(220, 30, 301, 301))
        self.tableWidget.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.tableWidget.setMidLineWidth(0)
        self.tableWidget.setAlternatingRowColors(True)
        self.tableWidget.setGridStyle(QtCore.Qt.SolidLine)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(1)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        item.setForeground(brush)
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setSortIndicatorShown(False)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(570, 20, 71, 41))
        self.label.setObjectName("label")
        self.Repetitions = QtWidgets.QLineEdit(Dialog)
        self.Repetitions.setGeometry(QtCore.QRect(672, 30, 101, 21))
        self.Repetitions.setObjectName("Repetitions")
        self.determine = QtWidgets.QPushButton(Dialog)
        self.determine.setGeometry(QtCore.QRect(810, 30, 51, 21))
        self.determine.setObjectName("determine")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(580, 90, 72, 15))
        self.label_2.setObjectName("label_2")
        self.NumOfDate = QtWidgets.QLineEdit(Dialog)
        self.NumOfDate.setGeometry(QtCore.QRect(580, 110, 51, 21))
        self.NumOfDate.setReadOnly(True)
        self.NumOfDate.setObjectName("NumOfDate")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(640, 110, 101, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(680, 150, 72, 15))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(680, 190, 72, 15))
        self.label_5.setObjectName("label_5")
        self.AverageDate = QtWidgets.QLineEdit(Dialog)
        self.AverageDate.setGeometry(QtCore.QRect(750, 110, 71, 21))
        self.AverageDate.setReadOnly(True)
        self.AverageDate.setObjectName("AverageDate")
        self.MinDate = QtWidgets.QLineEdit(Dialog)
        self.MinDate.setGeometry(QtCore.QRect(750, 150, 71, 21))
        self.MinDate.setReadOnly(True)
        self.MinDate.setObjectName("MinDate")
        self.MaxDate = QtWidgets.QLineEdit(Dialog)
        self.MaxDate.setGeometry(QtCore.QRect(750, 190, 71, 21))
        self.MaxDate.setReadOnly(True)
        self.MaxDate.setObjectName("MaxDate")
        self.Reset_2 = QtWidgets.QPushButton(Dialog)
        self.Reset_2.setGeometry(QtCore.QRect(590, 300, 61, 31))
        self.Reset_2.setObjectName("Reset_2")
        self.Finish = QtWidgets.QPushButton(Dialog)
        self.Finish.setGeometry(QtCore.QRect(700, 300, 61, 31))
        self.Finish.setObjectName("Finish")
        self.Help = QtWidgets.QPushButton(Dialog)
        self.Help.setGeometry(QtCore.QRect(810, 300, 61, 31))
        self.Help.setObjectName("Help")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(40, 330, 131, 16))
        self.label_6.setObjectName("label_6")
        self.tableWidget_2 = QtWidgets.QTableWidget(Dialog)
        self.tableWidget_2.setGeometry(QtCore.QRect(30, 350, 1131, 192))
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(9)
        self.tableWidget_2.setRowCount(1)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignVCenter)
        self.tableWidget_2.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(8, item)
        self.line = QtWidgets.QFrame(Dialog)
        self.line.setGeometry(QtCore.QRect(560, 100, 20, 131))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(Dialog)
        self.line_2.setGeometry(QtCore.QRect(570, 90, 16, 21))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.line_3 = QtWidgets.QFrame(Dialog)
        self.line_3.setGeometry(QtCore.QRect(570, 210, 321, 41))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.line_4 = QtWidgets.QFrame(Dialog)
        self.line_4.setGeometry(QtCore.QRect(640, 70, 251, 61))
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.line_5 = QtWidgets.QFrame(Dialog)
        self.line_5.setGeometry(QtCore.QRect(880, 100, 20, 131))
        self.line_5.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "重复实验"))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("Dialog", "*"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "实验编号"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "平均排队时间"))
        self.label.setText(_translate("Dialog", "重复次数："))
        self.determine.setText(_translate("Dialog", "确定"))
        self.label_2.setText(_translate("Dialog", "实验数据"))
        self.label_3.setText(_translate("Dialog", "次实验平均值："))
        self.label_4.setText(_translate("Dialog", "最小值："))
        self.label_5.setText(_translate("Dialog", "最大值："))
        self.Reset_2.setText(_translate("Dialog", "重置"))
        self.Finish.setText(_translate("Dialog", "完成"))
        self.Help.setText(_translate("Dialog", "帮助"))
        self.label_6.setText(_translate("Dialog", "最后一次试验结果："))
        item = self.tableWidget_2.verticalHeaderItem(0)
        item.setText(_translate("Dialog", "*"))
        item = self.tableWidget_2.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "客户编号"))
        item = self.tableWidget_2.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "间隔时间"))
        item = self.tableWidget_2.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "到达时间"))
        item = self.tableWidget_2.horizontalHeaderItem(3)
        item.setText(_translate("Dialog", "服务时间"))
        item = self.tableWidget_2.horizontalHeaderItem(4)
        item.setText(_translate("Dialog", "服务开始时间"))
        item = self.tableWidget_2.horizontalHeaderItem(5)
        item.setText(_translate("Dialog", "等待时间"))
        item = self.tableWidget_2.horizontalHeaderItem(6)
        item.setText(_translate("Dialog", "服务结束时间"))
        item = self.tableWidget_2.horizontalHeaderItem(7)
        item.setText(_translate("Dialog", "客户在系统花费时间"))
        item = self.tableWidget_2.horizontalHeaderItem(8)
        item.setText(_translate("Dialog", "空闲时间"))

