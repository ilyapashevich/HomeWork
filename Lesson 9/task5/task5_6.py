import csv

# Функция для фильтрации сотрудников и вычисления среднего роста
def filter_by_birth_year_and_calculate_avg_height(csv_file):
    try:
        input_year = int(input("Введите год рождения: ").strip())

        try:
            with open(csv_file, 'r', encoding='utf-8') as file:
                reader = csv.reader(file)
                headers = next(reader)

                if "birthday" not in headers or "height" not in headers:
                    return "В файле отсутствуют необходимые столбцы: 'birthday' и/или 'height'."

                year_index = headers.index("birthday")
                height_index = headers.index("height")

                heights = []

                for row in reader:
                    if row:
                        try:
                            birth_year = int(row[year_index])
                            height = float(row[height_index])

                            if birth_year < input_year:
                                heights.append(height)
                        except ValueError:
                            continue

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

# Функция для отображения всех сотрудников
def display_all_employees(csv_file):
    try:
        with open(csv_file, 'r', encoding='utf-8') as file:
            reader = csv.reader(file)
            headers = next(reader)
            print("\nСписок сотрудников:")
            print(", ".join(headers))
            for row in reader:
                print(", ".join(row))
        return "Все сотрудники успешно отображены."
    except FileNotFoundError:
        return f"Файл '{csv_file}' не найден. Убедитесь, что путь указан верно."
    except Exception as e:
        return f"Произошла ошибка: {e}"

# Главное меню программы
def main_menu():
    csv_file = r'C:\Users\User\Desktop\python_tasks\DZ\dz9\task5\data.csv' 

    while True:
        print("\n=== Меню программы ===")
        print("1. Показать всех сотрудников")
        print("2. Фильтровать сотрудников по году рождения и вычислить средний рост")
        print("3. Выход из программы")

        choice = input("Выберите действие (1-3): ").strip()

        if choice == "1":
            print(display_all_employees(csv_file))
        elif choice == "2":
            print(filter_by_birth_year_and_calculate_avg_height(csv_file))
        elif choice == "3":
            print("Выход из программы. До свидания!")
            break
        else:
            print("Ошибка: выберите корректный пункт меню (1-3).")

if __name__ == "__main__":
    main_menu()