def create_and_write_file(file_path):
    try:
        # Открываем файл для записи
        with open(file_path, 'w', encoding='utf-8') as file:
            print("Введите 6 строк для записи в файл:")
            for i in range(1, 7):
                line = input(f"Строка {i}: ")  # Ввод строки с клавиатуры
                file.write(line + '\n')  # Записываем строку в файл с переносом строки
        print(f"Файл успешно создан и записан: {file_path}")
    except Exception as e:
        print(f"Произошла ошибка: {e}")

file_path = r"C:\Users\User\Desktop\python_tasks\DZ\dz9\task2,3/text_file.txt"

create_and_write_file(file_path)