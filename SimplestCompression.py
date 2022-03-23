# -*- coding: utf-8 -*-
# Подключаемые модули
import math

# from typing import ParamSpecArgs
# Константы
nMethodShannonFano = 0  # Метод Шеннона-Фано
tMethodShannonFano = 'Метод Шеннона-Фано'
nMethodHuffman = 1
# Метод Хаффмана
tMethodHuffman = 'Метод Хаффмана'
# Список методов
listMethod = (tMethodShannonFano, tMethodHuffman)
sizeSymbol = 8


# Размер 1-го символ в битах
# Функции и классы
# Элемент кодовой таблицы
class codeElem:
    def __init__(self, x, p, code='', left=None, right=None):
        self.x = x
        # Символ
        self.p = p
        # Вероятность (частота) появления
        self.code = code
        # Код
        self.left = left
        # Ссылка на "левый" элемент
        # (необходим для метода Хаффмана)
        self.right = right  # Ссылка на "правый" элемент
        # (необходим для метода Хаффмана)
        pass

    # Рекурсия для создания кодов (необходима для метода Хаффмана)
    def makeCode(self, newCode):
        self.code = newCode
        if self.left != None:
            self.left.makeCode(newCode + '0')
        if self.right != None:
            self.right.makeCode(newCode + '1')
        pass

    # Сравнение ("меньше") элементов кодовой таблицы
    def __lt__(self, other):
        return (self.p > other.p) or ((self.p == other.p) and (self.x < other.x))


def makeShannonFano(bTable):
    # Действуем до тех пор, пока список содержит более 1 элемента
    if len(bTable) > 1:
        pass
    # Подсчитаем сумму вероятностей (частот)
    # ...
    # Определим количество элементов с начала списка,
    # для которых сумма вероятностей (частот) меньше половины
    # общей суммы
    # ...
    # Тогда сумма вероятностей (частот) второй половины равна ...
    # ...
    # Если перемещение k-го элемента уменьшает разницу,
    # то выполним это
    # ...
    # Cформируем список из первой половины
    cTable = []
    # ...
    # приписывая кодам ее элементов "0"
    # ...
    # Запускаем рекурсию на список из первой половины
    makeShannonFano(cTable)
    # Cформируем список из второй половины
    dTable = []
    # ...
    # приписывая кодам ее элементов "1"
    # ...
    # Запускаем рекурсию на список из второй половины
    makeShannonFano(dTable)
    pass


def makeHuffman(bTable):
    # Новым промежуточным вершинам дерева будем присваивать символы
    # с конца таблицы

    #
    # работа идёт через класс codeElem, чтобы работало сравненние - мы используем bCh = 0xffff
    #
    bCh = 0xffff # промежуточное значение
    # Формируем дерево
    k = len(bTable)


    # Пока не достигнут корень дерева
    while k > 1:
        # Сортируем список
        # ...
        # Создаем промежуточную вершину, ссылающуюся на 2 последних
        # элемента списка
        # ...
        # Удаляем из списка 2 последних элемента
        # ...
        # Добавляем в конец списка промежуточную вершину
        # ...
        # Новым промежуточным вершинам дерева будем присваивать символы
        # с конца таблицы
        bCh -= 1
        k -= 1
    # k = len(bTable)
    # Запускаем рекурсию по созданию кодов
    bTable[0].makeCode('')
    pass


def makeCodeTable(tInput, nMethod):
    # Разберем исходный текст на символы, подсчитаем их частоты
    aTable = []
    for ch in tInput:
        for k in range(len(aTable)):
            if aTable[k].x == ch:
                aTable[k].p += 1
                break
        else:
            # Формируем список из символов с их частотами
            aTable.append(codeElem(ch, 1))
    # Сортируем список
    aTable.sort()
    for a in aTable:
        print(a.x, a.p)
    # Создаем поверхностную копию списка, которая будет преобразована в
    # B-Tree
    bTable = aTable.copy()
    # Если метод Шеннона-Фано, создаем код по методу Шеннона-Фано
    if nMethod == nMethodShannonFano:
        makeShannonFano(bTable)
    # Если метод Хаффмана, создаем код по методу Хаффмана
    elif nMethod == nMethodHuffman:
        makeHuffman(bTable)
    return aTable


def makeCodeText(tInput, aTable):
    # Длина исходного сообщения в символах
    nInput = len(tInput)
    # Получим сжатое сообщение
    tOutput = ''
    for ch in tInput:
        for elem in aTable:
            if ch == elem.x:
                tOutput += elem.code
                break
    # Вычислим энтропию H(X) и среднюю длину кодовых слов ML(X)
    hx = 0.0;
    mlx = 0
    for elem in aTable:
        hx += -(elem.p / nInput) * math.log2(elem.p / nInput)
        mlx += len(elem.code) * (elem.p / nInput)
    return tOutput, hx, mlx, len(tOutput)


def makeDeCodeText(tInput, aTable):
	# Получим исходное сообщение
	tOutput = ''
	k = 0;
	j = 1
	while k + j <= len(tInput):
		tCode = tInput[k: k + j]
		for elem in aTable:
			if tCode == elem.code:
				tOutput += elem.x
				k += j;j = 1
				break
		else:
			j += 1
	return tOutput