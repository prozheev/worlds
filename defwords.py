def world(data, preps_file):
    import re
    from collections import Counter
    from prettytable import PrettyTable
    words = re.findall(r"[\w']+", data)
    preps = re.findall(r"[\w']+", preps_file)

    words_clear = [a for a in words if a not in preps]
    orig = set(words_clear) # Словарь без повторений

    words1 = Counter(words_clear)

    list_c = list(words1.items())

    list_c.sort(key=lambda i: i[1], reverse = True)
    print()
    print('Всего слов без предлогов: ' + str(len(words_clear)) + '. ' + 'Из них оригинальных: ' + str(len(orig))+ '.')
    print()

    while True:
        try:
            top15 = {f'{a}': int(b) for a, b in list_c[0:int(input('Введите сколько слов вы хотите увидеть: '))]}
            
        except Exception:
            print()
            print('Неверный ввод! Попробуйте ещё раз.')
            print()
            continue
        break

    z = PrettyTable()

    row = {}
    x = 1

    for a, b in top15.items(): # [('a', 1), ('b', 2)]
        row[x] = b
        z.add_row([x, a.capitalize(), row[x], round(b / len(words_clear) * 100, 2)])
        x = x + 1

    print()
    z.field_names  =  ["n", "Слово",  "Употр.раз", "Проценты"]
    print(z)