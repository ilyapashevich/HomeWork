def process_file(file_path, s1=None, s2=None):
    try:
        # Открываем файл для чтения
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()  # Читаем все строки в список

        # a) Первая строка
        print("a) Первая строка:")
        if lines:
            print(lines[0].strip())
        else:
            print("Файл пуст.")

        # b) Пятая строка
        print("\nb) Пятая строка:")
        if len(lines) >= 5:
            print(lines[4].strip())
        else:
            print("В файле меньше 5 строк.")

        # c) Первые 5 строк
        print("\nc) Первые 5 строк:")
        for line in lines[:5]:
            print(line.strip())

        # d) Строки с s1-й по s2-ю
        if s1 is not None and s2 is not None:
            print(f"\nd) Строки с {s1}-й по {s2}-ю:")
            for line in lines[s1-1:s2]:
                print(line.strip())

        # e) Весь файл
        print("\ne) Весь файл:")
        for line in lines:
            print(line.strip())

    except FileNotFoundError:
        print(f"Файл {file_path} не найден.")
    except Exception as e:
        print(f"Произошла ошибка: {e}")

file_path = r"C:\Users\User\Desktop\python_tasks\DZ\dz9\task2,3\text_file.txt"

# Укажите значения s1 и s2 для пункта d
s1, s2 = 2, 4

process_file(file_path, s1, s2)