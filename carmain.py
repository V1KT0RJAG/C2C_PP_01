from basisklassen import FrontWheels, BackWheels
from basecar import BaseCar
import time


fw = FrontWheels()
bw = BackWheels() 

car = BaseCar(fw, bw)

car.drive(50, new_angle=90)
print(fw._turning_offset)

time.sleep(1)
car.stop()