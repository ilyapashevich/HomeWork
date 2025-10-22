def calculate_bmi(weight, height):
    """
    Функция для расчёта индекса массы тела (ИМТ).
    :param weight: Вес в килограммах.
    :param height: Рост в метрах.
    :return: Значение ИМТ.
    """
    try:
        bmi = weight / (height ** 2)
        return round(bmi, 2)
    except ZeroDivisionError:
        return "Рост не может быть равен нулю!"

def bmi_category(bmi):
    """
    Функция для определения категории ИМТ.
    :param bmi: Значение ИМТ.
    :return: Категория ИМТ.
    """
    if bmi < 18.5:
        return "Недостаточный вес"
    elif 18.5 <= bmi < 24.9:
        return "Норма"
    elif 25 <= bmi < 29.9:
        return "Избыточный вес"
    else:
        return "Ожирение"

# Ввод данных
try:
    weight = float(input("Введите ваш вес (в кг): "))
    height = float(input("Введите ваш рост (в метрах): "))

    # Расчёт ИМТ
    bmi = calculate_bmi(weight, height)
    if isinstance(bmi, str):
        print(bmi)
    else:
        print(f"Ваш ИМТ: {bmi}")
        print(f"Категория: {bmi_category(bmi)}")
except ValueError:
    print("Пожалуйста, введите корректные числовые значения!")