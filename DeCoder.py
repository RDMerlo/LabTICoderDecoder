#!/usr/bin/python3
# -*- coding: utf-8 -*--

from PyQt5 import QtWidgets
import sys
# импорт сгенерированной фармы
from QtFormDeCoder import Ui_MainWindow
# и функционала
import SimplestCompression as sc

# Классы

class cWindow(QtWidgets.QMainWindow):
    mtd_operation = {'mtd-shanon-fano': sc.nMethodShannonFano, 'mtd-huffman': sc.nMethodHuffman}

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
        self.ui.pushButton14.clicked.connect(self.btn14Clicked)
        pass

    def btn14Clicked(self):
        import xml.etree.ElementTree as ET
        tree = ET.parse('test.xml')
        root = tree.getroot()

        self.ui.comboBox.setCurrentIndex(self.mtd_operation.get(root.find('method-code').text))

        employ_textcode = root.find('text-code').text

        self.ui.lineEdit1.setText(employ_textcode)

        employ_table = root.find('table')
        self.ui.tableWidget.clearContents()

        for table in employ_table:
            rowCol = self.ui.tableWidget.rowCount()
            self.ui.tableWidget.setRowCount(rowCol+1)

            employ_x= table.find('symbol').text
            self.ui.tableWidget.setItem(rowCol, 0, QtWidgets.QTableWidgetItem(employ_x))
            employ_p = table.find('probability').text
            self.ui.tableWidget.setItem(rowCol, 1, QtWidgets.QTableWidgetItem(employ_p))
            employ_code = table.find('code').text
            self.ui.tableWidget.setItem(rowCol, 2, QtWidgets.QTableWidgetItem(employ_code))
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
        # Создадим и запишем исходное сообщение
        tOutputText = sc.makeDeCodeText(tInputText, codeTable)
        self.ui.lineEdit2.setText(tOutputText)
        return

# -*- Main -*-
app = QtWidgets.QApplication([])
application = cWindow()
application.show()
sys.exit(app.exec())