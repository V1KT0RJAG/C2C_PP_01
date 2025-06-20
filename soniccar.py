from basecar import BaseCar
from basisklassen import Ultrasonic, FrontWheels, BackWheels

#SonicCar Klasse
class SonicCar(BaseCar):
    def __init__(self, front, back, fahrmodi):
        super().__init__(front, back)
        self.fahrmodi = fahrmodi
        print("SonicCar erzeugt")
        print(self.fahrmodi)

    def get_distance(self):
        print('Sonic Car: distance measurement')
        usm = Ultrasonic()
        usm.test()

#test 
fw = FrontWheels()
bw = BackWheels() 

sc = SonicCar(fw, bw, 3)
sc.get_distance()