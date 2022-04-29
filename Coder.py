#!/usr/bin/python3
# -*- coding: utf-8 -*-

from PyQt5 import QtWidgets 
import sys
# импорт сгенерированной фармы
from QtFormCoder import Ui_MainWindow
# и функционала
import SimplestCompression as sc

class cWindow(QtWidgets.QMainWindow):
	def __init__(self):
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
		# подключение клик-сигнала к слоту btn1Clicked 
		self.ui.pushButton1.clicked.connect(self.btn1Clicked) 
		# подключение клик-сигнала к слоту btn2Clicked 
		self.ui.pushButton2.clicked.connect(self.btn2Clicked)
		self.ui.pushButton3.clicked.connect(self.btn3Clicked)
		pass
	def btn3Clicked(self):
		rowCol = self.ui.tableWidget.rowCount()

		import xml.etree.ElementTree as ET

		root = ET.Element('data')
		tree = ET.ElementTree(element=root)

		employ_methodcode = ET.SubElement(root, 'method-code')
		employ_methodcode.text = 'Метод Хафмана'
		employ_textcode= ET.SubElement(root, 'text-code')
		employ_textcode.text = self.ui.lineEdit2.text()

		employee_table = ET.SubElement(root, 'table')
		for row in range(rowCol):
			print('x=',self.ui.tableWidget.item(row, 0).text())
			print('p=',self.ui.tableWidget.item(row, 1).text())
			print('code=',self.ui.tableWidget.item(row, 2).text())

			employee_row = ET.SubElement(employee_table, 'row')

			employ_symbol = ET.SubElement(employee_row, 'symbol')
			employ_symbol.text = self.ui.tableWidget.item(row, 0).text()
			employ_p = ET.SubElement(employee_row, 'probability')
			employ_p.text = self.ui.tableWidget.item(row, 1).text()
			employ_code = ET.SubElement(employee_row, 'code')
			employ_code.text = self.ui.tableWidget.item(row, 2).text()
		# xml_declaration=Trueにすると、バージョン情報など書き込んでくれる
		tree.write('test.xml', encoding='utf-8', xml_declaration=True)
		tree = ET.ElementTree(file='test.xml')
		return
	def btn1Clicked(self):
	# Прочитаем исходное сообщение
		tInputText = self.ui.lineEdit1.text()
		nInputText = len(tInputText)
		if nInputText == 0:
			msg = QtWidgets.QMessageBox()
			msg.setWindowTitle('Информация')
			msg.setText('Исходное сообщение должно содержать ' + \
			'хотя бы 1 символ!')
			msg.setDetailedText('Длина исходного сообщения ' + \
			'должна быть больше 0')
			msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
			msg.exec_()
			return
		# Создадим кодовую таблицу выбранным методом
		nMethod = self.ui.comboBox.currentIndex()
		codeTable = sc.makeCodeTable(tInputText, nMethod)
		# Запишем кодовую таблицу
		self.ui.tableWidget.clearContents()
		self.ui.tableWidget.setRowCount(len(codeTable))
		row = 0
		for cElem in codeTable:
			cellInfo = QtWidgets.QTableWidgetItem(cElem.x)
			self.ui.tableWidget.setItem(row, 0, cellInfo)
			cellInfo = QtWidgets.QTableWidgetItem(str(cElem.p) + \
			'/' + str(nInputText))
			self.ui.tableWidget.setItem(row, 1, cellInfo)
			cellInfo = QtWidgets.QTableWidgetItem(cElem.code)
			self.ui.tableWidget.setItem(row, 2, cellInfo)
			row += 1
		return
	def btn2Clicked(self):
		# Прочитаем исходное сообщение
		tInputText = self.ui.lineEdit1.text()
		if len(tInputText) == 0:
			msg = QtWidgets.QMessageBox()
			msg.setWindowTitle('Информация')
			msg.setText('Исходное сообщение должно содержать ' + \
			'хотя бы 1 символ!')
			msg.setDetailedText('Длина исходного сообщения ' + \
			'должна быть больше 0')
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
			'хотя бы 1 элемент')
			msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
			msg.exec_()
			return
		codeTable = []
		for row in range(nCodeTable):
			cellInfo = QtWidgets.QTableWidgetItem(self.ui.tableWidget.item(row, 0))
			x = str(cellInfo.text()).strip()
			if x == '':
				x = ' '
			cellInfo = QtWidgets.\
				QTableWidgetItem(self.ui.tableWidget.item(row, 1))
			try:
				p = int(str(cellInfo.text()).strip().split('/', 2)[0])
			except ValueError:
				p = 0
			cellInfo = QtWidgets.\
				QTableWidgetItem(self.ui.tableWidget.item(row, 2))
			codeTable.append(\
				sc.codeElem(x, p, code=str(cellInfo.text()).strip()))
		# Создадим и запишем закодированное сообщение
		tOutputText, hx, mlx, sizeOutputText = sc.makeCodeText(tInputText, codeTable)
		self.ui.lineEdit2.setText(tOutputText)
		# энтропию H(X) и среднюю длину кодовых слов ML(X)
		self.ui.lineEdit3.setText(str(hx))
		self.ui.lineEdit4.setText(str(mlx))
		# а также длину закодированного сообщения и коэффициент сжатия
		self.ui.lineEdit5.setText(str(sizeOutputText))
		self.ui.lineEdit6.setText(str(sizeOutputText/(len(tInputText)*sc.sizeSymbol)))
		return

app = QtWidgets.QApplication([])
application = cWindow() 
application.show()

sys.exit(app.exec())