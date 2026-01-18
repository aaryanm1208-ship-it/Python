class Car:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year

c1 = Car("BMW", 2022)
c2 = Car("Audi", 2023)

print(c1.brand, c1.year)
print(c2.brand, c2.year)
