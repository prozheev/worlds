from defwords import world

print()
print('Вычисляем количество слов в тексте:')
print()

while True:
    try:
        x = 1
        files = input('Введите путь к файлу и имя файла (либо несколько файлов через пробел): ')
        files_list = files.split(' ') # ['file1', 'file2']
        data = {}
        file1 = open("preps.txt")
        preps_file = file1.read().lower()
        file1.close()
        print()
        print('Выбрано файлов: ' + str(len(files_list)) + '.')
        for a in files_list:
            print()
            print('Файл ' + str(x) + ': ' + a)
            file = open(a)
            data[x] = file.read().lower()
            file.close()
            world(data[x], preps_file)
            x = x + 1
    except Exception:
        print()
        print('Неверный путь и(или) имя файла(файлов)!')
        print()
        continue
    break

# txt/krovostok_cherepovets.txt
# /home/user/Code/Files_downloaded_by_AirDroid/krovostok_cherepovets.txt