with open("test.py", "r", encoding="utf-8") as f:  #Вместо test.py пишешь название своего файла
    lines = f.readlines()

with open("test.py", "w", encoding="utf-8") as f:  #Вместо test.py пишешь название своего файла
    for line in lines:
        if not line.startswith("#"):
            f.write("#" + line)
        else:
            f.write(line)
print('Готово')
