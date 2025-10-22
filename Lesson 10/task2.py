class MyTime:
    def __init__(self, *args):
        if not args:
            # Без параметров: 00:00:00
            self.hours = self.minutes = self.seconds = 0
 
        elif len(args) == 1:
            arg = args[0]
            if isinstance(arg, str):
                # Одна строка "HH:MM:SS"
                try:
                    h, m, s = map(int, arg.split(":"))
                    self.hours, self.minutes, self.seconds = h, m, s
                except ValueError:
                    raise ValueError("Строка должна быть в формате 'HH:MM:SS'")
            elif isinstance(arg, MyTime):
                # Копирование из другого объекта MyTime
                self.hours, self.minutes, self.seconds = (
                    arg.hours, arg.minutes, arg.seconds
                )
            else:
                raise TypeError("Ожидается строка или объект MyTime")

        elif len(args) == 3:
            # Три числа: часы, минуты, секунды
            self.hours, self.minutes, self.seconds = args

        else:
            raise ValueError("Неверное количество аргументов")

        self._normalize()

    def _normalize(self):
        """Приводит время к корректному виду, перераспределяя секунды и минуты."""
        total = self.hours * 3600 + self.minutes * 60 + self.seconds
        self.hours = total // 3600
        self.minutes = (total % 3600) // 60
        self.seconds = total % 60

    def to_seconds(self):
        """Возвращает общее число секунд."""
        return self.hours * 3600 + self.minutes * 60 + self.seconds

    def __str__(self):
        """Строковое представление HH:MM:SS."""
        return f"{self.hours:02}:{self.minutes:02}:{self.seconds:02}"

    # Магические методы сравнения
    def __eq__(self, other):
        return self.to_seconds() == other.to_seconds()

    def __ne__(self, other):
        return self.to_seconds() != other.to_seconds()

    def __lt__(self, other):
        return self.to_seconds() < other.to_seconds()

    def __le__(self, other):
        return self.to_seconds() <= other.to_seconds()

    def __gt__(self, other):
        return self.to_seconds() > other.to_seconds()

    def __ge__(self, other):
        return self.to_seconds() >= other.to_seconds()

    # Арифметические операции
    def __add__(self, other):
        if not isinstance(other, MyTime):
            raise TypeError("Можно складывать только с MyTime")
        return MyTime(0, 0, self.to_seconds() + other.to_seconds())

    def __sub__(self, other):
        if not isinstance(other, MyTime):
            raise TypeError("Можно вычитать только MyTime")
        return MyTime(0, 0, self.to_seconds() - other.to_seconds())

    def __mul__(self, factor):
        if not isinstance(factor, (int, float)):
            raise TypeError("Можно умножать только на число")
        return MyTime(0, 0, int(self.to_seconds() * factor))

    def __rmul__(self, factor):
        return self.__mul__(factor)

# Без параметров
t0 = MyTime()                 
print(t0)       

# Из строки
t1 = MyTime("12:65:83")       
print(t1)       

# Из трёх чисел
t2 = MyTime(1, 59, 120)       
print(t2)        

# Копирование
t3 = MyTime(t1)               
print(t3)        

# Арифметика и сравнения
print(t1 + t2)  
print(t1 - t2)  
print(t1 * 2)   
print(t1 > t2)  