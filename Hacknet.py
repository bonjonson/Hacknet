import sys
import os

code_list = '' #переменная для чтения содержимого файла
code = '' #переменная хранящая код
code_inputed = '' #переменная для хранения введённых кодов

try:
    open_file = open('hacknet.txt', 'r').read() # открываем файл и сохраняем его в переменную
except IOError:
    print('No file')
    sys.exit(0) #программа завершается, если не обнаружен файл
if os.stat('hacknet.txt').st_size > 0:
    code_list = open_file #считываем содержимое файла с кодами
    code_list = code_list.split() #разделяем строку на элементы и записываем в список
    for code in code_list:
        print('Enter your code: ') 
        code = input() #вводим код
        code_inputed = code_inputed + ' ' + code #вносим код в строку code_inputed
    code_inputed = code_inputed.split() #сохраняем строку в лист, в качестве разделителя используется пробел
    if code_list == code_inputed: #сравниваем два списка
        print("Access Granted", u'\u2705')
    else:
        print("Access Denied", u'\u274c')
else:
    print('File is empty')
    sys.exit(0) #завершаем программу, если файл пустой