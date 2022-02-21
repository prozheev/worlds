from defwords import dates, start

print('\nВычисляем количество слов в тексте:\n')

data = dates()

file1 = open("preps.txt")
preps_file = file1.read().lower()
file1.close()

start(data, preps_file)

# txt/krovostok_cherepovets.txt
# /home/user/Code/Files_downloaded_by_AirDroid/krovostok_cherepovets.txt