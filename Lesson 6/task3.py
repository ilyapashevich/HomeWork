import math

number = int(input("Введите число "))
def proverka(number):
    if number < 2:
        return None
    else:
        for i in range(2, int(math.sqrt(number)) + 1):
            if number % i == 0:
                return False
        return True

result = proverka(number)
if result == True:
    print(f"{number} простое число")
elif result == False:
    print(f"{number} не простое число")
else:
    print(f"число {number} <= 1")