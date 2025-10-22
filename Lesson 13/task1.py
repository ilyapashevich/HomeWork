def cycle_sequence(values):
    """Генератор бесконечной циклической последовательности"""
    while True:
        for v in values:
            yield v

if __name__ == "__main__":
    try:
        count = int(input("Сколько чисел вывести? "))
        if count <= 0:
            print("Введите положительное число.")
        else:
            generator = cycle_sequence([1, 2, 3])
            for _ in range(count):
                print(next(generator), end=" ")
    except ValueError:
        print("Ошибка: введите целое число.")