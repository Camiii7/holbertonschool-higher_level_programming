#!/usr/bin/python3
from abc import ABC, abstractmethod

class Fish(ABC):
    @abstractmethod
    def swim(self):
        pass

    @abstractmethod
    def habitat(self):
        pass

class Bird(ABC):
    @abstractmethod
    def fly(self):
        pass

    @abstractmethod
    def habitat(self):
        pass

class FlyingFish(Fish, Bird):
    def fly(self):
        print("The flying fish is soaring!")

    def swim(self):
        print("The flying fish is swimming!")

    def habitat(self):
        print("The flying fish lives both in water and the sky!")

if __name__ == "__main__":
    flying_fish = FlyingFish()
    flying_fish.swim()
    flying_fish.fly()
    flying_fish.habitat()
    print(FlyingFish.mro())

