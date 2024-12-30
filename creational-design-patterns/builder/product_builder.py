class Product:
    def __init__(self):
        self.part_a = None
        self.part_b = None
        self.part_c = None
        self.part_d = None

    def __str__(self):
        return f"Part A: {self.part_a} | Part B: {self.part_b} | Part C: {self.part_c} | Part D: {self.part_d}"
    
class ProductBuilder:
    def __init__(self):
        self._product = Product()

    def build_part_a(self, value):
        self._product.part_a = value

    def build_part_b(self, value):
        self._product.part_b = value

    def build_part_c(self, value):
        self._product.part_c = value

    def build_part_d(self, value):
        self._product.part_d = value

    def get_product(self):
        return self._product
    
if __name__ == "__main__":
    build = ProductBuilder()
    build.build_part_a(10)
    build.build_part_b(20)
    build.build_part_c(30)
    build.build_part_d(40)

    product = build.get_product()

    print(product)
    print("*" * 50)

    build.build_part_a(100)
    build.build_part_b(200)
    build.build_part_c(300)
    build.build_part_d(400)

    product = build.get_product()

    print(product)