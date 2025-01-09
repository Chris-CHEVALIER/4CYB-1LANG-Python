from Vehicle import *

class Moto(Vehicle):
    def __init__(self, brand, model, color, power, has_side_car = False):
        super().__init__(brand, model, color, power)
        self.__has_side_car = has_side_car
        
    def start(self):
        print("La moto démarre !")