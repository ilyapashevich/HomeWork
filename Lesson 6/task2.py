n = int (input("Введите число "))
def con_num(n):
    result = ""
    while n > 0:
        result = str(n % 2) + result
        n = n // 2
    return result

binary = con_num(n)
print(f"{n} в двоичной системе счисления: {binary}")