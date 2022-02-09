import re
from collections import Counter
from prettytable import PrettyTable

file = open(input("Введите путь к файлу и имя файла: "))
file1 = open("preps.txt")
# file = open('Files_downloaded_by_AirDroid/krovostok_cherepovets.txt')
data = file.read().lower()
preps_file = file1.read().lower()
file.close()
file1.close
words = re.findall(r"[\w']+", data)
preps = re.findall(r"[\w']+", preps_file)
print('OK')
words_clear = [a for a in words if a not in preps]
orig = set(words_clear) # Словарь без повторений

words1 = Counter(words_clear)

list_c = list(words1.items())

list_c.sort(key=lambda i: i[1], reverse = True)
#top15 = {}
top15 = {f'{a}': int(b) for a, b in list_c[0:15]}
print()
print('Всего слов без предлогов: ' + str(len(words_clear)) + '. ' + 'Из них оригинальных: ' + str(len(orig))+ '.')
print()
print('Самые популярные слова в тексте и кол-во их повторений:') 

z = PrettyTable()
row = {}
x = 1
for a, b in top15.items(): # [('a', 1), ('b', 2)]
    print(str(x) + '. ' + a.capitalize(), '-', str(b) + ' раз(а)')
    row[x] = b
    x = x + 1

print()
print('Что в процентном соотношении от общего колличества:')
x = 1
for a, b in top15.items(): # [('a', 1), ('b', 2)]
    # print(str(x) + '. ' + a.capitalize(), '-', format(b / len(words_clear) * 100, '.3f') + ' %')
    print(str(x) + '. ' + a.capitalize(), '-', str(round(b / len(words_clear) * 100, 3)) + ' %')
    z.add_row([a.capitalize(), row[x], round(b / len(words_clear) * 100, 3)])
    x = x + 1

print()
z.field_names  =  ["Слово",  "Употр. раз", "Проценты"]
print(z)

# round
# repr
# /home/user/Code/Files_downloaded_by_AirDroid/krovostok_cherepovets.txt