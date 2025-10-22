'''
[
    {
        "name": "John Smith",
        "birthday": "02.10.1990",
        "height": 175,
        "weight": 76.5,
        "car": true,
        "languages": ["C++", "Python"]
    },
    {
        "name": "Alexey Alexeev",
        "birthday": "05.06.1986",
        "height": 197,
        "weight": 101.2,
        "car": false,
        "languages": ["Pascal", "Delphi"]
    },
    {
        "name": "Maria Ivanova",
        "birthday": "28.08.1998",
        "height": 165,
        "weight": 56.1,
        "car": true,
        "languages": ["C#", "C++", "C"]
    }
]
'''

import json
import csv

def json_to_csv_with_nested(json_file, csv_file):
    try:
        # Чтение данных из JSON-файла
        with open(json_file, 'r', encoding='utf-8') as jf:
            data = json.load(jf)

        # Проверка, что данные являются списком словарей
        if not isinstance(data, list):
            return "Ошибка: JSON-файл должен содержать список объектов (массив)."

        # Получение заголовков (ключей) из первого объекта
        headers = data[0].keys()

        # Запись данных в CSV-файл
        with open(csv_file, 'w', encoding='utf-8', newline='') as cf:
            writer = csv.DictWriter(cf, fieldnames=headers)
            writer.writeheader()  # Записываем заголовки

            # Обработка строк
            for row in data:
                # Преобразуем вложенные данные (например, массивы) в строку
                row = {key: (", ".join(value) if isinstance(value, list) else value) for key, value in row.items()}
                writer.writerow(row)

        return f"Данные успешно преобразованы из {json_file} в {csv_file}."
    except FileNotFoundError:
        return f"Ошибка: Файл {json_file} не найден."
    except json.JSONDecodeError:
        return "Ошибка: Неверный формат JSON-файла."
    except Exception as e:
        return f"Произошла ошибка: {e}"

json_file = r'C:\Users\User\Desktop\python_tasks\DZ\dz9\task5\data.json'  
csv_file = r'C:\Users\User\Desktop\python_tasks\DZ\dz9\task5\data.csv'    
result = json_to_csv_with_nested(json_file, csv_file)
print(result)