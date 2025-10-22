import csv

def filter_by_birth_year_and_calculate_avg_height(csv_file):
    try:
        # Ввод года рождения
        input_year = int(input("Введите год рождения: ").strip())

        # Проверяем, существует ли файл
        try:
            with open(csv_file, 'r', encoding='utf-8') as file:
                reader = csv.reader(file)
                headers = next(reader)  # Считываем заголовки

                # Проверяем наличие необходимых столбцов
                if "birthday" not in headers or "height" not in headers:
                    return "В файле отсутствуют необходимые столбцы: 'birthday' и/или 'height'."

                # Индексы столбцов
                year_index = headers.index("birthday")
                height_index = headers.index("height")

                # Список ростов сотрудников, чей год рождения меньше заданного
                heights = []

                for row in reader:
                    if row:
                        try:
                            birth_year = int(row[year_index])
                            height = float(row[height_index])

                            if birth_year < input_year:
                                heights.append(height)
                        except ValueError:
                            # Пропускаем строки с некорректными данными
                            continue

                # Вычисление среднего роста
                if heights:
                    avg_height = sum(heights) / len(heights)
                    return f"Средний рост сотрудников, родившихся до {input_year} года: {avg_height:.2f} см."
                else:
                    return f"Сотрудников, родившихся до {input_year} года, не найдено."

        except FileNotFoundError:
            return f"Файл '{csv_file}' не найден. Убедитесь, что путь указан верно."

    except ValueError:
        return "Ошибка: введите корректный год рождения."

    except Exception as e:
        return f"Произошла ошибка: {e}"

csv_file = r'C:\Users\User\Desktop\python_tasks\DZ\dz9\task5\data.csv' 
result = filter_by_birth_year_and_calculate_avg_height(csv_file)
print(result)