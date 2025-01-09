class Vehicle:
    def __init__(self, brand, model, color, power):
        self.__brand = brand
        self.__model = model
        self.__color = color
        self.__power = power
        
    def display(self):
        print(f"Il s'agit d'une {self.__brand} {self.__model} {self.__color} avec une puissance {self.__power} chevaux !")