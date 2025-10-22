class Car:
    def __init__(self, brand, model, year):
        self.__brand = brand
        self.__model = model
        self.__year = year
        self.__speed = 0
        self.__max_speed = 200  # Максимальная скорость

    def accelerate(self):
        if self.__speed + 5 <= self.__max_speed:
            self.__speed += 5
        else:
            self.__speed = self.__max_speed
 
    def decelerate(self):
        if self.__speed - 5 >= 0:
            self.__speed -= 5
        else:
            self.__speed = 0

    def stop(self):
        self.__speed = 0

    def show_speed(self):
        print(f"Текущая скорость: {self.__speed} км/ч")

    def reverse(self):
        self.__speed = -self.__speed

    def car_info(self):
        print(f"Марка: {self.__brand}, Модель: {self.__model}, Год: {self.__year}")

if __name__ == "__main__":
    my_car = Car("Toyota", "Camry", 2020)
    my_car.car_info()
    my_car.accelerate()
    my_car.show_speed()
    my_car.accelerate()
    my_car.show_speed()
    my_car.decelerate()
    my_car.show_speed()
    my_car.reverse()
    my_car.show_speed()
    my_car.stop()
    my_car.show_speed()