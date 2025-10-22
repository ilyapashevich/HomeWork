import csv

def find_employee_by_name(csv_file):
    try:
        # Ввод имени для поиска
        search_name = input("Введите имя сотрудника для поиска: ").strip()

        # Проверяем, существует ли файл
        try:
            with open(csv_file, 'r', encoding='utf-8') as file:
                reader = csv.reader(file)
                headers = next(reader)  # Считываем заголовки

                # Поиск сотрудника
                for row in reader:
                    if row and row[0].strip().lower() == search_name.lower():
                        # Если найдено совпадение
                        employee_info = dict(zip(headers, row))
                        return f"Информация о сотруднике:\n{employee_info}"

                # Если сотрудник не найден
                return f"Сотрудник с именем '{search_name}' не найден."

        except FileNotFoundError:
            return f"Файл '{csv_file}' не найден. Убедитесь, что путь указан верно."

    except Exception as e:
        return f"Произошла ошибка: {e}"

csv_file = r'C:\Users\User\Desktop\python_tasks\DZ\dz9\task5\data.csv'  
result = find_employee_by_name(csv_file)
print(result)