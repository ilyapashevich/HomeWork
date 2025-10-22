numbers = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
value = int(input("Введите число: "))

def binar_search(numbers, value):
    if len(numbers) == 0:
        return -1
    else:
        mid = len(numbers) // 2
        if numbers[mid] == value:
            return mid
        elif value < numbers[mid]:
            return binar_search(numbers[:mid], value)
        else:
            result = binar_search(numbers[mid+1:], value)
            if result == -1:
                return -1
            else:
                return mid + result + 1

pos = binar_search(numbers, value)
if pos == -1:
    print("Элемент отсутствует")
else:
    print(f"Позиция элемента = {pos}")