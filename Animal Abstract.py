from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def move(self):
        pass

class Human(Animal):
    def move(self):
        print("I can walk and run")

class Snake(Animal):
    def move(self):
        print("I can crawl")

class Dog(Animal):
    def move(self):
        print("I can Bark")

class Lion(Animal):
    def move(self):
        print("I can roar")

R= Human()
R.move()

K=Snake()
K.move()

R= Dog()
R.move()

T= Lion()
T.move()