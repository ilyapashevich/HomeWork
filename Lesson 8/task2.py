def calculator():
    print("Добро пожаловать в калькулятор!")
    print("Выберите операцию:")
    print("1. Сложение (+)")
    print("2. Вычитание (-)")
    print("3. Умножение (*)")
    print("4. Деление (/)")

    try:
        operation = input("Введите номер операции (1/2/3/4): ")

        if operation not in ['1', '2', '3', '4']:
            print("Ошибка: выбрана неверная операция.")
            return

        num1 = float(input("Введите первое число: "))
        num2 = float(input("Введите второе число: "))

        if operation == '1':
            result = num1 + num2
            print(f"Результат: {num1} + {num2} = {result}")
        elif operation == '2':
            result = num1 - num2
            print(f"Результат: {num1} - {num2} = {result}")
        elif operation == '3':
            result = num1 * num2
            print(f"Результат: {num1} * {num2} = {result}")
        elif operation == '4':
            if num2 == 0:
                print("Ошибка: деление на ноль невозможно.")
            else:
                result = num1 / num2
                print(f"Результат: {num1} / {num2} = {result}")
    except ValueError:
        print("Ошибка: введено некорректное значение. Попробуйте снова.")

calculator()