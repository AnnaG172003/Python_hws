from abc import ABC, abstractmethod
class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass
class Car(Vehicle):
    def start_engine(self):
        return "Car engine started."

class Motorcycle(Vehicle):
     def start_engine(self):
        return "Motorcycle engine started."

car = Car()
motorcycle = Motorcycle()
print(car.start_engine())
print(motorcycle.start_engine())

