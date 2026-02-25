class Car:
    def __init__(self, brand,model,year,mileage,price):
        self.brand = brand
        self.model = model
        self.year = year
        self.mileage = mileage
        self.price = price
    def display_info(self):
        print("Brand ",self.brand)
        print("Model ",self.model)
        print("Year ", self.year)
        print("Mileage ", self.mileage)
        print("Price " , self.price)
    def update_price(self, new_price):
        self.price = new_price
        print("Price updated.....")
        print(".....................")
        self.display_info()
class Sedan(Car):
     def __init__(self, brand,model,year,mileage,price,mpg,comfort_level):
         super().__init__(brand,model,year,mileage,price)
         self.mpg = mpg
         self.comfort_level = comfort_level
class SUV(Car):
    def __init__(self,brand,model,year,mileage,price,four_wheel_drive,off_road_capability):
        super().__init__(brand,model,year,mileage,price)
        self.four_wheel_drive =four_wheel_drive
        self.off_road_capability = off_road_capability
my_sedan = Sedan('Toyota','Camry',2022,15000,22000,33,'High')
my_suv = SUV('Jeep','Normal','2022',10000,35000,True,True)
my_sedan.display_info()
print("...........")
my_suv.display_info()
my_sedan.update_price(21000)
my_suv.update_price(30000)