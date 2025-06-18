from basisklassen import FrontWheels, BackWheels
from basecar import BaseCar
import time


fw = FrontWheels()
bw = BackWheels()

car = BaseCar(fw, bw)
car.drive(50, int(90))
time.sleep(1)
car.stop()