from abc import *


class AbstractAnimal(metaclass=ABCMeta):
    name = "name"
    weight = 0
    height = 0

    @abstractmethod
    def description(self):
        print("description")


class Flyable:
    def fly(self):
        print("fly")


class NonFlyable:
    def fly(self):
        print("can't fly")


class Runable:
    def run(self):
        print("run")


class NonRunable:
    def run(self):
        print("can't run")


class Dog(AbstractAnimal, Runable, NonFlyable):
    def __init__(self, name, weight, height):
        self.name = name
        self.weight = weight
        self.height = height

    def description(self):
        print(
            f"dog description, name: {self.name}, weight: {self.weight}, height: {self.height}"
        )


Albi = Dog("Albi", 22, 100)
Albi.description()
Albi.run()
Albi.fly()


class Bird(AbstractAnimal, NonRunable, Flyable):
    def __init__(self, name, weight, height):
        self.name = name
        self.weight = weight
        self.height = height

    def description(self):
        print(
            f"bird description, name: {self.name}, weight: {self.weight}, height: {self.height}"
        )


Sevi = Bird("Sevi", 16, 60)
Sevi.description()
Sevi.run()
Sevi.fly()
