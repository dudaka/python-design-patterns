from abc import ABC, abstractmethod

class Furniture(ABC):
    def __init__(self, quantity):
        self.quantity = quantity

    @abstractmethod
    def display(self):
        pass
    
class Chair(Furniture):
    def display(self):
        print(f"Chair: {self.quantity}")

class Sofa(Furniture):
    def display(self):
        print(f"Sofa: {self.quantity}")
    
class Electronic(ABC):
    def __init__(self, quantity):
        self.quantity = quantity

    @abstractmethod
    def display(self):
        pass
    
class Television(Electronic):
    def display(self):
        print(f"Television: {self.quantity}")

class Radio(Electronic):
    def display(self):
        print(f"Radio: {self.quantity}")
    

class Decoration(ABC):
    def __init__(self, quantity):
        self.quantity = quantity

    @abstractmethod
    def display(self):
        pass
        

class FlowerVase(Decoration):
    def display(self):
        print(f"Flower Vase: {self.quantity}")

class Chandalier(Decoration):
    def display(self):
        print(f"Chandalier: {self.quantity}")

class HouseFactory(ABC):
    @abstractmethod
    def furniture(self, quantity):
        pass

    @abstractmethod
    def electronic(self, quantity):
        pass

    @abstractmethod
    def decoration(self, quantity):
        pass
    
class SmallHouse(HouseFactory):
    def furniture(self):
        return Chair(4)

    def electronic(self):
        return Radio(2)

    def decoration(self):
        return FlowerVase(4)
    
class BigHouseHouse(HouseFactory):
    def furniture(self):
        return Sofa(10)

    def electronic(self):
        return Television(7)

    def decoration(self):
        return Chandalier(4)
    
def client(factory: HouseFactory):
    print(factory.furniture().display())
    print(factory.electronic().display())
    print(factory.decoration().display())
    print()


if __name__ == "__main__":

  print("Small House".center(40, "-"))
  client(SmallHouse())