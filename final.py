# ВВод данных
username = input("Введите имя: ")
content = input("Введите содержание заметки: ")
status = input("Введите статус заметки: ")
creation_date = input("Введите дату создания заметки: ")
modification_date = input("Введите дату изменения заметки: ")

# Ввод заголовков заметки
title_1 = input("Введите первый заголовок: ")
title_2 = input("Введите второй заголовок: ")

# Создание списка заголовков
note = [
    username,
    content,
    status,
    creation_date,
    modification_date,
    [title_1, title_2]
]
# Вывод данных
print("\nДанные заметки:")
print(f"Имя пользователя: {note[0]}")
print(f"Содержание заметки: {note[1]}")
print(f"Статус: {note[2]}")
print(f"Дата создания: {note[3]}")
print(f"Дата изменения: {note[4]}")
print("Заголовки:")
print("Заголовок 1: ", note[5][0])
print("Заголовок 2: ", note[5][1])
