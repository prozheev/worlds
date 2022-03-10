#!/usr/bin/env python3

from defwords import dates, start
import os

print('\nВычисляем количество слов в тексте:\n')
while True:
    try:
        files = input('Введите путь к файлу и имя файла (либо несколько файлов через пробел): ') # !
        data = dates(files)
        print('\nВыбрано файлов: ' + str(len(data[-1])) + '.')
        while True:
            sel = input('\nВведите цифрой, как бы вы хотели разобрать файлы?\n\n1: Объеденить в один.\n2: Каждый файл отдельно.\n \nВвод "1" или "2": ') # !
            if sel == str(1) or sel == str(2):
                pass

            else:
                print('\nНеверный ввод! Попробуйте ещё раз.')
                continue
            break
    except FileNotFoundError: # !
        print('\nНеверный путь и(или) имя файла(файлов)!\n')
        continue
    break

# file1 = open("preps.txt")
# preps_file = file1.read().lower()
# file1.close()

with open(os.path.dirname(__file__) + "/preps.txt") as file:
    preps_file = file.read().lower()

start(data, preps_file, sel)


# txt/krovostok_cherepovets.txt
# /home/user/Code/Files_downloaded_by_AirDroid/krovostok_cherepovets.txt
# 1 krovostok_cherepovets_copy.txt