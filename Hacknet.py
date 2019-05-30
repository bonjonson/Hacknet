import sys
import os
import subprocess
import time


code_list = '' #переменная для чтения содержимого файла
code = '' #переменная хранящая код
code_inputed = '' #переменная для хранения введённых кодов

subprocess.call('./download_codes.sh', shell = True) #вызов внешнего скрипта
print('Connecting to hacknet server') #приветственное сообщение
time.sleep(5) #пауза для гарантированной загрузки файла
team_id = (input('Enter your team id: ')) #ввод номера команда
print("You're logged in as team #" + team_id, '\n') #вывод подтверждения ввхода в программу

try:
    open_file = open('hacknet.txt', 'r').read() # открываем файл и сохраняем его в переменную
except IOError:
    print('No file')
    sys.exit(0) #программа завершается, если не обнаружен файл
if os.stat('hacknet.txt').st_size > 0:
    code_list = open_file.split() #считываем содержимое файла с кодами
    for code in code_list: 
        code = input('Enter your code: ') #вводим код
        code_inputed = code_inputed + ' ' + code #вносим код в строку code_inputed
    code_inputed = code_inputed.split() #сохраняем строку в лист, в качестве разделителя используется пробел
    if code_list == code_inputed: #сравниваем два списка
        print("Access Granted", u'\u2705')
        #Графический таймер с обратным отсчетом
        for remaining in range(10, 0, -1):
            sys.stdout.write("\r")
            sys.stdout.write("Starting upload security codes on Hacknet servers: ")
            sys.stdout.write("{:2d} seconds remaining.".format(remaining)) 
            sys.stdout.flush()
            time.sleep(1)
        sys.stdout.write("\rTransfer complite!                                                         \n")
        time.sleep(1)
        print("Congratulation! Team #"+ team_id, " You're won!")
    else:
        print("Access Denied", u'\u274c')
else:
    print('File is empty')
    sys.exit(0) #завершаем программу, если файл пустой
time.sleep(3) #пауза для гарантированного завершения программы
subprocess.call('./rmrf.sh', shell = True) #вызов скрипта удаления файла с кодами
