# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'QtFormCoder.ui'
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
        self.pushButton1 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton1.setGeometry(QtCore.QRect(390, 120, 401, 28))
        self.pushButton1.setObjectName("pushButton1")
        self.label2 = QtWidgets.QLabel(self.centralwidget)
        self.label2.setGeometry(QtCore.QRect(10, 520, 121, 16))
        self.label2.setObjectName("label2")
        self.lineEdit2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit2.setGeometry(QtCore.QRect(10, 540, 781, 22))
        self.lineEdit2.setObjectName("lineEdit2")
        self.pushButton3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton3.setGeometry(QtCore.QRect(390, 340, 401, 28))
        self.pushButton3.setObjectName("pushButton2")
        self.pushButton2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton2.setGeometry(QtCore.QRect(390, 150, 401, 28))
        self.pushButton2.setObjectName("pushButton2")
        self.label3 = QtWidgets.QLabel(self.centralwidget)
        self.label3.setGeometry(QtCore.QRect(510, 380, 91, 16))
        self.label3.setObjectName("label3")
        self.lineEdit3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit3.setGeometry(QtCore.QRect(610, 380, 111, 22))
        self.lineEdit3.setObjectName("lineEdit3")
        self.label3p = QtWidgets.QLabel(self.centralwidget)
        self.label3p.setGeometry(QtCore.QRect(730, 380, 55, 16))
        self.label3p.setObjectName("label3p")
        self.label4 = QtWidgets.QLabel(self.centralwidget)
        self.label4.setGeometry(QtCore.QRect(390, 410, 221, 16))
        self.label4.setObjectName("label4")
        self.lineEdit4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit4.setGeometry(QtCore.QRect(610, 410, 113, 22))
        self.lineEdit4.setObjectName("lineEdit4")
        self.label4p = QtWidgets.QLabel(self.centralwidget)
        self.label4p.setGeometry(QtCore.QRect(730, 410, 55, 16))
        self.label4p.setObjectName("label4p")
        self.label5 = QtWidgets.QLabel(self.centralwidget)
        self.label5.setGeometry(QtCore.QRect(440, 440, 161, 16))
        self.label5.setObjectName("label5")
        self.lineEdit5 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit5.setGeometry(QtCore.QRect(610, 440, 113, 22))
        self.lineEdit5.setObjectName("lineEdit5")
        self.label5p = QtWidgets.QLabel(self.centralwidget)
        self.label5p.setGeometry(QtCore.QRect(730, 440, 55, 16))
        self.label5p.setObjectName("label5p")
        self.label6 = QtWidgets.QLabel(self.centralwidget)
        self.label6.setGeometry(QtCore.QRect(470, 470, 131, 16))
        self.label6.setObjectName("label6")
        self.lineEdit6 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit6.setGeometry(QtCore.QRect(610, 470, 113, 22))
        self.lineEdit6.setObjectName("lineEdit6")
        self.label6p = QtWidgets.QLabel(self.centralwidget)
        self.label6p.setGeometry(QtCore.QRect(610, 500, 181, 16))
        self.label6p.setObjectName("label6p")
        self.line2 = QtWidgets.QFrame(self.centralwidget)
        self.line2.setGeometry(QtCore.QRect(390, 320, 391, 20))
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
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.comboBox.setCurrentIndex(-1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Простейшие алгоритмы сжатия - Coder"))
        self.label1.setText(_translate("MainWindow", "Исходное сообщение"))
        self.lineEdit1.setText(_translate("MainWindow", "красная_краска"))
        self.label.setText(_translate("MainWindow", "Кодовая таблица"))
        self.pushButton1.setText(_translate("MainWindow", "Проход 1: Создание кодовой таблицы"))
        self.label2.setText(_translate("MainWindow", "Сжатое сообщение"))
        self.lineEdit2.setText(_translate("MainWindow", "lineEdit2"))
        self.pushButton2.setText(_translate("MainWindow", "Проход 2: Сжатие"))
        self.pushButton3.setText(_translate("MainWindow", "Сохранить данные в XML"))
        self.label3.setText(_translate("MainWindow", "Энтропия H(X)"))
        self.lineEdit3.setText(_translate("MainWindow", "lineEdit3"))
        self.label3p.setText(_translate("MainWindow", "бит/сим"))
        self.label4.setText(_translate("MainWindow", "Средняя длина кодовых слов ML(X)"))
        self.lineEdit4.setText(_translate("MainWindow", "lineEdit4"))
        self.label4p.setText(_translate("MainWindow", "бит/сим"))
        self.label5.setText(_translate("MainWindow", "Длина сжатого сообщения"))
        self.lineEdit5.setText(_translate("MainWindow", "lineEdit5"))
        self.label5p.setText(_translate("MainWindow", "бит"))
        self.label6.setText(_translate("MainWindow", "Коэффициент сжатия"))
        self.lineEdit6.setText(_translate("MainWindow", "lineEdit6"))
        self.label6p.setText(_translate("MainWindow", "(без учета кодовой таблицы)"))
