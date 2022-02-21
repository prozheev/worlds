import re
from collections import Counter
from prettytable import PrettyTable

def dates():
    while True:
        try:
            x = 1
            files = input('Введите путь к файлу и имя файла (либо несколько файлов через пробел): ')
            files_list = files.split(' ') # ['file1', 'file2']
            data = {}
            data1 = ''

            print('\nВыбрано файлов: ' + str(len(files_list)) + '.')
            for a in files_list:
                file = open(a)
                file1 = open(a)
                data[x] = file.read().lower()
                data1 = data1 + file1.read().lower()
                file.close()
                x = x + 1
        except Exception:
            print('\nНеверный путь и(или) имя файла(файлов)!\n')
            continue
        return data, data1, files_list

def start(data, preps_file):
    while True:
        h = input('\nВведите цифрой, как бы вы хотели разобрать файлы?\n\n1: Объеденить в один.\n2: Каждый файл отдельно.\n \nВвод "1" или "2": ')
        if h == str(1):
            world(data[1], preps_file)
        elif h == str(2):
            x = 1
            for a in data[0]:

                print('\nФайл ' + str(x) + ': ' + data[-1][x-1])
                world(data[0][x], preps_file)
                x = x + 1

        else:
            print('\nНеверный ввод! Попробуйте ещё раз.')
            continue
        break

def world(data, preps_file):

    words = re.findall(r"[\w']+", data)
    preps = re.findall(r"[\w']+", preps_file)

    words_clear = [a for a in words if a not in preps]
    orig = set(words_clear) # Словарь без повторений

    words1 = Counter(words_clear)

    list_c = list(words1.items())
    list_c.sort(key=lambda i: i[1], reverse = True)

    print('\nВсего слов без предлогов: ' + str(len(words_clear)) + '. ' + 'Из них оригинальных: ' + str(len(orig))+ '.\n')
   
    print('\n' + str(pretty(words_clear, list_c)))


def range(list_c):
    while True:
        try:
            range = int(input('Введите сколько слов вы хотите увидеть: '))
            if range > 0:
                top15 = {f'{a}': int(b) for a, b in list_c[0:range]}
            else:
                print('\nОй! Похоже вы ввели неправильное число.. Попробуйте снова.\n')
                continue

        except Exception:
            print('\nНеверный ввод! Попробуйте ещё раз.\n')
            continue
        return top15

def pretty(words_clear, list_c):
    top15 = range(list_c)
    z = PrettyTable()

    row = {}
    x = 1

    for a, b in top15.items(): # [('a', 1), ('b', 2)]
        row[x] = b
        z.add_row([x, a.capitalize(), row[x], round(b / len(words_clear) * 100, 2)])
        x = x + 1

    z.field_names  =  ["n", "Слово",  "Употр.раз", "Проценты"]
    return z