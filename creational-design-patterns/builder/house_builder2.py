class House:
    def __init__(self):
        self.floor = None
        self.wall = None
        self.roof = None
        self.furniture = dict()

    def __str__(self):
        return f"Floor: {self.floor} | Wall: {self.wall} | Roof: {self.roof} | Furniture: {self.furniture}"
    
class HouseBuilder:
    def __init__(self):
        self._house = House()

    def set_floor(self, amount):
        self._house.floor = amount
        return self

    def set_wall(self, amount):
        self._house.wall = amount
        return self

    def set_roof(self, amount):
        self._house.roof = amount
        return self

    def set_furniture(self, name, amount):
        if not self._house.furniture.get(name):
            self._house.furniture[name] = 0
        self._house.furniture[name] += amount
        return self

    def get_house(self):
        return self._house
    
class SmallHouseBuilder(HouseBuilder):
    def build_floor(self):
        self.set_floor("Small floor")
    
    def build_wall(self):
        self.set_wall("Small wall")

    def build_roof(self):
        self.set_roof("Small roof")
    
    def build_furnitures(self):
        self.set_furniture("Chairs",5)
        self.set_furniture("Chairs", 4)
        self.set_furniture("Tables", 8)

class BigHouseBuilder(HouseBuilder):
    def build_floor(self):
        self.set_floor("Big floor")

    def build_wall(self):
        self.set_wall("Big wall")

    def build_roof(self):
        self.set_roof("Big roof")
        
    def build_furnitures(self):
        self.set_furniture("Sofa",30)
        self.set_furniture("Cabinets", 28)
        self.set_furniture("Stools", 34)
        self.set_furniture("Leg Rest", 27)

class Contractor: #director
    def __init__(self, builder):
        self.builder = builder

    def construct_house(self):
        self.builder.build_floor()
        self.builder.build_wall()
        self.builder.build_roof()
        self.builder.build_furnitures()

if __name__ == "__main__":
    small_builder = SmallHouseBuilder()
    big_builder = BigHouseBuilder()

    contractor = Contractor(small_builder)
    contractor.construct_house()
    small_house = small_builder.get_house()
    print("Small House:")
    print(small_house)

    contractor = Contractor(big_builder)
    contractor.construct_house()
    big_house = big_builder.get_house()
    print("Big House:")
    print(big_house)