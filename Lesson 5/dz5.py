# task 1

N = int(input("Введите сумму телефона: "))
k = int(input("Введите сумму дня: "))
init_summ = 0
days = 0

while init_summ < N:
    days += 1
    if days % 7 != 0:  # Проверяем 7 день
        init_summ += k
print(f"Нужная сумма за {days} дней.")


# task 2

n = int(input("Введите количество чисел Фибоначчи: "))
fibon = [1, 1] # первые два числа равны 1

for i in range(2, n):
    next_number = fibon[i - 1] + fibon[i - 2]
    fibon.append(next_number)

for number in fibon:
    print(number, end=' ')


# task 3

numbers = [1, 3, 9, 15, 25, 55, 90]

sum_numbers = sum(numbers)

min_number = min(numbers)
max_number = max(numbers)

print("Сумма чисел:", sum_numbers)
print("Минимальное число:", min_number)
print("Максимальное число:", max_number)


# task 4

list_numb = [8, 7, 52, 8, 45, 27, 52, 22, 11, 9, 1, 8]

duplicats = []
uniq = True

for number in list_numb:
    if list_numb.count(number) > 1:
        if number not in duplicats:
            duplicats.append(number)
        uniq = False

if uniq:
    print("Все числа в списке уникальны.")
else:
    print("Числа в списке не уникальны.")
    print("Дублирующиеся элементы:", duplicats)
    for duplicate in duplicats:
        print(f"Количество повторений элемента {duplicate}: {list_numb.count(duplicate)}")