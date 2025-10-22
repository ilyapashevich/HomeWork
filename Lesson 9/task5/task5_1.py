import json

def add_employee_to_json(json_file):
    try:
        # Чтение существующих данных из JSON-файла
        try:
            with open(json_file, 'r', encoding='utf-8') as file:
                data = json.load(file)
        except FileNotFoundError:
            # Если файл не существует, создаем пустой список
            data = []

        # Проверка, что данные являются списком
        if not isinstance(data, list):
            return "Ошибка: JSON-файл должен содержать список объектов (массив)."

        # Ввод данных о новом сотруднике
        print("Введите данные о новом сотруднике:")
        name = input("Имя: ")
        age = int(input("Возраст: "))
        position = input("Должность: ")
        department = input("Отдел: ")
        salary = float(input("Зарплата: "))

        # Формирование объекта сотрудника
        new_employee = {
            "name": name,
            "age": age,
            "position": position,
            "department": department,
            "salary": salary
        }

        # Добавление нового сотрудника в список
        data.append(new_employee)

        # Запись обновленных данных в JSON-файл
        with open(json_file, 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)

        return f"Сотрудник {name} успешно добавлен в файл {json_file}."

    except ValueError:
        return "Ошибка: Некорректный ввод данных."
    except Exception as e:
        return f"Произошла ошибка: {e}"

json_file = r'C:\Users\User\Desktop\python_tasks\DZ\dz9\task5\data.json'
result = add_employee_to_json(json_file)
print(result)