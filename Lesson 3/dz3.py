# task 1

a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
c = int(input("Введите третье число: "))
summa = a + b + c
dif = a - b - c
mult = a * b * c
ex_1 = (a - b) + c
ex_2 = (a * b) / c
ex_3 = (a + b) % c
print(f"Сумма чисел: {summa}")
print(f"Разность чисел: {dif}")
print(f"Произведение чисел: {mult}")
print(ex_1)  #  От первой переменной отнять вторую и прибавить третью
print(ex_2)  #  Поделить произведение двух переменных на третью
print(ex_3)  #  От суммы первых 2-ух переменных найти остаток от деления на 3-ю

# task 2

import math

cat_a = float(input("Введите длину первого катета: "))
cat_b = float(input("Введите длину второго катета: "))
sq = (1 / 2) * cat_a * cat_b
hyp = math.sqrt(cat_a**2 + cat_b**2)
print(f"Площадь треугольника: {sq}")
print(f"Длина гипотенузы: {hyp}")

# task 3

s_3 = "test1 test2 test3 test4 test5"

# Разделение строки на слова и подсчет их количества
txt = len(s_3.split())
print(f"Количество слов в строке: {txt}")

# task 4

s_4 = "hhhabchghhh"

# replace заменяет вхождения одной подстроки на другую
# count считает количество вхождений подстроки
txt_1 = s_4.replace("h", "H", s_4.count("h") - 1).replace("H", "h", 1)
print(txt_1)

# task 5

s_5 = "Hello"
print(s_5[2])
print(s_5[-2])
print(s_5[:5])
print(s_5[:-2])
print(s_5[::2])
print(s_5[1::2])
print(s_5[::-1])
print(s_5[::-2])
print(len(s_5))

s2_5 = "TEST-STR"
print(s2_5[2])
print(s2_5[-2])
print(s2_5[:5])
print(s2_5[:-2])
print(s2_5[::2])
print(s2_5[1::2])
print(s2_5[::-1])
print(s2_5[::-2])
print(len(s2_5))

# task 6

s_6 = int(input("Введите трехзначное число: "))
print(s_6 % 10) # Выводим последнее число вычисляя остаток от заданного числа

# task 7

s_7 = int(input("Введите трехзначное число: "))
s_72 = (s_7 // 10) % 10 # Делим число на 10 и находим остаток
print(s_72, "Десятков")

# task 84 

s_8 = int(input("Введите трехзначное число: "))

# Преобразуем введенное число в строку и каждую цифру из числа, затем их суммируем
s_82 = sum(int(digit) for digit in str(s_8))
print(f"Сумма чисел: " + str(s_82))