import csv

def filter_employees_by_language(csv_file):
    try:
        # Ввод языка программирования для фильтрации
        search_language = input("Введите язык программирования для фильтрации: ").strip().lower()

        # Проверяем, существует ли файл
        try:
            with open(csv_file, 'r', encoding='utf-8') as file:
                reader = csv.reader(file)
                headers = next(reader)  # Считываем заголовки

                # Проверяем, есть ли столбец "Языки программирования"
                if "languages" not in headers:
                    return "В файле отсутствует столбец 'languages'."

                # Индекс столбца с языками программирования
                lang_index = headers.index("languages")

                # Список сотрудников, владеющих указанным языком
                matching_employees = []

                for row in reader:
                    if row and search_language in row[lang_index].lower():
                        matching_employees.append(dict(zip(headers, row)))

                # Результат фильтрации
                if matching_employees:
                    return f"Сотрудники, владеющие языком '{search_language}':\n" + "\n".join(
                        [str(employee) for employee in matching_employees]
                    )
                else:
                    return f"Сотрудников, владеющих языком '{search_language}', не найдено."

        except FileNotFoundError:
            return f"Файл '{csv_file}' не найден. Убедитесь, что путь указан верно."

    except Exception as e:
        return f"Произошла ошибка: {e}"

csv_file = r'C:\Users\User\Desktop\python_tasks\DZ\dz9\task5\data.csv' 
result = filter_employees_by_language(csv_file)
print(result)