created_date = "19.03.2024"
issue_date = "19.03.2024"

# Убираем год из даты с помощью срезов строк
temp_created_date = created_date[:5]
temp_issue_date = issue_date[:5]

# Вывод измененных дат
print("Создано:", temp_created_date)
print("Дата задачи:", temp_issue_date)
