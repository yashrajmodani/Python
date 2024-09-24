class Car:
    def __init__(self,brand,model,year):
        self.__brand = brand
        self.__model = model
        self.__year = year
    wheels = 4
    model = ""
    brand = ""
    year = ""

    def display_info(self):
        print(f"Information:\nThis car is {self.wheels} wheeler \nBrand: {self.brand}\nModel: {self.model}\nYear: {self.year}\n")

if __name__ =='__main__':
    car1 = Car("TOYOTA","AE86",2014)
    car1.brand="TOYOTA"
    car1.model = "AE86"
    car1.year = 2014

    car2 = Car("BMW","X3",2020)
    car2.brand="BMW"
    car2.model = "X4"
    car2.year = 2020

    car1.display_info()
    car2.display_info()