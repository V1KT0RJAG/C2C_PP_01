from basisklassen import FrontWheels, BackWheels
from basecar import BaseCar
import time


fw = FrontWheels()
bw = BackWheels()

car = BaseCar(fw, bw)
time.sleep(2)
car.drive(new_angle=90)
#time.sleep(2)
#car.drive(new_angle=130)
#time.sleep(4)
car.stop