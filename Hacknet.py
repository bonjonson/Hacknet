import requests
import sys

code_list = '' #переменная для чтения содержимого файла
code = '' #переменная хранящая код
code_inputed = '' #переменная для хранения введённых кодов

try:
    open_file = open(r'hacknet.txt', 'wb') #открываем файл для записи
    ufr = requests.get('http://commando21.ru/hacknet.txt') #создаем запрос
    open_file.write(ufr.content) #записываем содержимое в файл
except IOError:
    print('No file')
    sys.exit(0) #программа завершается, если не обнаружен файл
#code_list.split #сохраняем строку в лист, в качестве разделителя используется пробел
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
