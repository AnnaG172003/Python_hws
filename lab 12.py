class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
class Minivan(Car):
    def __init__(self, brand, model, year,  hasASD):
        super().__init__(brand, model,year)
        self.hasASD =hasASD
    pass
m1 = Minivan("GMC", "Sierra", "2024", True)
print(getattr(m1, "brand"), "", getattr(m1, "model"), " ", getattr(m1, "year"), " " ,getattr(m1, "hasASD"))