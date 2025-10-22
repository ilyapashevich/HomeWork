import csv
import os

def add_employee_to_csv(csv_file):
    try:
        # Проверяем, существует ли файл
        file_exists = os.path.isfile(csv_file)

        # Ввод данных о новом сотруднике
        print("Введите данные о новом сотруднике:")
        name = input("Имя: ")
        age = int(input("Возраст: "))
        position = input("Должность: ")
        department = input("Отдел: ")
        salary = float(input("Зарплата: "))

        # Формирование строки данных
        new_employee = [name, age, position, department, salary]

        # Открытие файла в режиме добавления
        with open(csv_file, 'a', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)

            # Если файл создается впервые, добавляем заголовки
            if not file_exists:
                writer.writerow(["Имя", "Возраст", "Должность", "Отдел", "Зарплата"])

            # Добавляем данные нового сотрудника
            writer.writerow(new_employee)

        return f"Сотрудник {name} успешно добавлен в файл {csv_file}."

    except ValueError:
        return "Ошибка: Некорректный ввод данных."
    except Exception as e:
        return f"Произошла ошибка: {e}"

csv_file = r'C:\Users\User\Desktop\python_tasks\DZ\dz9\task5\data.csv' 
result = add_employee_to_csv(csv_file)
print(result)