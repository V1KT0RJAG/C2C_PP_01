from BaseCar_Main import BaseCar
from basisklassen import *


class SonicCar(BaseCar):
    def __init__(self, front, back, ultra):
        super().__init__(front, back)  # ruft von BaseCar auf
        self.ultra = ultra
        print("SonicCar wurde erzeugt")
        
    def get_distance(self):
        distance = self.ultra.distance()
        return distance




# fw = FrontWheels
# bw = BackWheels
# ul = Ultrasonic()


# cars = SonicCar(fw, bw, ul)

# cars.get_distance() 
