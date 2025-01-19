# Ввод данных
username = input("Введите имя: ")
content = input("Введите содержание заметки: ")
status = input("Введите статус заметки: ")
creation_date = input("Введите дату создания заметки (в формате ГГГГ-ММ-ДД): ")
modification_date = input("Введите дату изменения заметки (в формате ГГГГ-ММ-ДД): ")

# Ввод заголовков заметки
title_1 = input("Введите первый заголовок: ")
title_2 = input("Введите второй заголовок: ")

# Создание словаря для заметки
note = {
    "username": username,
    "content": content,
    "status": status,
    "creation_date": creation_date,
    "modification_date": modification_date,
    "titles": [title_1, title_2],  # список заголовков
}

# Вывод данных
print("\nДанные заметки:")
print(f"Имя пользователя: {note['username']}")
print(f"Содержание заметки: {note['content']}")
print(f"Статус: {note['status']}")
print(f"Дата создания: {note['creation_date']}")
print(f"Дата изменения: {note['modification_date']}")
print("Заголовки:")
print(f"Заголовок 1: {note['titles'][0]}")
print(f"Заголовок 2: {note['titles'][1]}")
