# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'QtFormDeCoder.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(10, 10, 780, 22))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox.sizePolicy().hasHeightForWidth())
        self.comboBox.setSizePolicy(sizePolicy)
        self.comboBox.setObjectName("comboBox")
        self.label1 = QtWidgets.QLabel(self.centralwidget)
        self.label1.setGeometry(QtCore.QRect(10, 50, 131, 16))
        self.label1.setObjectName("label1")
        self.line1 = QtWidgets.QFrame(self.centralwidget)
        self.line1.setGeometry(QtCore.QRect(10, 40, 781, 16))
        self.line1.setFrameShape(QtWidgets.QFrame.HLine)
        self.line1.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line1.setObjectName("line1")
        self.lineEdit1 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit1.setGeometry(QtCore.QRect(10, 70, 781, 22))
        self.lineEdit1.setObjectName("lineEdit1")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 100, 111, 16))
        self.label.setObjectName("label")
        self.pushButton11 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton11.setGeometry(QtCore.QRect(390, 120, 401, 28))
        self.pushButton11.setObjectName("pushButton11")
        self.label2 = QtWidgets.QLabel(self.centralwidget)
        self.label2.setGeometry(QtCore.QRect(10, 520, 121, 16))
        self.label2.setObjectName("label2")
        self.lineEdit2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit2.setGeometry(QtCore.QRect(10, 540, 781, 22))
        self.lineEdit2.setObjectName("lineEdit2")
        self.pushButton2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton2.setGeometry(QtCore.QRect(390, 500, 401, 28))
        self.pushButton2.setObjectName("pushButton2")
        self.line2 = QtWidgets.QFrame(self.centralwidget)
        self.line2.setGeometry(QtCore.QRect(390, 470, 401, 20))
        self.line2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line2.setObjectName("line2")
        self.line3 = QtWidgets.QFrame(self.centralwidget)
        self.line3.setGeometry(QtCore.QRect(10, 510, 361, 16))
        self.line3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line3.setObjectName("line3")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(10, 120, 361, 381))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.pushButton12 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton12.setGeometry(QtCore.QRect(390, 160, 401, 28))
        self.pushButton12.setObjectName("pushButton12")
        self.pushButton13 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton13.setGeometry(QtCore.QRect(390, 200, 401, 28))
        self.pushButton13.setObjectName("pushButton13")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.comboBox.setCurrentIndex(-1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Простейшие алгоритмы сжатия - DeCoder"))
        self.label1.setText(_translate("MainWindow", "Сжатое сообщение"))
        self.lineEdit1.setText(_translate("MainWindow", "lineEdit1"))
        self.label.setText(_translate("MainWindow", "Кодовая тедовая таблица: добавить строку"))
        self.label2.setText(_translate("MainWindow", "Исходное сообщение"))
        self.lineEdit2.setText(_translate("MainWindow", "lineEdit2"))
        self.pushButton2.setText(_translate("MainWindow", "Декодирование"))
        self.pushButton12.setText(_translate("MainWindow", "Кодовая таблица: вставить строку"))
        self.pushButton13.setText(_translate("MainWindow", "Кодовая таблица: удалить строку"))
