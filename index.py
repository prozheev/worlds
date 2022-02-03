import re
from collections import Counter

file = open("krovostok_cherepovets.txt")
# file = open('Files_downloaded_by_AirDroid/krovostok_cherepovets.txt')
data = file.read().lower()
#print(data)
file.close()
words = re.findall(r"[\w']+", data)
orig = set(words) # Словарь без повторений

words1 = Counter(words)

list_c = list(words1.items())

list_c.sort(key=lambda i: i[1], reverse = True)
#top15 = {}
top15 = {f'{a}': int(b) for a, b in list_c[0:15]}
print()
print('Всего слов в тексте: ' + str(len(words)) + '. ' + 'Из них оригинальных: ' + str(len(orig))+ '.')
print()
print('Самые популярные слова в тексте и кол-во их повторений:') 
x = 1
for a, b in top15.items(): # [('a', 1), ('b', 2)]
    print(str(x) + '. ' + a.capitalize(), '-', str(b) + ' раз(а)')
    x = x + 1
print()
print('Что в процентном соотношении от общего колличества:')
x = 1
for a, b in top15.items(): # [('a', 1), ('b', 2)]
    print(str(x) + '. ' + a.capitalize(), '-', str(len(words) / 100 * b) + ' %')
    x = x + 1