class Car:
    def __init__(self, brand):
        self.brand = brand

my_car = Car("Toyota")



# Now check again
print(hasattr(my_car, "brand"))  # False
