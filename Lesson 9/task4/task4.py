def compare_files(file1, file2):
    try:
        # Открываем оба файла для чтения
        with open(file1, 'r', encoding='utf-8') as f1, open(file2, 'r', encoding='utf-8') as f2:
            # Читаем строки из обоих файлов
            lines1 = f1.readlines()
            lines2 = f2.readlines()

            # Проверяем, совпадает ли количество строк
            if len(lines1) != len(lines2):
                return f"Файлы имеют разное количество строк: {len(lines1)} и {len(lines2)}."

            # Сравниваем строки по порядку
            for i, (line1, line2) in enumerate(zip(lines1, lines2), start=1):
                if line1.strip() != line2.strip():  # Убираем лишние пробелы и переносы строк
                    return f"Файлы отличаются на строке {i}:\nФайл 1: {line1.strip()}\nФайл 2: {line2.strip()}"

            return "Все строки в файлах совпадают."
    except FileNotFoundError as e:
        return f"Ошибка: {e}"
    except Exception as e:
        return f"Произошла ошибка: {e}"

file1 = r'C:\Users\User\Desktop\python_tasks\DZ\dz9\task4/file1.txt'
file2 = r'C:\Users\User\Desktop\python_tasks\DZ\dz9\task4/file2.txt'
result = compare_files(file1, file2)
print(result)