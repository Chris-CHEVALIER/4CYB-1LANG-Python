class Kart:
    def __init__(self, name, model_3d, speed, weight):
        self.__name = name
        self.__model_3d = model_3d
        self.__speed = speed
        self.__weight = weight
        
    # def display(self):
    #    print(f"Le kart {self.name} va a {self.speed}km/h et pèse {self.weight}kg.")
    
    def __str__(self):
        return f"Le kart {self.__name} va a {self.__speed}km/h et pèse {self.__weight}kg."
    
    def get_name(self):
        return self.__name
    
    def set_name(self, new_name):
        if 3 <= len(new_name) <= 15:
            self.__name = new_name
    
    def get_model_3d(self):
        return self.__model_3d
    
    def get_speed(self):
        return self.__speed
    
    def get_weight(self):
        return self.__weight
