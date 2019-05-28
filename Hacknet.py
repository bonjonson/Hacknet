import wget

open_file = '' #переменная для открытия файла
code_list = '' #переменная для чтения содержимого файла
code = '' #переменная хранящая код
code_inputed = '' #переменная для хранения введённых кодов

#wget.download = ('http://hacknet.commando21.ru", 'hacknet.txt') #Загрузка файла с кодами
try:
    open_file = open('hacknet.txt', 'r') # открываем файл и сохраняем его в переменную
except IOError:
    print('No file')
#code_list.split #сохраняем строку в лист, в качестве разделителя используется пробел
code_list = open_file.read() #считываем содержимое файла с кодами
code_list = code_list.split() #разделяем строку на элементы и записываем в список
print(code_list) # дебаг
for code in code_list:
    code = input() #вводим код
    code_inputed = code_inputed + ' ' + code #вносим код в строку code_inputed
code_inputed = code_inputed.split() #сохраняем строку в лист, в качестве разделителя используется пробел
print(code_inputed) #дебаг
if code_list == code_inputed: #сравниваем два списка
    print("Access Granted")
else:
    print("You're Wrong")