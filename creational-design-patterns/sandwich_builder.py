class Sandwich:
    def __init__(self):
        self._bread = None
        self._meat = None
        self._cheese = None
        self._vegetables = []
        self._sauces = []

    def __str__(self):
        ingredients = f'Bread: {self._bread} | Meat: {self._meat}'

        if self._cheese:
            ingredients += f' | Cheese: {self._cheese}'

        ingredients += f' | Vegetables: {", ".join(self._vegetables)}'
        ingredients += f' | Sauces: {", ".join(self._sauces)}'

        return ingredients
    
class SandwichBuilder:
    def __init__(self):
        self.sandwich = Sandwich()

    def add_bread(self):
        pass

    def add_meat(self):
        pass

    def add_cheese(self):
        pass

    def add_vegetables(self):
        pass

    def add_sauces(self):
        pass

    def get_sandwich(self):
        return self.sandwich
    

class ClubSandwichBuilder(SandwichBuilder):
    def add_bread(self):
        self.sandwich._bread = 'Club bread'

    def add_meat(self):
        self.sandwich._meat = 'Turkey'

    def add_cheese(self):
        self.sandwich._cheese = 'Cheddar'

    def add_vegetables(self):
        self.sandwich._vegetables = ['Tomato', 'Lettuce']

    def add_sauces(self):
        self.sandwich._sauces = ['Mayo', 'Mustard']

class VeggieSandwichBuilder(SandwichBuilder):
    def add_bread(self):
        self.sandwich._bread = 'Wheat bread'

    def add_meat(self):
        self.sandwich._meat = 'Tofu'

    def add_vegetables(self):
        self.sandwich._vegetables = ['Tomato', 'Lettuce', 'Cucumber']

    def add_sauces(self):
        self.sandwich._sauces = ['Vinegar', 'Oil']

class Waiter:
    def __init__(self):
        self.sandwich_builder = None

    def set_builder(self, builder):
        self.sandwich_builder = builder

    def create_sandwich(self):
        self.sandwich_builder.add_bread()
        self.sandwich_builder.add_meat()
        self.sandwich_builder.add_cheese()
        self.sandwich_builder.add_vegetables()
        self.sandwich_builder.add_sauces()

    def serve_sandwich(self):
        return self.sandwich_builder.get_sandwich()
    

if __name__ == '__main__':
    waiter = Waiter()
    waiter.set_builder(ClubSandwichBuilder())
    waiter.create_sandwich()
    print("======CLUB SANDWICH =======")
    sandwich1 = waiter.serve_sandwich() 
    print(sandwich1)

    waiter.set_builder(VeggieSandwichBuilder())
    waiter.create_sandwich()
    print("======VEGGIE SANDWICH =======")
    sandwich2 = waiter.serve_sandwich()
    print(sandwich2)