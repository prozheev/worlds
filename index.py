from defwords import world

print()
print('Вычисляем количество слов в тексте:')
print()

while True:
    try:
        files = input('Введите путь к файлу и имя файла (либо несколько файлов через пробел): ')
        files_list = files.split(' ') # ['file1', 'file2']
        data = ''
        for a in files_list:
            file = open(a)
            data = data + file.read().lower()
    except Exception:
        print()
        print('Неверный путь и(или) имя файла(файлов)!')
        print()
        continue
    break

file1 = open("preps.txt")
preps_file = file1.read().lower()
file.close()
file1.close()

world(data, preps_file)

# txt/krovostok_cherepovets.txt
# /home/user/Code/Files_downloaded_by_AirDroid/krovostok_cherepovets.txt