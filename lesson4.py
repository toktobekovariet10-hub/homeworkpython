from abc import ABC, abstractmethod

class  Animal(ABC):
    @abstractmethod
    def test        (self):
        pass

class Dog(Animal):
    def make_sound(self):
        print("гав гав гав")

    def test_sound(self):
        print("test in dog")

class Cat(Animal):

    def make_sound(self):
        print("мяу мяу мяу")

