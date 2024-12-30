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
    
if __name__ == "__main__":
    print("===== Small House =====")
    small_house_builder = HouseBuilder()
    small_house_builder.set_floor(9).set_wall(12).set_furniture('Chairs',5).set_furniture('Tables',4).set_furniture('Tables',8)

    small_house = small_house_builder.get_house()
    print(small_house)

    print("===== Big House =====")
    big_house_builder = HouseBuilder()
    big_house_builder.set_floor(20).set_wall(30).set_roof(1).set_furniture('Chairs',10).set_furniture('Tables',20).set_furniture('Tables',40)

    big_house_builder.set_furniture('Sofas',5).set_furniture('Sofas',10).set_furniture('Sofas',15)

    big_house = big_house_builder.get_house()
    print(big_house)