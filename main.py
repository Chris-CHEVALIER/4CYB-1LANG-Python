""" from Kart import Kart

moto = Kart("Moto", "./path/to/model-3d.3d", 230, 80)
print(moto.get_name()) """

from Car import *
from Moto import *

bmw = Moto("BMW", "S1000RR", "blanche", 210)
clio_3_rs = Car("Renault", "Clio 3 RS", "noire", 275, 5, 3)

bmw.start()
clio_3_rs.start()

bmw.display()
clio_3_rs.display()