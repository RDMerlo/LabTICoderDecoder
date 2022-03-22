#!/usr/bin/python3
# -*- coding: utf-8 -*--

from PyQt5 import QtWidgets
import sys
# импорт сгенерированной фармы
from forms.QtFormDeCoder import Ui_MainWindow
# и функционала
import SimplestCompression as sc

# Классы

class cWindow(QtWidgets.QMainWindow):
    def __init__(self):
        # Дополнительные настройки формы
        super(cWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.comboBox.addItems(sc.listMethod)
        self.ui.comboBox.setCurrentIndex(sc.nMethodHuffman)
        self.ui.tableWidget.setColumnCount(3)
        self.ui.tableWidget.setHorizontalHeaderLabels(['X', 'P', 'Code'])
        self.ui.tableWidget.setColumnWidth(0, 50)
        self.ui.tableWidget.setColumnWidth(1, 130)
        self.ui.tableWidget.setColumnWidth(2, 130)
        self.ui.tableWidget.setRowCount(0)
        # подключение клик-сигнал к слоту btn11Clicked
        self.ui.pushButton11.clicked.connect(self.btn11Clicked)
        # подключение клик-сигнал к слоту btn12Clicked
        self.ui.pushButton12.clicked.connect(self.btn12Clicked)
        # подключение клик-сигнал к слоту btn13Clicked
        self.ui.pushButton13.clicked.connect(self.btn13Clicked)
        # подключение клик-сигнал к слоту btn2Clicked
        self.ui.pushButton2.clicked.connect(self.btn2Clicked)
        pass

    def btn11Clicked(self):
        row = self.ui.tableWidget.rowCount()
        self.ui.tableWidget.insertRow(row)
        pass

    def btn12Clicked(self):
        row = self.ui.tableWidget.currentRow()
        self.ui.tableWidget.insertRow(row)
        pass

    def btn13Clicked(self):
        row = self.ui.tableWidget.currentRow()
        self.ui.tableWidget.removeRow(row)
        pass

    def btn2Clicked(self):
        # Прочитаем исходное сообщение
        tInputText = self.ui.lineEdit1.text()
        if len(tInputText) == 0:
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle('Информация')
            msg.setText('Исходное сообщение должно содержать ' + \
                    'хотя бы 1 символ!')
            msg.setDetailedText('Длина исходного сообщения ' + \
                    'должна быть больше0')
            msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
            msg.exec_()
            return
        print(1)
        # Прочитаем кодовую таблицу
        nCodeTable = self.ui.tableWidget.rowCount()
        if nCodeTable == 0:
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle('Информация')
            msg.setText('Кодовая таблица пуста!')
            msg.setDetailedText('Кодовая таблица должна содержать ' + \
                    'хотя быn 1 элемент')
            msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
            msg.exec_()
            return
        print(2)
        codeTable = []
        for row in range(nCodeTable):
            cellInfo = QtWidgets. \
                QTableWidgetItem(self.ui.tableWidget.item(row, 0))
            x = str(cellInfo.text()).strip()
            if x == '':
                x = ' '
            cellInfo = QtWidgets. \
                QTableWidgetItem(self.ui.tableWidget.item(row, 1))
            try:
                p = int(str(cellInfo.text()).strip().split(' / ', 2)[0])
            except ValueError:
                p = 0
                cellInfo = QtWidgets.QTableWidgetItem(self.ui.tableWidget.item(row, 2))
                codeTable.append(sc.codeElem(x, p, code=str(cellInfo.text()).strip()))
        print(3)
        # Создадим и запишем исходное сообщение
        # FIXME:
        tOutputText = sc.makeDeCodeText(tInputText, codeTable)
        self.ui.lineEdit2.setText(tOutputText)
        return

# -*- Main -*-
app = QtWidgets.QApplication([])
application = cWindow()
application.show()
sys.exit(app.exec())