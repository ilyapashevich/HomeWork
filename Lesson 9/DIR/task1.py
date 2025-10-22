import os
import shutil

# 1
name_oc = os.name
print(f"Наша OC: {name_oc}")

# 2
script_directory = os.path.dirname(os.path.abspath(__file__))
print(f"Папка скрипта: {script_directory}")

# 3
def sort_files_by_extension_and_rename(directory):
    # Проверяем, существует ли директория
    if not os.path.exists(directory):
        print(f"Директория {directory} не найдена.")
        return

    # Словарь для хранения информации о перемещенных файлах
    stats = {}

    # Перебираем файлы в директории
    for file in os.listdir(directory):
        file_path = os.path.join(directory, file)

        # Пропускаем папки
        if os.path.isdir(file_path):
            continue

        # Получаем расширение файла
        file_extension = os.path.splitext(file)[1][1:]  # Убираем точку
        if not file_extension:  # Если у файла нет расширения
            file_extension = "Без_расширения"

        # Создаем папку для расширения, если её нет
        extension_folder = os.path.join(directory, file_extension)
        os.makedirs(extension_folder, exist_ok=True)

        # Перемещаем файл в соответствующую папку
        shutil.move(file_path, os.path.join(extension_folder, file))

        # Обновляем статистику
        file_size = os.path.getsize(os.path.join(extension_folder, file))  # Размер файла в байтах
        if file_extension not in stats:
            stats[file_extension] = {"count": 0, "size": 0}
        stats[file_extension]["count"] += 1
        stats[file_extension]["size"] += file_size

    # Переименование хотя бы одного файла в каждой поддиректории
    for ext, data in stats.items():
        extension_folder = os.path.join(directory, ext)
        files_in_folder = os.listdir(extension_folder)

        if files_in_folder:  # Если в папке есть файлы
            old_name = files_in_folder[0]  # Берем первый файл
            old_path = os.path.join(extension_folder, old_name)

            # Генерируем новое имя
            new_name = f"renamed_{old_name}"
            new_path = os.path.join(extension_folder, new_name)

            # Переименовываем файл
            os.rename(old_path, new_path)

            # Выводим сообщение о переименовании
            print(f"Файл {old_name} был переименован в {new_name}.")

    # Выводим статистику
    for ext, data in stats.items():
        size_in_gb = data["size"] / (1024 ** 3)  # Перевод размера в гигабайты
        print(f"В папке с файлами типа '{ext}' перемещено {data['count']} файлов, их суммарный размер – {size_in_gb:.2f} ГБ.")

    print("Сортировка и переименование завершены!")

directory_path = r"C:\Users\User\Desktop\python_tasks\DZ\dz9\DIR"
sort_files_by_extension_and_rename(directory_path)