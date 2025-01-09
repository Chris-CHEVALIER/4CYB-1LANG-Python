from Vehicle import *

class Car(Vehicle):
    def __init__(self, brand, model, color, power, seat_number, door_number):
        super().__init__(brand, model, color, power)
        self.__seat_number = seat_number
        self.__door_number = door_number
        
    def start(self):
        print("La voiture démarre !")