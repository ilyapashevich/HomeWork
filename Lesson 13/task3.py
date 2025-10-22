from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Гав-гав!"

class Cat(Animal):
    def speak(self):
        return "Мяу!"

class AnimalFactory:
    def create_animal(self, animal_type: str) -> Animal:
        animal_type = animal_type.lower()
        if animal_type == "dog":
            return Dog()
        elif animal_type == "cat":
            return Cat()
        else:
            raise ValueError(f"Неизвестный тип животного: {animal_type}")

factory = AnimalFactory()

a1 = factory.create_animal("dog")
print(a1.speak())  # Гав-гав!

a2 = factory.create_animal("cat")
print(a2.speak())  # Мяу!
